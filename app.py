import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page Layout
st.set_page_config(page_title="AI Cyber-Guardian", page_icon="🛡️", layout="wide")

# Sidebar: Setup Center
st.sidebar.title("🔐 Setup Center")
gemini_key = st.sidebar.text_input("Google Gemini API Key", type="password")

st.title("🛡️ AI Cyber-Guardian v2.0")
st.markdown("### Detect Text Scams & Deepfake Photos")

# Tabs for Features
tab1, tab2 = st.tabs(["💬 Text Scam Scanner", "🖼️ Image/Deepfake Detector"])

# --- TAB 1: TEXT SCAM DETECTION ---
with tab1:
    st.subheader("Message ya Link Scan Karein")
    user_text = st.text_area("Yahan message paste karein:", placeholder="Example: You won a lottery!")
    if st.button("Scan Message"):
        if not gemini_key:
            st.error("Pehle Sidebar mein apni API Key dalein!")
        else:
            try:
                genai.configure(api_key=gemini_key)
                # Updated Model Name here
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"Analyze this text for scams or phishing. Give a risk score (0-100%) and explain why: {user_text}"
                response = model.generate_content(prompt)
                st.warning(f"**AI Analysis Result:**\n\n{response.text}")
            except Exception as e:
                st.error(f"Error: {e}")

# --- TAB 2: IMAGE/DEEPFAKE DETECTION ---
with tab2:
    st.subheader("Photo Scan Karein")
    uploaded_file = st.file_uploader("Deepfake ya AI photo upload karein", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Check for Deepfake"):
            if not gemini_key:
                st.error("Pehle Sidebar mein apni API Key dalein!")
            else:
                try:
                    genai.configure(api_key=gemini_key)
                    # Updated Model Name here
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(["Check if this image is AI generated or a deepfake. Look for anomalies. Explain why.", image])
                    st.info(f"**AI Assessment:**\n\n{response.text}")
                except Exception as e:
                    st.error(f"Error: {e}")
