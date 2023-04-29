from autoware_auto_perception_msgs.msg import TrafficSignal, TrafficLight, TrafficSignalArray
from carla_msgs.msg import CarlaTrafficLightStatusList
from rclpy.node import Node
from std_msgs.msg import Header
import rclpy

class TrafficlightNode(Node):

    def __init__(self) -> None:
        super().__init__('traffic_light')

        self.carla_traffic = self.create_subscription(
            CarlaTrafficLightStatusList, '/carla/traffic_lights/status',
            self._carla_traffic_callback, 1)

        self.auto_traffic = self.create_publisher(
            TrafficSignalArray, '/perception/traffic_light_recognition/traffic_signals', 1)
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.autoware_traffic_lights = []

    def _carla_traffic_callback(self, carla_traffic_msg):
        self.autoware_traffic_lights = []
        for traffic_light in carla_traffic_msg.traffic_lights:
            
            if traffic_light.id == 28:
                lights = [TrafficLight(color=traffic_light.state + 1, shape=5, status=14, confidence=1.0)]
                signal = TrafficSignal(map_primitive_id=29733, lights=lights)
                self.autoware_traffic_lights.append(signal)
            elif traffic_light.id == 38:
                lights = [TrafficLight(color=traffic_light.state + 1, shape=5, status=14, confidence=1.0)]
                signal = TrafficSignal(map_primitive_id=29847, lights=lights)
                self.autoware_traffic_lights.append(signal)
            elif traffic_light.id == 50:
                lights = [TrafficLight(color=traffic_light.state + 1, shape=5, status=14, confidence=1.0)]
                signal = TrafficSignal(map_primitive_id=29913, lights=lights)
                self.autoware_traffic_lights.append(signal)
        
    def timer_callback(self):
        if self.autoware_traffic_lights is not None:
            header = Header(stamp=self.get_clock().now().to_msg(), frame_id='')
            signal_array = TrafficSignalArray(header=header, signals=self.autoware_traffic_lights)   
            self.auto_traffic.publish(signal_array)
            print(signal_array)



def main(args=None):
    rclpy.init(args=args)
    Traffic = TrafficlightNode()

    rclpy.spin(Traffic)

    Traffic.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
