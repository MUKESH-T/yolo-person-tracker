# Real-Time Person Detection, Tracking & Counting

A real-time computer vision application that uses **YOLO**, **ByteTrack**, and **OpenCV** to detect, track, and count people from a live webcam feed.

## 🚀 Features

- Real-time person detection using YOLO
- Person tracking using ByteTrack
- Unique ID assignment for detected people
- Current visible person count
- Unique people count during the session
- Bounding boxes and tracking IDs
- Real-time webcam processing
- Confidence threshold configuration
- FPS-friendly lightweight YOLO model

## 🧠 System Architecture

```text
Webcam
   ↓
OpenCV Frame Capture
   ↓
YOLO Object Detection
   ↓
Filter Person Class
   ↓
ByteTrack Object Tracking
   ↓
Unique Person IDs
   ↓
Person Counting
   ↓
OpenCV Visualization
```

## 🛠️ Technologies Used

- **Python**
- **YOLO**
- **Ultralytics**
- **ByteTrack**
- **OpenCV**

## 📁 Project Structure

```text
yolo-person-tracker/
│
├── main.py
├── detector.py
├── tracker.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── screenshots/
    └── demo.png
```

## ⚙️ How It Works

### 1. Frame Capture

OpenCV captures frames continuously from the webcam.

### 2. Object Detection

YOLO processes each frame and identifies objects.

The project filters the detections to focus only on the **person** class.

### 3. Object Tracking

ByteTrack maintains the identity of detected people across consecutive frames.

For example:

```text
Person → ID 1
Person → ID 2
Person → ID 3
```

This allows the system to distinguish between different people while they remain in the camera view.

### 4. Counting

The application displays:

- **People Visible** — number of people currently detected
- **Unique People** — number of unique tracking IDs encountered during the session

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/yolo-person-tracker.git
```

Navigate to the project:

```bash
cd yolo-person-tracker
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
python main.py
```

The first run downloads the required pretrained YOLO model automatically.

Press:

```text
Q
```

to exit the application.

## 📸 Demo

Add your project screenshot here:

```text
screenshots/demo.png
```

## 🔍 Example Output

The application displays detected people with bounding boxes and tracking information.

```text
People Visible: 2
Unique People: 4
```

## 🎯 Project Objective

The objective of this project was to gain hands-on experience with a real-time computer vision pipeline involving:

- Object detection
- Object tracking
- Video processing
- Real-time inference
- Post-processing
- Object counting

## 🔮 Future Improvements

- Line-crossing based entry and exit counting
- People entry/exit analytics
- Custom YOLO model fine-tuning
- Detection history and statistics
- GPU acceleration
- ONNX model export
- TensorRT optimization
- Edge-device deployment

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- YOLO-based object detection
- ByteTrack object tracking
- OpenCV video processing
- Real-time inference pipelines
- Tracking IDs
- Detection confidence thresholds
- Computer vision system architecture

## 👨‍💻 Author

**Mukesh T**

BCA Graduate | Software Developer | AI/ML & Computer Vision Enthusiast

GitHub: https://github.com/MUKESH-T