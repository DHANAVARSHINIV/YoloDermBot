# YoloDermBot
Real-time detection with voice interaction
#  YOLOv12-based Dark Circle Detection Video Chatbot

This project is an AI-powered video chatbot that:
- Uses a YOLOv12-trained model to detect **dark circles** via webcam
- Gives **real-time spoken feedback** using `pyttsx3`
- Saves the final prediction + audio into a video

##  Features

- Real-time webcam feed with bounding box detection
- Text-to-speech (TTS) response while processing
- 10-second automated run and exit
- Saves a final `.mp4` with both detection and voice
- Custom-trained on Roboflow using YOLOv12

---
# 👁️ Dark Circle Detection Video Chatbot

This project uses a YOLOv12-based deep learning model to detect dark circles under the eyes via webcam and responds with real-time voice suggestions using TTS.

## 📸 Sample Detection Output

![Output Image](https://drive.google.com/uc?export=view&id=12ZaSS_QXvs_K3E6lZnqkVZT51gm3xjJ9)

## 🎥 Demo Video

[![Watch the demo](https://img.shields.io/badge/Watch-Demo-blue?logo=google-drive)](https://drive.google.com/file/d/1iqlSQhyEGtmQJcTyb5G1EAytbYlMFG_M/view?usp=sharing)



##  Requirements

Install required packages:

```bash
pip install ultralytics pyttsx3 opencv-python
