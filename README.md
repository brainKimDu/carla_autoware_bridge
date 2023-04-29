# carla_autoware_bridge
An addition package to `carla_ros_bridge` to connect CARLA simulator to Autoware Universe software.

Warning! This is **Work in Progress** repository. Reports and improvement suggestions are very welcome.

![demo_with_traffic](images/demo_with_traffic.png)

![image](https://user-images.githubusercontent.com/110883172/235323835-ff28b58b-4dbc-4a88-9400-ce87799acee6.png)


## Why carla_autoware_bridge is required?

However there is no official support of the Autoware Universe self-driving open source project from CARLA developers, there is a maintained `carla_ros_bridge`, which supports communication between CARLA simulator and ROS2 applications. This ROS2 package reuses `carla_ros_bridge` and adds missing things to support communicating with the Autoware Universe.

## Getting started tutorial

Go to [Getting started](getting-started.md) tutorial to setup and launch autoware simulation with CARLA simulator.



## the differences between the current git and the original one
I have merged the traffic signal information of Carla and Autoware together. 

I have improved the content in the tutorial section.



## My System
### Hardware
- RTX 3080
- CPU I7 9700KF
- RAM 32GB
### Software
- Ubuntu 20.04
- Nvidia-Driver 530
- CUDA 11.6
- cuDNN 8.7.0
- ROS2 Foxy
- Autoware Universe Docker Humble
- Carla 0.9.13

There is an issue with the odometry of Carla and Autoware not matching in my version, possibly due to a version problem
