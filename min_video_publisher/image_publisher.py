import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge
import os

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher = self.create_publisher(Image, '/image', 10)
        self.timer = self.create_timer(1.0/5.0, self.timer_callback)
        self.bridge = CvBridge()
        #self.image_directory = '/home/uarsnuc6/ai/trail_dataset_raw/014/014/videos/07/videos/sc/26804209.frames'  # Update this path
        #self.image_directory = '/home/uarsnuc6/ai/trail_dataset_raw/012/012/videos/sc/26802500.frames'  # Update this path
        self.image_directory = '/media/uarsnuc6/2903-994D/dataset_lateral/center'  # Update this path
        self.images = os.listdir(self.image_directory)
        self.images.sort()  # Sort the files if needed
        self.current_image_index = 0

    def timer_callback(self):
        if self.current_image_index < len(self.images):
            image_path = os.path.join(self.image_directory, self.images[self.current_image_index])
            frame = cv2.imread(image_path)
            if frame is not None:
                ros_image = self.bridge.cv2_to_imgmsg(frame, "bgr8")
                self.publisher.publish(ros_image)
            self.current_image_index += 1
        else:
            self.current_image_index = 0  # Restart or stop based on your need

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
