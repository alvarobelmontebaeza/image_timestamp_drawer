import rosbag
from rosbag.bag import Bag
import os
import numpy as np
from collections import defaultdict
import cv2
from sensor_msgs.msg import CompressedImage

if __name__ == '__main__':

    # Read environment variable with bag name and open it. Also, create writabel bagfile
    filename = os.environ['BAGFILE']
    bag_read = Bag('/bagfiles/' + filename)
    bag_write = Bag('/bagfiles/amod20-rh3-ex-process-alvarobelmontebaeza.bag', 'w')

    # Read recorded values from the camera image topic
    for topic, msg, t in bag_read.read_messages(topics=['/sora/camera_node/image/compressed']):
        # Extract information
        image = np.fromstring(msg, np.uint8)
        timestamp = t.to_sec()

        # Add timestamp to the image
        cv2.putText(image,t,(10,100),cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,0))

        # Create new ROS CompressedImage msg with new image
        new_image = CompressedImage()
        new_image.header.stamp = t
        new_image.format = "jpeg"
        new_image.data = np.array(cv2.imencode('.jpg', image)[1]).tostring()

        # Write image in new bag file
        bag_write.write(topic,new_image)
        



