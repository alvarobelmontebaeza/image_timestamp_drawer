# image_timestamp_drawer

1) Clone the repository using:
git clone https://github.com/alvarobelmontebaeza/image_timestamp_drawer

2) Go to the repo, and put all bagfiles that you want to have access in the bagfiles/ directory (the two bagfiles from the exercise are already included).

3) Compile the ROS package with "dts devel build -f"

4) Run the container with the following command:

docker run -it -e BAGFILE='amod20-rh3-ex-record-alvarobelmontebaeza.bag' -v <path_to_image_timestamp_drawer/bagfiles>:/bagfiles duckietown/image_timestamp_drawer:v2-amd64

where <path_to_image_timestamp_drawer> is the path in your machine to the rosbag_analyzer/bagfiles directory.

5) Now you've generated the processed bagfile in the same directory!