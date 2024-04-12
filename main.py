from ultralytics import YOLO

model = YOLO(model="yolov8n.pt")

results = model.train(data = "datasetcustom.yaml",
                      epochs = 100,
                      batch = 8,
                      imgsz = 640,
                      optimizer = 'Adam')
