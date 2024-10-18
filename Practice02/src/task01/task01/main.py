import rclpy
from std_msgs.msg import String
from rclpy.node import Node

class TopicsNode(Node):
	def __init__(self):
			super(TopicsNode, self).__init__('imposter')
			self.subscriber = self.create_subscription(String,
				'/spgc/sender',
				self.subscriber_callback,
				qos_profile=10)

	def subscriber_callback(self, msg):
			self.get_logger().info(f"{msg.data}")

def main():
	rclpy.init()
	node = TopicsNode()
	rclpy.spin(node)
	rclpy.shutdown()

if __name__ == '__main__':
	main()
