import cv2
from application.vision_detection_service import VisionDetectionService


def main():
    video_capture = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        _, frame = video_capture.read()

        # Detect the skin with the vision service
        vision_service = VisionDetectionService()
        detected_skin = vision_service.analyze_frame_for_skin(frame)

        # Display the resulting frame
        cv2.imshow('frame', detected_skin)
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
