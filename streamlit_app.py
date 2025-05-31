import streamlit as st
import streamlit as st
import json
from flask import Flask, request

st.title("AI-Powered Dashboard")
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    with open("data.json", "w") as f:
        json.dump(data, f)
    return {"status": "success"}

if __name__ == "__main__":
    app.run(port=8501)
st.write("Waiting for data from n8n...")
