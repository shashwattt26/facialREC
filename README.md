
# 🎥 Face Recognition Attendance System

A real-time facial recognition attendance system built using Python, OpenCV, and the `face_recognition` library. This project captures video from a webcam, identifies known faces from a dataset, and logs their attendance with a timestamp in a daily CSV file.

---

## 🚀 Features

- 🔍 Real-time face detection and recognition using webcam
- 🧠 Pre-encoded known face database from images
- 📅 Daily CSV log for attendance records
- 🖼️ Automatic image format normalization
- ✅ One-time attendance marking per session
- 🧾 Lightweight, dependency-minimal, and easy to deploy

---

## 📂 Project Structure

```
.
├── facialREC.py         # Main script
├── faces/               # Input images of known people
├── faces_fixed/         # Normalized image outputs
├── YYYY-MM-DD.csv       # Output file with attendance records
```

---

## 🧰 Requirements

- Python 3.7+
- OpenCV (`cv2`)
- face_recognition (`dlib`-based)
- NumPy
- Pillow (PIL)
- Webcam device

> Install dependencies:
```bash
pip install opencv-python face_recognition numpy pillow
```

---

## 🛠️ Setup Instructions

1. **Prepare known face images**:
   - Place `.jpg`, `.jpeg`, or `.png` images in the `faces/` folder.
   - Filenames should be identifiable names (e.g., `shashwat.jpg`, `anushka.jpg`).

2. **Run the script**:
   ```bash
   python facialREC.py
   ```

3. **Marking attendance**:
   - When a face is recognized, it is marked once in the day's CSV file.
   - Press `q` to exit the webcam view.

4. **Check logs**:
   - A new CSV file is generated each day with the format `YYYY-MM-DD.csv`.

---

## 📝 Sample Attendance CSV

```
Name,Time
shashwat,10:15:03
anushka,10:16:42
```

---

## 📌 Notes

- Images are normalized using OpenCV to ensure consistent encoding.
- Recognition accuracy depends on lighting, image quality, and webcam resolution.
- Supports only one attendance record per person per session.

---

## 🧠 Acknowledgements

- [face_recognition](https://github.com/ageitgey/face_recognition) – Simple face recognition library built on top of dlib
- [OpenCV](https://opencv.org/) – Real-time computer vision
- [Python](https://www.python.org/) – Backend scripting

---

## 📸 Screenshot

![sample-screenshot](https://via.placeholder.com/600x300?text=Attendance+UI+Preview)

>

---

## 👤 Author

**Shashwat Rao**
