# 🤖 OpenAI API Caller

> 🚀 A Python program that interacts with OpenAI's GPT-3.5-turbo model and shows token usage stats.


## 📖 Overview

This simple yet powerful tool connects to OpenAI's API and allows you to:
- Send prompts to the GPT-3.5-turbo model
- Get AI-generated responses in real-time
- Monitor your token usage for cost management

Perfect for developers exploring AI capabilities or anyone learning to work with language models!

## ✨ Features

- 🧠 Uses the powerful gpt-3.5-turbo model
- 💬 Includes a fixed system prompt for consistent responses
- 📊 Displays detailed token usage statistics
- 🛡️ Handles API errors gracefully
- 🔒 Securely manages API keys via environment variables

## 📋 Requirements

- 🐍 Python 3.6+
- 🔑 OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- 📦 Required packages: `openai`, `python-dotenv`

## 🛠️ Installation

1️⃣ **Clone this repository:**
```bash
git clone https://github.com/yourusername/openai-api-caller.git
cd openai-api-caller
```

2️⃣ **Install required packages:**
```bash
pip install openai python-dotenv
```

3️⃣ **Create a `.env` file in the project directory:**
```
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Usage

Run the program:
```bash
python api_call.py
```

### 🔄 How it works:
1. 💭 Enter your question when prompted
2. 🌐 The program sends your question to OpenAI with a predefined system prompt
3. 📝 The AI response is displayed in the console
4. 📈 Token usage statistics are shown (prompt, completion, and total)

## 📝 Example

```
Enter your question: What is artificial intelligence?

Assistant's response:
Artificial intelligence is a field of computer science focused on creating systems capable of performing tasks that typically require human intelligence...

Token usage:
Prompt tokens: 27
Completion tokens: 58
Total tokens: 85
```

## 🔧 Customization

You can easily modify the system prompt in the code to change how the AI responds:

```python
# In api_call.py
system_prompt = "You are a helpful, concise assistant."  # Change this as needed
```

## 📊 Token Usage

Understanding token usage helps manage costs when using OpenAI's API:

- **Prompt tokens:** Count of tokens in your input
- **Completion tokens:** Count of tokens in the AI response
- **Total tokens:** Sum of prompt and completion tokens

OpenAI charges based on the total number of tokens processed.
