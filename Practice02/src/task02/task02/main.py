import rclpy
from std_msgs.msg import String
from rclpy.node import Node

FALLBACK_MESSAGE = "Hello, ROS2!"

class TopicsNode(Node):
	def __init__(self):
			super(TopicsNode, self).__init__('amogus')
			
			# Interface setup
			self.declare_parameter("text", FALLBACK_MESSAGE)
			self.declare_parameter("topic_name", "/sgpc/receiver")

			# Runtime setup
			self.msg = self.get_parameter("text").get_parameter_value().string_value
			self.topic = self.get_parameter("topic_name").get_parameter_value().string_value
			self.publisher = self.create_publisher(String, self.topic, 10)
			self.timer = self.create_timer(0.5, self.timer_callback)
			
	def timer_callback(self):
			# Send
			m = String()
			m.data = self.msg
			self.publisher.publish(m)

def main():
	rclpy.init()
	node = TopicsNode()
	rclpy.spin(node)
	rclpy.destroy()
	rclpy.shutdown()

if __name__ == '__main__':
	main()
