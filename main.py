import cv2

from detector import PersonDetector
from tracker import PersonTracker


def main():

    # Initialize detector and tracker
    detector = PersonDetector(
        model_path="yolov8n.pt",
        confidence=0.5
    )

    tracker = PersonTracker()

    # Open webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:

        # Read frame
        success, frame = cap.read()

        if not success:
            print("Error: Could not read frame.")
            break

        # YOLO detection + tracking
        result = detector.detect(frame)

        # Process tracking IDs
        current_ids = tracker.process(result)

        # Draw YOLO results
        annotated_frame = result.plot()

        # Current people visible
        current_count = len(current_ids)

        # Total unique people detected
        total_count = tracker.get_total_count()

        # Display information
        cv2.putText(
            annotated_frame,
            f"People Visible: {current_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            annotated_frame,
            f"Unique People: {total_count}",
            (20, 75),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )

        # Display frame
        cv2.imshow(
            "YOLO Person Detection & Tracking",
            annotated_frame
        )

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()