# 📸 Barai PictoChat

Barai PictoChat is a **Streamlit-based AI app** that allows you to **ask questions about uploaded images** using Groq’s LLaMA Vision models.  
It supports **automatic `.env` API key validation** and provides a **fallback option** for users to input their own API key if the `.env` key is invalid or missing.

---

## 🚀 Features
- Upload **JPG, JPEG, PNG** images.  
- Ask natural language questions about the image.  
- Uses **Groq LLaMA Vision model** for image understanding.  
- **Automatic `.env` API key validation**:
  - If a valid `GROQ_API_KEY` exists in `.env`, it’s used directly.
  - If invalid or missing, users are prompted to input their key in the **sidebar**.
- Clean **Streamlit UI** with custom footer branding.

---

## 📂 Project Structure


---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   # Using SSH
   git clone git@github.com:M-Ashraf-Barai/barai-PictoChat-assistant.git

   # OR using HTTPS
   git clone https://github.com/M-Ashraf-Barai/barai-PictoChat-assistant.git

2. **Setup UV if not already** 

 
```
pip install uv
```
3. **run uv sync to install packages and dependencies with same versions that repo has**    

```
uv sync
```

GROQ_API_KEY=your_groq_api_key_here
## Start application:
streamlit run main.py
