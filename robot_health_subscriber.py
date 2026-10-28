nano robot_health_subscriber.py
Paste the following complete Python program:

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class RobotHealthSubscriber(Node):
  def __init__(self):
    super().__init__('robot_health_subscriber')
    self.subscription = self.create_subscription(String,'/robot/health',self.health_callback,10)
    self.get_logger().info('Robot Health Subscriber started')
    self.get_logger().info('Listening to /robot/health')
  def health_callback(self, message):
    self.get_logger().info('Received robot health: ' + message.data)
def main(args=None):
  rclpy.init(args=args)
  node = RobotHealthSubscriber()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  finally:
    node.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
  main()
