import cv2
import numpy as np

class VisionDetectionService:
    def __init__(self) -> None:
        """
        Constructor for class VisionDetectionService
        """
        pass

    def analyze_frame_hsv_for_skin(self, frame: np.ndarray) -> np.ndarray:
        """
        Analyzes a frame in order to detect the human skin
        :param frame: The frame to analyze
        :return: The new frame with detected skin only
        """
        # Adding a border to detect the skin on the edge
        borderType = cv2.BORDER_CONSTANT
        top = int(0.006 * frame.shape[0])  # shape[0] = rows
        bottom = top
        left = int(0.002 * frame.shape[1])  # shape[1] = cols
        right = left
        border_color = (0, 0, 0)
        img = cv2.copyMakeBorder(frame, top, bottom, left, right, borderType, None, border_color)

        # We transfer into HSV
        frame_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        # We filter the image after smoothing it
        blurred_frame = cv2.GaussianBlur(frame_hsv, (3, 3), 0)
        lighter_skin = cv2.inRange(blurred_frame, (115, 10, 50), (170, 70, 255))
        darker_skin = cv2.inRange(blurred_frame, (0, 40, 100), (17, 120, 255))
        redder_skin = cv2.inRange(blurred_frame, (170, 25, 160), (179, 50, 255))
        skin = cv2.bitwise_or(lighter_skin, darker_skin)
        skin = cv2.bitwise_or(skin, redder_skin)
        
        # We treat the holes in the filtered frame
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel)

        return opening

    def analyze_frame_rgb_for_skin(self, frame: np.ndarray) -> np.ndarray:
        """
        Analyzes a frame in order to detect the human skin
        :param frame: The frame to analyze
        :return: The new frame with detected skin only
        """
        # Adding a border to detect the skin on the edge
        borderType = cv2.BORDER_CONSTANT
        top = int(0.006 * frame.shape[0])  # shape[0] = rows
        bottom = top
        left = int(0.002 * frame.shape[1])  # shape[1] = cols
        right = left
        border_color = (0, 0, 0)
        img = cv2.copyMakeBorder(frame, top, bottom, left, right, borderType, None, border_color)
        
        # We only keep the pixels that respect the following conditions:
        # R > 95 and G > 40 and B > 20 and R > G and R > B and | R - G | > 15 and Y > 80 where Y = 0.299*R + 0.287*G + 0.11*B
        rows,cols,_ = img.shape
        for i in range(rows):
            for j in range(cols):
                k = img[i,j]
                B = k[0]
                G = k[1]
                R = k[2]
                Y = 0.299*R + 0.287*G + 0.11*B
                if (R > G and R > B and abs(R - G) > 15 and Y > 80 and max(k) - min(k) > 15):
                    img[i,j] = k
                else:
                    img[i,j] = [0,0,0]

        # We filter the image after smoothing it
        blurred_frame = cv2.GaussianBlur(img, (3, 3), 0)
        skin = cv2.inRange(blurred_frame, (20, 40, 95), (255, 255, 255))
        
        # We treat the holes in the filtered frame
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel)

        return opening

    def analyze_frame_ycrcb_for_skin(self, frame: np.ndarray) -> np.ndarray:
        # Adding a border to detect the skin on the edge
        borderType = cv2.BORDER_CONSTANT
        top = int(0.006 * frame.shape[0])  # shape[0] = rows
        bottom = top
        left = int(0.002 * frame.shape[1])  # shape[1] = cols
        right = left
        border_color = (0, 0, 0)
        frame = cv2.copyMakeBorder(frame, top, bottom, left, right, borderType, None, border_color)
        
        # We transfer into YCRCB
        frame_ycrcb = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
        
        # We filter the image after smoothing it
        blurred_frame = cv2.GaussianBlur(frame_ycrcb, (3, 3), 0)
        skin = cv2.inRange(blurred_frame, (88, 137, 85), (243, 180, 128))

        # We treat the holes in the filtered frame
        kernel = np.ones((3, 3), np.uint8)
        opening = cv2.morphologyEx(skin, cv2.MORPH_OPEN, kernel)
        
        return opening

    def analyze_frame_for_skin(self, frame: np.ndarray) -> np.ndarray:
        skin_on_hsv_frame = self.analyze_frame_hsv_for_skin(frame)
        skin_on_ycrcb_frame = self.analyze_frame_ycrcb_for_skin(frame)
        skin_on_rgb_frame = self.analyze_frame_rgb_for_skin(frame)
        global_skin_mask = cv2.bitwise_and(skin_on_hsv_frame, skin_on_ycrcb_frame)
        global_skin_mask = cv2.bitwise_and(global_skin_mask, skin_on_rgb_frame)
        return skin_on_rgb_frame
        