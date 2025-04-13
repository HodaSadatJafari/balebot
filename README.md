# BaleBot

[![Bale Messenger](https://img.shields.io/badge/Bale-Messenger-blue)](https://bale.ai/)
[![OpenAI Integration](https://img.shields.io/badge/OpenAI-Integration-green)](https://openai.com/)

A robust, AI-powered bot for Bale messenger that leverages language models to provide English language assistance.

## 🚀 Features

- English word definitions and explanations
- Synonym and antonym suggestions
- Example usage in sentences
- Powered by OpenAI's language models
- Simple, user-friendly interface

## 📋 Requirements

- Python 3.6+
- Bale messenger account
- OpenAI API key (or compatible LLM provider)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/balebot.git
   cd balebot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

Create a `.env` file in the project root with the following variables:

```
BOT_TOKEN=your_bale_bot_token
OPENAI_API_KEY=your_openai_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
```

### Getting the Required Keys

1. **Bale Bot Token**: 
   - Open Bale messenger
   - Start a chat with [@BotFather](https://bale.ai/botfather)
   - Follow instructions to create a new bot
   - Copy the provided token

2. **OpenAI API Key**:
   - Register at [OpenAI](https://platform.openai.com/)
   - Navigate to API keys section
   - Generate a new API key

## 🚀 Usage

The repository contains three sample implementations:

- `sample1.py`: Basic bot implementation
- `sample2.py`: Intermediate features
- `main.py`: Full-featured English language assistant

To run the main bot:

```bash
python main.py
```

### User Interaction

1. Start a chat with your bot in Bale messenger
2. Enter an English word
3. Select from available options:
   - Get definition
   - Find synonyms/antonyms
   - See example sentences
   - And more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Bale Messenger](https://bale.ai/) for their bot API
- [OpenAI](https://openai.com/) for their language model API

---

*Note: This bot is not officially affiliated with Bale or OpenAI.*