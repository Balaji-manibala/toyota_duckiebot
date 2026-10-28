FROM ros:humble-ros-base

SHELL ["/bin/bash", "-c"]

WORKDIR /robot_monitor_ws

COPY src/ ./src/

RUN source /opt/ros/humble/setup.bash && \
    colcon build --packages-select robot_monitor

CMD ["bash", "-lc", "source /opt/ros/humble/setup.bash && source /robot_monitor_ws/install/setup.bash && ros2 run robot_monitor robot_health_publisher"]
