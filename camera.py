import cv2
import time
import threading
from datetime import datetime

class Camera:
    __lastTime = 0
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    DELAY = {
        'seconds':0,
        'minutes':0,
        'hours':1,
        'days':0
    }
    file_name = ''
    out = None

    def __init__(self, camera_num, f_name_prefijo, extension, fps, size, device_path) -> None:
        self.cap = cv2.VideoCapture(camera_num)
        self.f_name = f_name_prefijo
        self.extension = extension
        self.fps = fps
        self.size = size
        self.device_path = device_path

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
        now = datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
        return self.device_path + '/' + self.f_name + now + '.' + self.extension

    def __capture(self):
        self.file_name = self.__get_file_name()
        self.out = cv2.VideoWriter(self.file_name, self.fourcc, self.fps, self.size)
        self.__lastTime = self.__millis()
        while(1):
            if((self.__millis() - self.__lastTime) >= self.__get_time()): # saving video
                self.__lastTime = self.__millis()
                self.__saving()
            else: # recording
                self.__record()

    def __record(self):
        ret, frame = self.cap.read()
        if ret:
            self.out.write(frame)

    def __saving(self):
        self.out.release()
        self.out = None
        print('save: {}'.format(self.file_name))
        self.file_name = self.__get_file_name()
        self.out = cv2.VideoWriter(self.file_name, self.fourcc, self.fps, self.size)
