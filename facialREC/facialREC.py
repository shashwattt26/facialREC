import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
from PIL import Image
import os

# Initialize video capture
video_capture = cv2.VideoCapture(0)
print("Opening webcam...")



# Helper function for safe encoding
def get_face_encoding(image_path, name):
    try:
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        print(f"Loaded and encoded: {name}")
        return encoding
    except Exception as e:
        print(f"Failed to encode {name} ({image_path}): {e}")
        return None

input_dir = "faces"
output_dir = "faces_fixed"
os.makedirs(output_dir, exist_ok=True)

for filename in os.listdir(input_dir):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Read image with OpenCV (ensures 8-bit format)
        img = cv2.imread(input_path)

        if img is None:
            print(f"❌ Cannot read {filename} — possibly corrupted or unsupported format.")
            continue

        # Save the image back in standard format
        cv2.imwrite(output_path, img)
        print(f"✅ Converted: {filename} -> {output_path}")

# Load known faces
known_faces = {
    "anushka": "faces_fixed/anushka.jpg",
    "shashwat": "faces_fixed/shashwat.jpg",
    "nikita": "faces_fixed/nikita.jpg",
    "Krishna": "faces_fixed/krishna.jpg"
}

known_face_encodings = []
known_face_names = []

for name, path in known_faces.items():
    encoding = get_face_encoding(path, name)
    if encoding is not None:
        known_face_encodings.append(encoding)
        known_face_names.append(name)

if not known_face_encodings:
    print("No known faces loaded. Exiting...")
    exit()

# Students to mark
students = known_face_names.copy()

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")
csv_filename = f"{current_date}.csv"
file_exists = os.path.isfile(csv_filename)

# Open CSV in append mode
with open(csv_filename, "a", newline="") as f:
    lnwriter = csv.writer(f)

    # Write header only once
    if not file_exists:
        lnwriter.writerow(["Name", "Time"])

    print("Starting recognition loop... Press 'q' to quit.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame.")
            break

        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        print(f"Detected {len(face_encodings)} face(s) in frame")

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                print(f"Match found: {name}")

                if name in students:
                    students.remove(name)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])
                    print(f"Marked attendance for {name} at {current_time}")

                # Display name on frame
                cv2.putText(frame, f"{name} Present", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Show video frame
        cv2.imshow("Attendance", frame)

        # Exit on 'q'
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exiting recognition loop.")
            break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
print("Webcam and windows closed.")

