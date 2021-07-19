import cv2
import time
import threading
from datetime import datetime

class Camera:
    __lastTime = 0
    fourcc = cv2.cv.CV_FOURCC(*'mp4v')
    DELAY = {
        'seconds':30,
        'minutes':0,
        'hours':0,
        'days':0
    }

    def __init__(self, camera_num, file_name, extension) -> None:
        self.cap = cv2.VideoCapture(camera_num)
        self.file_name = file_name
        self.extension = extension

    def __get_time(self):
        return self.DELAY['seconds'] * 1000 +\
            self.DELAY['minutes'] * (60 * 1000) +\
            self.DELAY['hours'] * (60 * 60 * 1000) +\
            self.DELAY['days'] * (24 * 60 * 60 * 1000)

    def __millis(self):
        return round(time.time() * 1000)

    def start(self):
        self.job = threading.Thread(target=self.__capture)
        self.job.start()

    def __get_file_name(self):
        now = datetime.now().strftime("%d-%m/%Y_%H:%M:%S")
        return self.file_name + now + self.extension

    def __capture(self):
        
        out = cv2.VideoWriter(self.__get_file_name(), self.fourcc, 12.0, (640,480))
        while(1):
            if((self.__millis() - self.__lastTime) >= self.__get_time()): # saving video
                self.__lastTime = self.__millis()
                self.__saving(out)
            else: # recording
                self.__record(out)

    def __record(self, out):
        ret, frame = self.cap.read()
        if ret:
            out.write(frame)

    def __saving(self, out):
        out.release()
        out = cv2.VideoWriter(self.__get_file_name(), self.fourcc, 12.0, (640,480))
