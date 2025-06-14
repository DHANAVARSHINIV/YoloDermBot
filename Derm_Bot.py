from ultralytics import YOLO
import cv2
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty("rate", 160)

# Load your YOLO model
model = YOLO(r"D:\Research\Promotion\Model_Output\best.pt")  # Replace with your dark circle model

# Define class name you trained for (e.g., "dark_circle")
target_class = "dark_circle"
class_names = ["dark_circle"]  # Add more if you have

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

speak("Video chatbot started. Looking for dark circles...")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run detection
    results = model(frame, save=False, verbose=False)[0]

    detections = results.boxes
    dark_circle_count = 0

    for i, box in enumerate(detections):
        cls_id = int(box.cls.item())
        class_name = class_names[cls_id]
        if class_name == target_class:
            dark_circle_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            cv2.putText(frame, class_name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Respond based on detection
    if dark_circle_count == 0:
        speak("No eye Detected! No dark circles detected. Keep up the good rest!")
    else:
        speak(f"I see {dark_circle_count} sign(s) of dark circles. You may need rest.")
        speak("Try sleeping at least 7 hours, stay hydrated, and use an under-eye cream with vitamin C.")

    # Show webcam feed
    cv2.imshow("Dark Circle Chatbot", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
cap.release()
cv2.destroyAllWindows()
speak("Goodbye! Take care.")
