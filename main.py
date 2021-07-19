from camera import Camera

cam1 = Camera(
    camera_num=0,
    f_name_prefix='vid1', 
    extension='avi', 
    fps=22, 
    size=(1600,1200),
    device_path='/media/pi/Seagate Expansion Drive/video_test'
)

cam2 = Camera(
    camera_num=1,
    f_name_prefix='vid2', 
    extension='avi', 
    fps=22, 
    size=(1600,1200),
    device_path='/media/pi/Seagate Expansion Drive/video_test'
)

cam1.start()
cam2.start()