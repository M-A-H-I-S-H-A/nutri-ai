import streamlit as st
from PIL import Image

def image_analysis():

    st.subheader("Vitamin Deficiency Image Analysis")

    image_type = st.selectbox(
        "Select image type",
        ["Tongue", "Nails", "Skin", "Eyes"]
    )

    uploaded_file = st.file_uploader(
        "Upload image",
        type=["jpg","jpeg","png"]
    )

    if uploaded_file:

        img = Image.open(uploaded_file)

        st.image(img, caption="Uploaded Image")

        # Simple rule-based detection

        if image_type == "Tongue":
            result = "Pale tongue may indicate Iron or B12 deficiency."

        elif image_type == "Nails":
            result = "Brittle nails may indicate Iron deficiency."

        elif image_type == "Skin":
            result = "Pale skin may indicate Iron deficiency."

        elif image_type == "Eyes":
            result = "Dry eyes may indicate Vitamin A deficiency."

        st.success(result)