# QuietSpark

**QuietSpark** is a personal, agent-based AI companion system designed for intentional, introvert-friendly living. It supports reflection, emotional affirmation, ethical decision-making, and voice-first interaction — all backed by long-term memory.

## ✨ Features
- 🔊 Voice-to-text journaling (powered by OpenAI Whisper)
- 💬 Modular agents with distinct tones and purposes
- 🧠 Persistent memory per agent (local JSON store)
- 🌱 Built with LangChain + OpenAI API
- 🧘‍♀️ Designed for softness, sovereignty, and self-alignment

## 🧱 Core Agents
- **Affirmation Agent** – Supports self-trust, motivation, and emotional regulation
- **Companion Agent** – Reflects on your journaling, spots patterns, holds space
- **Ethics Agent** – Helps navigate low-impact living, veganism, and slow consumption (coming soon)

## 📦 Requirements
See `requirements.txt`.

## 🚀 Getting Started
```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/quietspark.git
cd quietspark

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Set up your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" > .env