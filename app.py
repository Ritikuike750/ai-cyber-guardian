import streamlit as st
import google.generativeai as genai
from PIL import Image
import requests

# Page Layout
st.set_page_config(page_title="AI Cyber-Guardian", page_icon="🛡️", layout="wide")

# Sidebar: Yahan aap apni API keys dalenge (Point 6 - Free & Secure)
st.sidebar.title("🔐 Setup Center")
st.sidebar.markdown("Apni API keys yahan paste karein:")
gemini_key = st.sidebar.text_input("Google Gemini API Key", type="password")
hf_token = st.sidebar.text_input("Hugging Face Token (Optional)", type="password")

st.title("🛡️ AI Cyber-Guardian v2.0")
st.markdown("### Detect Text Scams & Deepfake Photos")

# Tabs for Features
tab1, tab2 = st.tabs(["💬 Text Scam Scanner", "🖼️ Image/Deepfake Detector"])

# --- TAB 1: TEXT SCAM DETECTION ---
with tab1:
    st.subheader("Message ya Link Scan Karein")
    user_text = st.text_area("Yahan message ya email paste karein:", placeholder="Example: You won $10,000! Click here...")
    if st.button("Scan Message"):
        if not gemini_key:
            st.error("Pehle Sidebar mein apni Google API Key dalein!")
        else:
            try:
                genai.configure(api_key=gemini_key)
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"Analyze this text for scams, phishing, or fraud. Give a risk score (0-100%) and explain why: {user_text}"
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
                st.error("Pehle Sidebar mein apni Google API Key dalein!")
            else:
                try:
                    genai.configure(api_key=gemini_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(["Check if this image is AI generated or a deepfake. Look for lighting, skin, and edges. Explain details.", image])
                    st.info(f"**AI Assessment:**\n\n{response.text}")
                except Exception as e:
                    st.error(f"Error: {e}")

st.sidebar.markdown("---")
st.sidebar.info("Unique Point: Yeh tool Text aur Image dono ko ek saath scan karta hai.")
