import rclpy
from std_msgs.msg import String
from rclpy.node import Node
from std_srvs.srv import Trigger

FALLBACK_MESSAGE = "I lost my pants"

class TopicsNode(Node):
  def __init__(self):
    super(TopicsNode, self).__init__('drug')

    # Interface setup
    self.declare_parameter("default_string", FALLBACK_MESSAGE)
    self.declare_parameter("service_name", "/trigger_service")

    # Runtime setup
    self.default_response = self.get_parameter("default_string").get_parameter_value().string_value()
    self.provided_service_name = self.get_parameter("service_name").get_parameter_value().string_value()
    self.called_service = self.create_client(Trigger, "spgc/trigger")
    self.provided_service = self.create_service(Trigger, self.service_name, self.proxy_callback)
    #self.timer = self.create_timer(0.5, self.probe_callback)
			
	def proxy_callback(self, request, response):
		response.success = True
		response.message = self.default_response

    if not self.called_service.wait_for_service(timeout_sec=1.0):
      result = self.called_service.call_async(Trigger.Request())
      rclpy.spin_until_future_complete(self, result)
      response.message = result.result().message

    return response

	#def probe_callback(self): pass

def main():
	rclpy.init()
	node = TopicsNode()
	rclpy.spin(node)
	rclpy.destroy()
	rclpy.shutdown()

if __name__ == '__main__':
	main()