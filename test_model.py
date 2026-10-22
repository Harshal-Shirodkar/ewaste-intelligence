
from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

image_path = "images/pcb_sample3.jpg"

results = model.predict(
    source=image_path,
    conf=0.10,
    save=True,
    verbose=True
)

for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0].item())
        confidence = float(box.conf[0].item())
        name = model.names[class_id]

        print(
            f"Component: {name} | "
            f"Confidence: {confidence:.2f}"
        )
