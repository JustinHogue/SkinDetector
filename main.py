import cv2
from application.vision_detection_service import VisionDetectionService


def main():
    # Image to be loaded
    frame = cv2.imread("images\\image_01.jpg")

    # Detect the skin with the vision service
    vision_service = VisionDetectionService()
    detected_skin = vision_service.analyze_frame_for_skin(frame)

    # Display the resulting frame
    cv2.imshow('frame', detected_skin)
    cv2.waitKey(0)

    # Delete the window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
