# kafka/producer.py

import os
import cv2
import time
from kafka import KafkaProducer

IMAGE_DIR = "test_images"
KAFKA_TOPIC = "image-stream"

producer = KafkaProducer(bootstrap_servers='localhost:9092')

for filename in os.listdir(IMAGE_DIR):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        path = os.path.join(IMAGE_DIR, filename)
        image = cv2.imread(path)
        _, buffer = cv2.imencode('.jpg', image)
        producer.send(KAFKA_TOPIC, buffer.tobytes())
        print(f"📤 Sent: {filename}")
        time.sleep(1)  # Simulate stream delay
