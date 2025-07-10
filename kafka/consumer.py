# kafka/consumer.py

import cv2
import numpy as np
from kafka import KafkaConsumer
import tensorflow as tf
import io

KAFKA_TOPIC = "image-stream"

# Load model
model = tf.keras.models.load_model("model/cnn_classifier")
print("✅ Model loaded.")

# Define class names (CIFAR-10)
CLASS_NAMES = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

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
