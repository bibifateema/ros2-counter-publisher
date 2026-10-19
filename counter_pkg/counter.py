import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Counter(Node):
    def __init__(self):
        super().__init__('counter')
        self.count = 0
        self.pub = self.create_publisher(Int32, 'counter', 10)
        self.timer = self.create_timer(1.0, self.publish_number)

    def publish_number(self):
        self.count += 1
        msg = Int32()
        msg.data = self.count
        self.pub.publish(msg)
        print(self.count)

def main():
    rclpy.init()
    node = Counter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
