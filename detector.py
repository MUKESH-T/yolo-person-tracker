from ultralytics import YOLO


class PersonDetector:
    def __init__(self, model_path="yolov8n.pt", confidence=0.5):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            classes=[0],  # COCO class 0 = person
            conf=self.confidence,
            verbose=False
        )

        return results[0]