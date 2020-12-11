import cv2
import os


class image_IO:
    def __init__(self, file_name):
        # Initialize the class.
        self.writer_con = 0
        if os.path.exists(file_name):
            self.file_name = file_name
            self.img = cv2.imread(self.file_name)
            self.temp_img = self.img
        else:
            self.file_name = None
            self.img = None

    def reset_img(self):
        self.img = self.temp_img

    def end(self):
        cv2.destroyAllWindows()

    def display(self):
        while(1):
            try:
                cv2.imshow("Display", self.img)
            except:
                break
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cv2.destroyWindow("Display")

    def write_img(self, file_out_name="test.jpg"):
        cv2.imwrite(file_out_name, self.img)
