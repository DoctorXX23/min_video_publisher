import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge

class VideoPublisher(Node):
    def __init__(self):
        super().__init__('video_publisher')
        self.publisher = self.create_publisher(Image, '/image', 10)
        self.timer = self.create_timer(1.0/30.0, self.timer_callback)
        self.bridge = CvBridge()
        #self.cap = cv2.VideoCapture('/media/pcraichl/02F7-159F/DCIM/100GOPRO/GX010483.MP4')#center left right
        self.cap = cv2.VideoCapture('/home/pcraichl/Downloads/continental_hike.mp4')#center left right
        #self.cap = cv2.VideoCapture('/home/pcraichl/neural_nets/test_videos/GX010524.MP4')

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            ros_image = self.bridge.cv2_to_imgmsg(frame, "bgr8")
            self.publisher.publish(ros_image)
        else:
            self.cap.release()

def main(args=None):
    rclpy.init(args=args)
    node = VideoPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.cap.release()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
