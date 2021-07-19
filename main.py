from camera import Camera

cam = Camera(
    camera_num=0,
    f_name='vid1', 
    extension='avi', 
    fps=12, 
    size=(640,480),
    device_path='/media/pi/Seagate Expansion Drive/video_test'
)

cam.start()