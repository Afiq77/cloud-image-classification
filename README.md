# Cloud Image Classification with GCP & Kafka

A scalable image classification pipeline that processes wildlife image streams using a custom-trained CNN and real-time messaging via Kafka. The model is deployed on Google Cloud AI Platform, with predictions logged to a PostgreSQL database and visualized using Streamlit.

---

## Features

- Train and evaluate a CNN model (TensorFlow) for multi-class image classification
- Simulate real-time image stream using Kafka producers/consumers
- Deploy the trained model to Google Cloud AI Platform
- Log classification results to PostgreSQL
- Visualize prediction metrics and class distribution in Streamlit dashboard

---

## Tech Stack

- Python
- TensorFlow / Keras
- Apache Kafka
- Google Cloud Platform (Vertex AI or AI Platform)
- PostgreSQL
- Streamlit

---

## Project Structure

    cloud-image-classification/
    │
    ├── training/ # CNN model training code
    ├── kafka/ # Kafka producer/consumer scripts
    ├── cloud/ # GCP model deployment scripts (placeholder)
    ├── dashboard/ # Streamlit UI
    ├── db/ # PostgreSQL logging setup
    ├── test_images/ # Sample wildlife images
    ├── requirements.txt
    ├── README.md
    └── .gitignore


## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/cloud-image-classification.git
    cd cloud-image-classification
    python -m venv venv
    source venv/bin/activate   # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    # Start Zookeeper and Kafka broker
    bin/zookeeper-server-start.sh config/zookeeper.properties
    bin/kafka-server-start.sh config/server.properties
    python kafka/producer.py
    python kafka/consumer.py
    streamlit run dashboard/app.py

## Future Improvements

- Use cloud storage for image ingestion (e.g., GCS bucket)
- Connect to live camera traps or drone feed
- Integrate email/SMS alerts for critical species
- Add Kafka Stream or Spark pipeline for larger scale
- Automate retraining via Vertex AI Pipelines

# License
  This project is licensed under the MIT License.



