
# Multi-Modal Flight Assistant

OpenAI agent: Text → Flight prices + DALL-E images + TTS responses.

[![Gradio](https://img.shields.io/badge/Gradio-Live-brightgreen?logo=gradio)](https://3e719bc121f00297f3.gradio.live)

## ✨ Features
- **🛫 Function Calling** → Real-time SQLite flight prices
- **🗣️ Text-to-Speech** → Onyx voice responses  
- **🖼️ DALL-E 3** → Pop-art style city images
- **🎙️ Gradio UI** → Production chat interface

## 🚀 Quick Start
```bash
pip install -r requirements.txt

cat > .env << EOF
OPENAI_API_KEY=sk-your-key-here
MODEL=gpt-4o-mini
DB_PATH=prices.db
IMAGE_MODEL=dall-e-3
TTS_MODEL=tts-1
TTS_VOICE=onyx
IMAGE_SIZE=1024x1024
EOF

python app.py
**VSCode → Update .env section only:**
```

## 🏗️ Architecture

- **app.py**           → Gradio UI
- **src/agents.py**    → OpenAI tool calling
- **src/database.py**  → SQLite prices
- **src/openai_client**→ DALL-E + TTS







