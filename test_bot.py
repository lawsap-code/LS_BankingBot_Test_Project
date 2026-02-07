#!/usr/bin/env python3
"""Test script for the banking bot"""

import sys
sys.path.insert(0, 'd:\\LISRC\\AI\\Banking')

from banking_bot import chat_with_bot, create_chat_conversation

def test_banking_bot():
    """Test the banking bot with sample queries"""
    
    print("🧪 Testing Banking Bot...\n")
    
    conversation_history = create_chat_conversation()
    
    # Test queries
    test_questions = [
        "What is the difference between a savings account and a checking account?",
        "How can I protect myself from fraud?",
        "What factors should I consider when applying for a mortgage?"
    ]
    
    for i, question in enumerate(test_questions, 1):
        print(f"Test #{i}")
        print(f"Question: {question}")
        print("-" * 60)
        
        response, conversation_history = chat_with_bot(question, conversation_history)
        
        if response:
            print(f"Response: {response}")
        else:
            print("❌ Failed to get response from bot")
        
        print("=" * 60 + "\n")

if __name__ == "__main__":
    test_banking_bot()
