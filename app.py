import streamlit as st
from PIL import Image
import numpy as np
import os

from stego_encoder import encode_lsb
from decode_lsb import decode_lsb
from blip_reader import get_caption

st.set_page_config(page_title="StegoVision", page_icon="🔍")

st.title("🧠 StegoVision: Hide & Reveal Messages in Images")

st.markdown("Upload an image, hide a secret message in it, and see what AI thinks of it!")

# Upload section
uploaded_file = st.file_uploader("📤 Upload an Image", type=["png", "jpg", "jpeg"])

message = st.text_input("✏️ Enter a Secret Message to Hide")

col1, col2 = st.columns(2)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    image_path = "original.png"
    image.save(image_path)

    if col1.button("🔐 Hide Message"):
        try:
            output_path = "stego_image.png"
            encode_lsb(image_path, message, output_path)
            st.success("✅ Message hidden successfully!")

            st.image(output_path, caption="Stego Image (with hidden message)", use_column_width=True)

            # Optional: Get BLIP caption
            if st.checkbox("🧠 Run BLIP to Caption Image"):
                caption = get_caption(output_path)
                st.info(f"BLIP thinks this image is: **{caption}**")
        except Exception as e:
            st.error(f"❌ Error: {e}")

if col2.button("🔓 Decode Message from Image"):
    try:
        decoded = decode_lsb("stego_image.png")
        st.success(f"🔓 Hidden Message: {decoded}")
    except Exception as e:
        st.error(f"❌ Error decoding message: {e}")
