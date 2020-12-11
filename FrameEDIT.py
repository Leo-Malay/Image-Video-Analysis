# This file takes frame as input and then apply the necessay effects.
import cv2


class frameEDIT:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = 1
        self.brg = (255, 255, 255)
        self.thickness = 2

    def set_frame(self, frame):
        self.frame = frame
        self.temp = frame

    def get_frame(self):
        # Return the edited frme.
        return self.frame

    def save_frame(self):
        # Save frme to Original frame
        self.temp = self.frame

    def discard_frame(self):
        # Get the Original Frame.
        self.frame = self.temp

    def add_text(self, text, x_pos=-1, y_pos=-1):
        if x_pos == -1:
            x_pos = self.width * 0.2
        if y_pos == -1:
            y_pos = self.height * 0.2
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.frame = cv2.putText(self.frame, text, (int(x_pos), int(y_pos)),
                                 self.font, self.size, self.brg, self.thickness, cv2.LINE_AA)

    def add_line(self, x1, y1, x2, y2):
        self.frame = cv2.line(self.frame, (x1, y1),
                              (x2, y2), self.brg, self.thickness)

    def add_rectangle(self, x1, y1, x2, y2):
        self.frame = cv2.rectangle(
            self.frame, (x1, y1), (x2, y2), self.brg, self.thickness)

    def add_circle(self, x, y):
        self.frame = cv2.circle(
            self.frame, (x, y), self.radius, self.brg, self.thickness)
    # Additional Function

    def set_size(self, size):
        self.size = size

    def set_thickness(self, thickness):
        self.thickness = int(thickness)

    def set_rgb(self, r, g, b):
        self.brg = (b, r, g)

    def set_rad(self, radius):
        self.radius = radius
