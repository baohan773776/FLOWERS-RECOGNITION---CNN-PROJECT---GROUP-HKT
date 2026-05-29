import cv2
import numpy as np
from keras.utils import img_to_array
from tensorflow.keras.models import load_model

MODEL_PATH = "flowersrecog.keras"   
IMG_WIDTH, IMG_HEIGHT = 128, 128


CLASS_LABELS = {
    0: "Daisy",
    1: "Dandelion",
    2: "Rose",
    3: "Sunflower",
    4: "Tulip"
}

model = load_model(MODEL_PATH)
print("Đã load model thành công!")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Không mở được webcam!")
    exit()

print("Đang chạy... Bấm 'q' để thoát.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    img_resized = cv2.resize(frame, (IMG_WIDTH, IMG_HEIGHT))
    img_array = img_to_array(img_resized)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype("float32") / 255.0

    pred_probs = model.predict(img_array, verbose=0)
    pred = np.argmax(pred_probs, axis=1)[0]

    flower_name = CLASS_LABELS.get(pred, "Unknown")
    confidence = pred_probs[0][pred] * 100

    if confidence < 80:
        display_text = f"Chua xac dinh duoc"
        color = (0, 165, 255) 
    else:
        display_text = f"{flower_name}: {confidence:.1f}%"
        color = (0, 255, 0)   

    cv2.rectangle(frame, (10, 15), (550, 65), (0, 0, 0), -1)
    cv2.putText(frame, display_text, (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2, cv2.LINE_AA)

    cv2.imshow("Nhan dien Hoa - Real Time", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Đã thoát.")