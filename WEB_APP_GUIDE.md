# Running the Banking Bot in Browser

## 🌐 Web Interface (Streamlit)

The bot now has a full web interface built with Streamlit, allowing you to use it directly in your browser!

### Quick Start

1. **Install Streamlit** (if not already installed):
   ```bash
   pip install streamlit
   ```

2. **Run the web app:**
   ```bash
   streamlit run web_app.py
   ```

3. **Open in browser:**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually visit the URL shown in the terminal

### Features

✨ **Web Interface Features:**
- 💬 **Interactive Chat Interface** - Beautiful chat-like conversation
- 📊 **Statistics Panel** - Track questions, responses, and session duration
- 🔄 **Clear Conversation** - Start fresh anytime
- 💾 **Message History** - All messages preserved during session
- 🎨 **Modern UI** - Responsive design with gradient header
- 📱 **Mobile Friendly** - Works on mobile devices and tablets
- ⚡ **Real-time Updates** - Instant message display

### Browser Interface Layout

```
┌─────────────────────────────────────┐
│  🏦 Banking AI Assistant            │
│  Powered by Mistral AI              │
├─────────────────────────────────────┤
│ SIDEBAR               │ MAIN CHAT   │
│                       │             │
│ 📋 About              │ 💬 Messages │
│ ⚙️ Settings           │             │
│ [Clear Conv]          │ [User Q]    │
│ 📊 Statistics         │ [Bot A]     │
│                       │             │
│                       │ [Chat Input]│
└─────────────────────────────────────┘
```

### Usage Examples

**Example 1: First Time User**
```
1. Open browser to http://localhost:8501
2. In chat box: "What account should I open as a first-time saver?"
3. Read detailed response with recommendations
```

**Example 2: Multi-turn Conversation**
```
Message 1: "I have $50k in student loans"
Message 2: "What's the best repayment strategy?"
Message 3: "How does income-driven repayment work?"
→ Bot maintains context across all messages
```

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Ctrl+C` (terminal) | Stop the app |
| Browser Back | Go back (if needed) |

### Statistics & Monitoring

The sidebar displays real-time conversation stats:
- **Your Questions** - Count of questions asked
- **Bot Responses** - Count of responses received
- **Duration** - Session time elapsed

### Customization

**Styling:**
Edit the CSS in `web_app.py` to customize colors:
```python
<style>
.header-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style>
```

**Bot Behavior:**
Modify the system prompt to change bot personality:
```python
BANKING_SYSTEM_PROMPT = """Your custom prompt here..."""
```

### Troubleshooting

**Issue: "Module not found: streamlit"**
```bash
pip install streamlit
```

**Issue: Port 8501 already in use**
```bash
streamlit run web_app.py --server.port 8502
```

**Issue: App won't open automatically**
- Manually visit: `http://localhost:8501`

**Issue: Slow responses**
- Check internet connection
- Verify Mistral API is accessible

### Performance Tips

- Keep browser updated for best performance
- Close unnecessary tabs
- Clear conversation history if it grows very large

### Running on Different Ports

```bash
# Use custom port
streamlit run web_app.py --server.port 8502

# Expose to network (careful with this!)
streamlit run web_app.py --server.address 0.0.0.0
```

### Deployment Options

### Option 1: Local Network Sharing
```bash
streamlit run web_app.py --server.address 192.168.1.100
```
Then access from other devices: `http://192.168.1.100:8501`

### Option 2: Streamlit Cloud (Free)
1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Deploy directly from your repo

### Option 3: Docker Container
```dockerfile
FROM python:3.11
RUN pip install streamlit mistralai
COPY . /app
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "web_app.py"]
```

### Option 4: Cloud Platforms
- **AWS**: Use EC2 or Lightsail
- **Google Cloud**: Deploy on Cloud Run
- **Azure**: Use App Service
- **Heroku**: Deploy Streamlit apps

### Browser Compatibility

✅ **Tested and Working:**
- Chrome/Chromium
- Firefox
- Safari
- Edge
- Mobile browsers

### API Rate Limiting

The Mistral AI API has rate limits. If you get rate limit errors:
1. Wait a few seconds before the next message
2. Clear conversation history
3. Check your API quota

### Security Notes

⚠️ **Important:**
- API key is embedded in the code (for development only)
- For production, use environment variables: `export MISTRAL_API_KEY=your_key`
- Update code to read from environment:
  ```python
  import os
  API_KEY = os.getenv("MISTRAL_API_KEY")
  ```

### Accessing from Mobile

1. Run on your computer:
   ```bash
   streamlit run web_app.py --server.address 0.0.0.0
   ```

2. Find your computer's IP:
   - Windows: `ipconfig` (look for IPv4 Address)
   - Mac/Linux: `ifconfig`

3. On mobile, visit: `http://YOUR_IP:8501`

### Session Management

**Session Data:**
- Conversations are stored in session memory
- Lost when app restarts
- To persist: Use database integration

**Clear Data:**
- Click "🔄 Clear Conversation" button
- Refreshing page also resets conversation

### Advanced: Running Multiple Instances

```bash
# Terminal 1 - Instance 1
streamlit run web_app.py --server.port 8501

# Terminal 2 - Instance 2
streamlit run web_app.py --server.port 8502

# Terminal 3 - Instance 3
streamlit run web_app.py --server.port 8503
```

### Logs & Debug Info

Check terminal output for:
- Connection status to Mistral API
- Message processing times
- Any errors or warnings

### Next Steps

1. ✅ Run the web app
2. 📝 Try different questions
3. 🔧 Customize styling and behavior
4. 🚀 Deploy to cloud platform
5. 📊 Monitor usage statistics

---

**Happy banking with your AI assistant! 🏦**

See [README.md](README.md) for command-line options or [CONFIGURATION.md](CONFIGURATION.md) for advanced setup.
