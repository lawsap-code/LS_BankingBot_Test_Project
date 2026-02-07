# 🏦 Banking AI Bot - Quick Start Guide

Your banking bot is now ready to use in **three different ways**!

## 🚀 Start Here - Choose Your Interface

### Option 1: 🌐 Web Browser Interface (Recommended)

**Best for**: Easy sharing, mobile access, modern interface

1. **Start the web app:**
   ```bash
   streamlit run web_app.py
   ```

2. **Open in browser:**
   - Automatically opens at: `http://localhost:8501`
   - Or manually visit: `http://localhost:8501`

3. **Use the bot:**
   - Type questions in the chat box
   - See responses instantly
   - Statistics displayed in sidebar

**Features:**
- Beautiful chat interface
- Real-time conversation tracking
- Session statistics
- Clear conversation button

---

### Option 2: 💻 Command Line Interface

**Best for**: Quick questions, terminal lovers, scripting

1. **Run the bot:**
   ```bash
   python banking_bot.py
   ```

2. **Commands:**
   - Type your question and press Enter
   - `quit` or `exit` to end
   - `clear` to start new conversation

**Example:**
```
You: What's the difference between a savings account and checking?
🤖 Banking Bot: Great question! Savings accounts and checking accounts serve...
```

---

### Option 3: 🔬 Advanced Features

**Best for**: Logging conversations, analytics, custom integration

1. **Run advanced bot:**
   ```bash
   python advanced_banking_bot.py
   ```

2. **Features:**
   - Conversation logging to JSON
   - Session statistics
   - Save conversations
   - Better for production use

---

## Setup (One-time only)

### 1. Activate Virtual Environment
```bash
# Windows
.\.venv\Scripts\Activate.ps1

# Mac/Linux
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Done! ✅

---

## Usage Scenarios

### Scenario 1: Asking a Quick Question
```bash
$ python banking_bot.py
You: How do I protect myself from fraud?
🤖 Banking Bot: Here are 10 essential ways to prevent fraud...
```

### Scenario 2: Learning About Products
```
Open: http://localhost:8501
Chat: What's the best investment strategy for beginners?
→ Get detailed, educational responses with examples
```

### Scenario 3: Multi-turn Conversation
```
Q1: I have $50k in student loans
Q2: What are my repayment options?
Q3: Which option saves me the most money?
→ Bot maintains context across all questions
```

---

## 📊 File Guide

| File | Purpose | Run With |
|------|---------|----------|
| `banking_bot.py` | Basic interactive bot | `python banking_bot.py` |
| `advanced_banking_bot.py` | Advanced features, logging | `python advanced_banking_bot.py` |
| `web_app.py` | Web interface | `streamlit run web_app.py` |
| `test_bot.py` | Test the bot | `python test_bot.py` |
| `requirements.txt` | Dependencies | `pip install -r requirements.txt` |

---

## 🔑 Important Notes

- **API Key**: Already configured (use your own key in production)
- **Model**: Mistral AI Large (best for banking advice)
- **Educational**: For learning - not for real transactions
- **Data**: Not stored anywhere (only in current session)

---

## ⚡ Quick Commands

```bash
# Activate environment
.\.venv\Scripts\Activate.ps1

# Run CLI version
python banking_bot.py

# Run web version
streamlit run web_app.py

# Run tests
python test_bot.py

# Check installed packages
pip list

# Install new packages
pip install package_name
```

---

## 🆘 Troubleshooting

**Problem: "Module not found"**
```bash
# Solution: Make sure environment is activated
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Problem: "Port 8501 already in use"**
```bash
# Use different port
streamlit run web_app.py --server.port 8502
```

**Problem: Slow responses**
- Check internet connection
- Wait a few seconds between messages
- Try clearing the conversation

---

## 📝 Example Questions to Try

1. "What's the difference between a savings account and checking account?"
2. "How can I protect myself from credit card fraud?"
3. "I want to buy a home. What should I know about mortgages?"
4. "What are the best practices for financial planning?"
5. "How does compound interest work?"
6. "What credit score do I need for a loan?"
7. "Should I pay off debt or invest?"
8. "What are the fees I should look for in banks?"

---

## 🎉 You're Ready!

Choose your preferred interface above and start chatting with your banking AI assistant! 🏦

For more details, see:
- [README.md](README.md) - Full documentation
- [WEB_APP_GUIDE.md](WEB_APP_GUIDE.md) - Web interface details
- [CONFIGURATION.md](CONFIGURATION.md) - Advanced configuration
- [USE_CASES.md](USE_CASES.md) - Real-world examples

---

**Last Updated**: February 7, 2026
**Version**: 1.1 (Now with web interface!)
