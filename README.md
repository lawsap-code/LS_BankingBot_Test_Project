# Banking AI Bot

A sophisticated banking assistant powered by **Mistral AI Large Model**.

## 🚀 Features

- **Interactive conversational interface** with multi-turn conversation support
- **Banking expertise** on topics including:
  - Account types and management
  - Loan and mortgage guidance
  - Investment and portfolio advice
  - Fraud protection and security
  - Financial planning and budgeting
  - Credit card information
  - Transaction and payment assistance
  
- **Mistral AI Large Model** for high-quality, contextual responses
- **Conversation history** tracking for coherent discussions
- **User-friendly CLI interface** with clear formatting

## 📋 Requirements

- Python 3.8+
- Virtual environment (optional but recommended)
- Mistral AI API key

## 🛠️ Installation

1. **Create and activate virtual environment:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # On Windows PowerShell
   # or
   source .venv/bin/activate     # On macOS/Linux
   ```

2. **Install required package:**
   ```bash
   pip install mistralai
   ```

## 🏃 Running the Bot

### Interactive Mode

```bash
python banking_bot.py
```

Then type your questions in natural language:
```
You: What is the difference between a savings account and a checking account?
🤖 Banking Bot: [Response from the bot...]
```

### Test Mode

Run the test script to see example queries and responses:
```bash
python test_bot.py
```

## 📖 Usage Examples

### Example 1: Account Information
```
You: What should I consider when opening a savings account?
🤖 Banking Bot: When opening a savings account, consider these key factors...
```

### Example 2: Fraud Protection
```
You: How can I protect myself from banking fraud?
🤖 Banking Bot: Here are 10 essential ways to prevent fraud...
```

### Example 3: Mortgage Guidance
```
You: What factors should I consider when applying for a mortgage?
🤖 Banking Bot: Applying for a mortgage is a major financial decision...
```

## 🎮 Commands

| Command | Description |
|---------|-------------|
| `quit` or `exit` | End the conversation |
| `clear` | Start a new conversation (clears history) |

## 🔑 API Configuration

The bot uses the Mistral AI API. The API key is configured in the script:

```python
API_KEY = "t8D9FaLjfluImZ7qAZ7EWPd3D5TxhBen"
client = Mistral(api_key=API_KEY)
```

Model used: `mistral-large-latest`

## 📁 File Structure

```
Banking/
├── banking_bot.py      # Main bot application
├── test_bot.py        # Test script with sample queries
├── README.md          # This file
└── .venv/             # Virtual environment (created after setup)
```

## 🔒 Security & Disclaimers

⚠️ **IMPORTANT**: This is an **educational AI assistant**. 

- **NOT for real transactions**: Do not use for actual banking operations
- **Consult professionals**: For complex financial decisions, consult with licensed financial advisors
- **Data security**: API key should be stored securely (not in version control)
- **Accuracy**: While the bot provides quality information, always verify with official banking sources
- **Limitations**: The bot cannot execute actual banking transactions or access real account information

## 💡 Tips for Best Results

1. **Be specific**: Ask clear, detailed questions
2. **Follow-up**: The bot maintains conversation history for context
3. **Clarify**: If the response is unclear, ask for clarification
4. **Provide context**: Include relevant financial information when appropriate
5. **Multiple topics**: The bot can handle various financial topics in one conversation

## 🐛 Troubleshooting

### API Key Error
```
Error communicating with Mistral AI: Invalid API key
```
- Verify the API key in `banking_bot.py` is correct
- Check internet connection

### Import Error
```
ModuleNotFoundError: No module named 'mistralai'
```
- Ensure you're in the virtual environment
- Run `pip install mistralai`

### Connection Timeout
- Check internet connection
- Verify Mistral API is accessible
- Try again after a few seconds

## 📚 Resources

- [Mistral AI Documentation](https://docs.mistral.ai/)
- [Mistral API Reference](https://docs.mistral.ai/api/)
- [Financial Literacy Resources](https://www.consumer.ftc.gov/)

## 🤝 Contributing

This is an educational project. Feel free to extend it with:
- Additional banking topics
- Enhanced conversation features
- Integration with banking APIs (read-only)
- Web interface
- Multi-language support

## 📄 License

This project is provided as-is for educational purposes.

## ✨ Features Roadmap

- [ ] Web interface (Flask/Streamlit)
- [ ] Database for conversation logging
- [ ] Advanced financial calculations
- [ ] Integration with real-time market data
- [ ] Multi-language support
- [ ] Voice interaction
- [ ] Personalized financial recommendations

---

**Last Updated**: February 7, 2026
**Bot Version**: 1.0
**Model**: Mistral AI Large
