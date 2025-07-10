# dashboard/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

LOG_FILE = "dashboard/predictions.log"

st.set_page_config(page_title="📊 Prediction Dashboard", layout="wide")
st.title("📸 Image Classification Dashboard")

# Load logs
if not LOG_FILE or not st.file_uploader:
    st.info("Waiting for predictions...")
else:
    if not open(LOG_FILE).read().strip():
        st.warning("Log file is empty.")
    else:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()

        classes = [line.strip() for line in lines if line.strip()]
        count = Counter(classes)

        df = pd.DataFrame.from_dict(count, orient='index', columns=['Count'])
        df.index.name = 'Class'
        df = df.sort_values(by='Count', ascending=False)

        st.bar_chart(df)

        st.markdown("---")
        st.write("🧾 Latest Predictions")
        for c in classes[-10:]:
            st.write(f"✅ {c}")
