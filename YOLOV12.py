!nvidia-smi
!pip install ultralytics
import ultralytics
ultralytics.checks()
#Dataset@ Roboflow
!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="Pwe5iGc9318O2epDHGxI")
project = rf.workspace("model-cn9k6").project("dark-circles-mj5ij")
version = project.version(1)
dataset = version.download("yolov11")
dataset.location
!yolo task=detect mode=train model=yolo12l.pt data=/content/Dark-Circles-1/data.yaml epochs=100 imgsz=640
