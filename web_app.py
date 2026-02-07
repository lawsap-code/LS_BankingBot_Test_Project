#!/usr/bin/env python3
"""
Streamlit Web Interface for Banking AI Bot
Run with: streamlit run web_app.py
"""

import streamlit as st
from mistralai import Mistral
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Banking AI Assistant",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize theme in session state
if "theme" not in st.session_state:
    st.session_state.theme = "light"

# Define color themes
THEMES = {
    "light": {
        "bg_main": "#f8f9fa",
        "bg_chat": "white",
        "text_chat": "#333333",
        "header_start": "#667eea",
        "header_end": "#764ba2",
        "input_bg": "white",
        "input_text": "#2c3e50",
        "input_border": "#e0e0e0",
        "border_accent": "#667eea",
    },
    "dark": {
        "bg_main": "#1a1a1a",
        "bg_chat": "#2d2d2d",
        "text_chat": "#e0e0e0",
        "header_start": "#667eea",
        "header_end": "#764ba2",
        "input_bg": "#333333",
        "input_text": "#ffffff",
        "input_border": "#555555",
        "border_accent": "#667eea",
    },
    "red-blue": {
        "bg_main": "#f0f2f5",
        "bg_chat": "#ffffff",
        "text_chat": "#1a1a1a",
        "header_start": "#e63946",
        "header_end": "#1d3557",
        "input_bg": "#f8f9fa",
        "input_text": "#1a1a1a",
        "input_border": "#e63946",
        "border_accent": "#e63946",
    },
}

# Get current theme
theme = THEMES[st.session_state.theme]

# Custom CSS based on selected theme
st.markdown(f"""
    <style>
    .main {{
        background-color: {theme['bg_main']};
    }}
    .stChatMessage {{
        background-color: {theme['bg_chat']};
        border-radius: 10px;
        color: {theme['text_chat']};
        border-left: 4px solid {theme['border_accent']};
    }}
    .header-container {{
        background: linear-gradient(135deg, {theme['header_start']} 0%, {theme['header_end']} 100%);
        color: white;
        padding: 30px;
        border-radius: 10px;
        margin-bottom: 20px;
    }}
    .header-container h1 {{
        color: white;
    }}
    .header-container p {{
        color: rgba(255, 255, 255, 0.95);
    }}
    .info-box {{
        background-color: {theme['input_bg']};
        border-left: 4px solid {theme['border_accent']};
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }}
    .success-box {{
        background-color: {theme['bg_chat']};
        border-left: 4px solid #4CAF50;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }}
    /* Chat input styling */
    .stChatInput {{
        background-color: {theme['input_bg']} !important;
        border: 2px solid {theme['input_border']} !important;
        border-radius: 8px !important;
        padding: 8px !important;
        margin: 10px 0 !important;
    }}
    .stChatInput input,
    .stChatInput textarea {{
        background-color: {theme['input_bg']} !important;
        color: {theme['input_text']} !important;
        border: none !important;
        padding: 12px !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }}
    .stChatInput input::placeholder,
    .stChatInput textarea::placeholder {{
        color: rgba(128, 128, 128, 0.5) !important;
    }}
    .stChatInput input:focus,
    .stChatInput textarea:focus {{
        background-color: {theme['input_bg']} !important;
        color: {theme['input_text']} !important;
        border: 2px solid {theme['border_accent']} !important;
        outline: none !important;
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize Mistral client
API_KEY = os.getenv("MISTRAL_API_KEY")
if not API_KEY:
    st.error("❌ Error: MISTRAL_API_KEY not found. Please set it in your .env file.")
    st.stop()
client = Mistral(api_key=API_KEY)

# Banking bot system prompt
BANKING_SYSTEM_PROMPT = """You are a professional banking assistant AI bot. You help customers with:
- Account information and balance inquiries
- Transaction history and statements
- Banking products (savings accounts, checking accounts, loans, mortgages)
- Investment advice and portfolio management
- Credit card information and rewards
- Money transfer and payment assistance
- Fraud protection and security advice
- Budgeting and financial planning
- Loan applications and mortgage guidance
- Interest rates and APY information

You are knowledgeable, professional, and helpful. You always:
- Provide accurate financial information
- Encourage responsible banking practices
- Suggest consulting with financial advisors for complex decisions
- Prioritize customer data security
- Are empathetic to customer concerns
- Provide clear explanations of banking concepts

DISCLAIMER: This is an educational AI assistant. For actual banking transactions, 
please contact your bank directly or use official banking channels."""

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

if "start_time" not in st.session_state:
    st.session_state.start_time = datetime.now()


def get_bot_response(user_message):
    """Get response from Mistral AI"""
    try:
        # Build messages for API (without timestamps)
        api_messages = [
            {"role": msg["role"], "content": msg["content"]}
            for msg in st.session_state.messages
        ]
        
        # Add current user message
        api_messages.append({"role": "user", "content": user_message})
        
        # Call Mistral API
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {"role": "system", "content": BANKING_SYSTEM_PROMPT}
            ] + api_messages,
            temperature=0.7,
            max_tokens=1500
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"❌ Error communicating with Mistral AI: {str(e)}"


def main():
    """Main Streamlit app"""
    
    # Header
    st.markdown("""
        <div class="header-container">
            <h1>🏦 Banking AI Assistant</h1>
            <p style="font-size: 18px; margin: 0;">Powered by Mistral AI Large Model</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## 📋 About This Bot")
        st.info("""
        This banking assistant provides help with:
        - Account types and management
        - Banking products information
        - Financial planning advice
        - Fraud protection tips
        - Loan and mortgage guidance
        - Investment assistance
        
        **Disclaimer:** For actual banking transactions, contact your bank directly.
        """)
        
        st.markdown("---")
        st.markdown("## ⚙️ Settings")
        
        # Theme selector
        st.markdown("### 🎨 Color Theme")
        new_theme = st.radio(
            "Choose a theme:",
            options=["light", "dark", "red-blue"],
            index=["light", "dark", "red-blue"].index(st.session_state.theme),
            format_func=lambda x: "☀️ Light" if x == "light" else "🌙 Dark" if x == "dark" else "🔴 Red-Blue"
        )
        
        if new_theme != st.session_state.theme:
            st.session_state.theme = new_theme
            st.rerun()
        
        st.markdown("---")
        
        if st.button("🔄 Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            st.session_state.message_count = 0
            st.session_state.start_time = datetime.now()
            st.success("✅ Conversation cleared!")
            st.rerun()
        
        st.markdown("---")
        st.markdown("## 📊 Statistics")
        
        if st.session_state.messages:
            user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
            bot_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
            duration = (datetime.now() - st.session_state.start_time).total_seconds()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Your Questions", user_msgs)
            with col2:
                st.metric("Bot Responses", bot_msgs)
            
            st.metric("Duration", f"{int(duration)}s")
        else:
            st.text("No messages yet")
    
    # Main chat area
    st.markdown("## 💬 Chat")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar="👤" if message["role"] == "user" else "🤖"):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about banking..."):
        # Add user message to history
        st.session_state.messages.append({
            "role": "user",
            "content": prompt,
            "timestamp": datetime.now().isoformat()
        })
        
        # Display user message
        with st.chat_message("user", avatar="👤"):
            st.markdown(prompt)
        
        # Get and display bot response
        with st.chat_message("assistant", avatar="🤖"):
            with st.spinner("🤔 Thinking..."):
                response = get_bot_response(prompt)
            st.markdown(response)
        
        # Add bot response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "timestamp": datetime.now().isoformat()
        })
        
        st.session_state.message_count += 1
    
    # Footer
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; color: #666; padding: 20px;">
            <p><strong>Banking AI Assistant</strong> | Powered by Mistral AI</p>
            <p style="font-size: 12px;">For educational purposes only. Not for real banking transactions.</p>
        </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
