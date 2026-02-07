#!/usr/bin/env python3
"""
Banking AI Bot using Mistral AI Large Model
This bot provides banking-related assistance and advice
"""

import os
from mistralai import Mistral
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Mistral client with API key
API_KEY = os.getenv("MISTRAL_API_KEY")
if not API_KEY:
    print("❌ Error: MISTRAL_API_KEY not found. Please set it in your .env file.")
    exit(1)
client = Mistral(api_key=API_KEY)

# System prompt for the banking bot
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


def create_chat_conversation():
    """Initialize conversation history"""
    return []


def chat_with_bot(user_message, conversation_history):
    """
    Send a message to the banking bot and get a response
    
    Args:
        user_message: The user's input message
        conversation_history: List of previous messages in conversation
    
    Returns:
        The bot's response and updated conversation history
    """
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    try:
        # Call Mistral API with conversation history
        response = client.chat.complete(
            model="mistral-large-latest",
            messages=[
                {
                    "role": "system",
                    "content": BANKING_SYSTEM_PROMPT
                }
            ] + conversation_history,
            temperature=0.7,
            max_tokens=1024
        )
        
        # Extract bot response
        bot_message = response.choices[0].message.content
        
        # Add bot response to history
        conversation_history.append({
            "role": "assistant",
            "content": bot_message
        })
        
        return bot_message, conversation_history
    
    except Exception as e:
        error_message = f"Error communicating with Mistral AI: {str(e)}"
        print(f"\n❌ {error_message}")
        return None, conversation_history


def display_welcome_message():
    """Display welcome message to the user"""
    print("\n" + "="*60)
    print("🏦 BANKING AI ASSISTANT BOT")
    print("="*60)
    print("Welcome to the Banking AI Assistant powered by Mistral AI!")
    print("\nI'm here to help you with:")
    print("  • Account information and inquiries")
    print("  • Banking products information")
    print("  • Financial planning advice")
    print("  • Transaction assistance")
    print("  • Security and fraud prevention tips")
    print("\nType 'quit' or 'exit' to end the conversation")
    print("Type 'clear' to start a new conversation")
    print("="*60 + "\n")


def main():
    """Main function to run the banking bot"""
    display_welcome_message()
    conversation_history = create_chat_conversation()
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("\n👋 Thank you for using Banking AI Assistant. Goodbye!")
                break
            
            # Check for clear command
            if user_input.lower() == 'clear':
                conversation_history = create_chat_conversation()
                print("\n🔄 Conversation cleared. Starting fresh!\n")
                continue
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Get response from bot
            print("\n🤖 Banking Bot: ", end="", flush=True)
            response, conversation_history = chat_with_bot(user_input, conversation_history)
            
            if response:
                print(response)
            
            print()  # Add spacing between exchanges
        
        except KeyboardInterrupt:
            print("\n\n👋 Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {str(e)}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
