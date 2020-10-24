import rosbag
from rosbag.bag import Bag
import os
import numpy as np
from collections import defaultdict
import cv2
from sensor_msgs.msg import CompressedImage
import time

if __name__ == '__main__':

    # Read environment variable with bag name and open it. Also, create writabel bagfile
    filename = os.environ['BAGFILE']
    bag_read = Bag('/bagfiles/' + filename)
    bag_write = Bag('/bagfiles/amod20-rh3-ex-process-alvarobelmontebaeza.bag', 'w')

    # Read recorded values from the camera image topic
    for topic, msg, t in bag_read.read_messages(topics=['/sora/camera_node/image/compressed']):
        
        try:
            # Extract information
            image_raw = np.frombuffer(msg.data, np.uint8)
            image = cv2.imdecode(image_raw, cv2.IMREAD_COLOR)
            timestamp = str(t.to_sec())

            # Add timestamp to the image
            cv2.putText(image,timestamp,(10,50),cv2.FONT_HERSHEY_PLAIN, 1.5, (0,0,0))

            # Create new ROS CompressedImage msg with new image
            new_image = CompressedImage()
            new_image.header.stamp = msg.header.stamp
            new_image.format = "jpeg"
            new_image.data = np.array(cv2.imencode('.jpg', image)[1]).tostring()

            # Write image in new bag file
            bag_write.write(topic,new_image)
        except:
            pass
    
    bag_write.close()
        



