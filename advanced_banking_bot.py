#!/usr/bin/env python3
"""
Advanced Banking Bot with Additional Features
Includes conversation management, logging, and advanced banking functions
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Optional
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


class BankingBot:
    """Advanced Banking Bot with conversation management and logging"""
    
    def __init__(self, log_file: str = "conversation_log.json"):
        self.conversation_history: List[Dict] = []
        self.log_file = log_file
        self.start_time = datetime.now()
        self.message_count = 0
    
    def add_to_history(self, role: str, content: str) -> None:
        """Add a message to conversation history"""
        self.conversation_history.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_response(self, user_message: str) -> Optional[str]:
        """
        Get response from Mistral AI
        
        Args:
            user_message: User's input message
            
        Returns:
            Bot's response or None if error
        """
        self.add_to_history("user", user_message)
        
        try:
            # Build message list for API (without timestamps)
            api_messages = [
                {"role": msg["role"], "content": msg["content"]} 
                for msg in self.conversation_history
            ]
            
            # Call Mistral API
            response = client.chat.complete(
                model="mistral-large-latest",
                messages=[
                    {
                        "role": "system",
                        "content": BANKING_SYSTEM_PROMPT
                    }
                ] + api_messages,
                temperature=0.7,
                max_tokens=1024
            )
            
            # Extract response
            bot_message = response.choices[0].message.content
            self.add_to_history("assistant", bot_message)
            self.message_count += 1
            
            return bot_message
        
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"\n❌ {error_msg}")
            return None
    
    def save_conversation(self) -> None:
        """Save conversation history to file"""
        try:
            data = {
                "start_time": self.start_time.isoformat(),
                "end_time": datetime.now().isoformat(),
                "message_count": self.message_count,
                "conversation": self.conversation_history
            }
            
            with open(self.log_file, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"\n✅ Conversation saved to {self.log_file}")
        except Exception as e:
            print(f"\n❌ Could not save conversation: {str(e)}")
    
    def clear_history(self) -> None:
        """Clear conversation history"""
        self.conversation_history.clear()
        self.message_count = 0
    
    def get_stats(self) -> Dict:
        """Get conversation statistics"""
        return {
            "message_count": self.message_count,
            "user_messages": len([m for m in self.conversation_history if m["role"] == "user"]),
            "bot_responses": len([m for m in self.conversation_history if m["role"] == "assistant"]),
            "duration_seconds": (datetime.now() - self.start_time).total_seconds()
        }
    
    def display_welcome(self) -> None:
        """Display welcome message"""
        print("\n" + "="*60)
        print("🏦 ADVANCED BANKING AI ASSISTANT BOT")
        print("="*60)
        print("Welcome to the Banking AI Assistant powered by Mistral AI!")
        print("\nI'm here to help you with:")
        print("  • Account information and inquiries")
        print("  • Banking products information")
        print("  • Financial planning advice")
        print("  • Transaction assistance")
        print("  • Security and fraud prevention tips")
        print("\n📋 Commands:")
        print("  • 'quit' or 'exit' - End the conversation")
        print("  • 'clear' - Start a new conversation")
        print("  • 'stats' - Show conversation statistics")
        print("  • 'save' - Save conversation to file")
        print("="*60 + "\n")
    
    def display_stats(self) -> None:
        """Display conversation statistics"""
        stats = self.get_stats()
        print("\n" + "-"*40)
        print("📊 CONVERSATION STATISTICS")
        print("-"*40)
        print(f"Total Messages: {stats['message_count']}")
        print(f"Your Questions: {stats['user_messages']}")
        print(f"Bot Responses: {stats['bot_responses']}")
        print(f"Duration: {int(stats['duration_seconds'])} seconds")
        print("-"*40 + "\n")


def main():
    """Main function"""
    bot = BankingBot()
    bot.display_welcome()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Handle commands
            if user_input.lower() in ['quit', 'exit']:
                print("\n👋 Thank you for using Banking AI Assistant!")
                if bot.message_count > 0:
                    response = input("Would you like to save this conversation? (yes/no): ").strip().lower()
                    if response in ['yes', 'y']:
                        bot.save_conversation()
                break
            
            elif user_input.lower() == 'clear':
                bot.clear_history()
                print("🔄 Conversation cleared. Starting fresh!\n")
                continue
            
            elif user_input.lower() == 'stats':
                bot.display_stats()
                continue
            
            elif user_input.lower() == 'save':
                bot.save_conversation()
                continue
            
            # Get response from bot
            print("\n🤖 Banking Bot: ", end="", flush=True)
            response = bot.get_response(user_input)
            
            if response:
                print(response)
            
            print()  # Spacing
        
        except KeyboardInterrupt:
            print("\n\n👋 Conversation interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
