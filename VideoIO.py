import cv2
from ffpyplayer import player
import os


class video_IO:
    def __init__(self, file_name):
        # Initialize the class.
        self.writer_con = 0
        if os.path.exists(file_name):
            self.file_name = file_name
            self.cap_hold = cv2.VideoCapture(self.file_name)
            self.aud_hold = player.MediaPlayer(self.file_name)
        else:
            self.file_name = None
            self.cap_hold = None
            self.aud_hold = None

    def read_frame(self, frame_id=-1):
        # Read the next Frame.
        if frame_id != -1:
            self.cap_hold.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
        if(self.cap_hold.isOpened()):
            self.ret, self.frame = self.cap_hold.read()
            self.aud_frame, self.val = self.aud_hold.get_frame()
            return self.frame, self.aud_frame
        return -1

    def write_config(self, file_name, fps=-1, height=-1, width=-1):
        if fps == -1:
            self.fps = self.get_fps()
        else:
            self.fps = fps
        if height == -1:
            self.height = self.get_height()
        else:
            self.height = height
        if width == -1:
            self.width = self.get_width()
        else:
            self.width = width
        # Setting the write option.
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.out = cv2.VideoWriter(
            file_name, self.fourcc, self.fps, (self.width, self.height))
        self.writer_con = 1
        return 1

    def write_frame(self, frame):
        # Write a frame to the out put.
        if self.writer_con == 0:
            return -1
        self.out.write(frame)
        return 1

    def end(self):
        # End all the capture holds and save the out put file if any.
        self.cap_hold.release()
        self.aud_hold.close_player()
        if self.writer_con == 1:
            self.out.release()
            self.writer_con = 0

    # Additional Functions.
    def preview(self, ws=-1, from_frame=-1):
        # To preview the video in a mini display.
        if ws == -1:
            ws = int(1000 / self.get_fps())
        if from_frame != -1:
            self.cap_hold.set(cv2.CAP_PROP_POS_FRAMES, from_frame)
        while(1):
            frame = self.read_frame()
            try:
                frame = cv2.resize(frame, (640, 480))
                cv2.imshow("Mini-Preview", frame)
            except:
                break
            if cv2.waitKey(ws) & 0xFF == ord('q'):
                break
        cv2.destroyWindow('Mini-Preview')

    def get_height(self):
        return int(self.cap_hold.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def get_width(self):
        return int(self.cap_hold.get(cv2.CAP_PROP_FRAME_WIDTH))

    def get_fps(self):
        return int(self.cap_hold.get(cv2.CAP_PROP_FPS))

    def get_frame(self):
        return self.cap_hold.get(cv2.CAP_PROP_POS_FRAMES)

    def get_total_frame(self):
        return self.cap_hold.get(cv2.CAP_PROP_FRAME_COUNT)

    def get_time(self):
        return int(self.cap_hold.get(cv2.CAP_PROP_POS_MSEC)/1000)
