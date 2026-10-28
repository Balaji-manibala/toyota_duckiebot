import random

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotHealthPublisher(Node):

    def __init__(self):
        super().__init__('robot_health_publisher')

        self.publisher = self.create_publisher(
            String,
            '/robot/health',
            10
        )

        self.timer = self.create_timer(
            2.0,
            self.publish_health
        )

        self.get_logger().info(
            'Robot Health Publisher started'
        )

    def publish_health(self):
        # Generate simulated sensor readings.
        battery = random.randint(10, 100)
        temperature = random.randint(25, 75)
        obstacle_distance = round(
            random.uniform(0.1, 3.0), 2
        )

        # Classify battery status.
        if battery < 20:
            battery_status = 'LOW BATTERY'
        else:
            battery_status = 'NORMAL'

        # Classify motor temperature.
        if temperature >= 60:
            temperature_status = 'HIGH TEMPERATURE'
        else:
            temperature_status = 'NORMAL'

        # Classify obstacle distance.
        if obstacle_distance < 0.5:
            obstacle_status = 'OBSTACLE NEAR'
        else:
            obstacle_status = 'CLEAR'

        # Construct the health message.
        message = String()
        message.data = (
            f'Battery={battery}% ({battery_status}) | '
            f'MotorTemp={temperature}C '
            f'({temperature_status}) | '
            f'Obstacle={obstacle_distance}m '
            f'({obstacle_status})'
        )

        # Publish the message.
        self.publisher.publish(message)

        # Display the published health information.
        self.get_logger().info(message.data)


def main(args=None):
    rclpy.init(args=args)

    node = RobotHealthPublisher()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
