

from dotenv import load_dotenv
import os
import base64
import streamlit as st
from langchain.chat_models import init_chat_model

# Load API key from .env
load_dotenv()
st.set_page_config(page_title="Barai PictoChat", page_icon="📸", layout="centered")
st.title("📸")
st.title("PictoChat - Ask About Your Image")
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;} /* Hide hamburger menu */
    header {visibility: hidden;}    /* Hide Streamlit header */
    footer {visibility: hidden;}    /* Hide default footer */

    /* Custom sticky footer */
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: gray;
        border-top: 1px solid #ddd;
        z-index: 9999;
    }
    </style>

    <div class="custom-footer">
        © 2025 Barai – 📸 Built by <b>M-Ashraf-Barai</b>
    </div>
    """,
    unsafe_allow_html=True
)

api_key = os.getenv("GROQ_API_KEY")

# Function to validate API key
def validate_api_key(key: str) -> bool:
    try:
        test_llm = init_chat_model(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            model_provider="groq",
            api_key=key,
        )
        # Try a tiny dummy request to ensure the key is valid
        test_llm.invoke([{"role": "user", "content": [{"type": "text", "text": "ping"}]}])
        return True
    except Exception:
        return False

# Validate .env key, else ask user for input
if not api_key or not validate_api_key(api_key):
    st.sidebar.header("🔑 API Key Settings")
    api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
    if not api_key or not validate_api_key(api_key):
        st.sidebar.error("⚠️ Please provide a valid Groq API key to continue.")
        st.stop()

# Initialize Groq LLM (vision model) with validated key
llm = init_chat_model(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    model_provider="groq",
    api_key=api_key,
)



# Step 1: Upload Image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Step 2: Preview the uploaded image
if uploaded_file:
    uploaded_file.seek(0)  # ensure pointer is at start
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Step 3: Form for question input (clears automatically after submit)
    with st.form("ask_form", clear_on_submit=True):
        user_question = st.text_input("Ask a question about the image")
        submitted = st.form_submit_button("Ask")

    # Step 4: Process when form is submitted
    if submitted and user_question:
        uploaded_file.seek(0)  # reset pointer again before reading
        image_bytes = uploaded_file.read()
        base64_image = base64.b64encode(image_bytes).decode("utf-8")

        # Construct message in Groq schema
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": user_question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        },
                    },
                ],
            }
        ]

        # Query Groq
        with st.spinner("Analyzing image..."):
            response = llm.invoke(messages)

        # Display response
        st.subheader("Answer:")
        st.write(response.content if hasattr(response, "content") else response.text)
