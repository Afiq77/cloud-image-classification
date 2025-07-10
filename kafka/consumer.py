# kafka/consumer.py

import cv2
import numpy as np
from kafka import KafkaConsumer
import tensorflow as tf
import os

KAFKA_TOPIC = "image-stream"
LOG_FILE = "dashboard/predictions.log"

# Load model
model = tf.keras.models.load_model("model/cnn_classifier")
print("✅ Model loaded.")

# Define class names (CIFAR-10)
CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

# Create log file if not exists
os.makedirs("dashboard", exist_ok=True)
if not os.path.exists(LOG_FILE):
    open(LOG_FILE, "w").close()

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    enable_auto_commit=True
)

for msg in consumer:
    image_bytes = msg.value
    image_array = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    resized = cv2.resize(image, (32, 32)) / 255.0
    prediction = model.predict(np.expand_dims(resized, axis=0))
    predicted_class = CLASS_NAMES[np.argmax(prediction)]

    print(f"🧠 Prediction: {predicted_class}")

    # Append prediction to log file for dashboard
    with open(LOG_FILE, "a") as f:
        f.write(predicted_class + "\n")

