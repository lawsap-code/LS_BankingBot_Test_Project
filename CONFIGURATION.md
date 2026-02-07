# Banking Bot Configuration Guide

## Configuration Files

### API Key Setup

The bot requires a valid Mistral AI API key. You have two options:

#### Option 1: Direct Configuration (Current)
The API key is stored directly in the Python files:
```python
API_KEY = "t8D9FaLjfluImZ7qAZ7EWPd3D5TxhBen"
```

#### Option 2: Environment Variable (Recommended for Production)
Create a `.env` file in the project root:
```
MISTRAL_API_KEY=your_api_key_here
```

Then modify the bot to read from environment:
```python
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MISTRAL_API_KEY")
```

## Bot Configuration

### System Prompt
The bot's behavior is controlled by the `BANKING_SYSTEM_PROMPT` variable. You can customize it to:
- Add specific banking products your organization offers
- Adjust tone and formality level
- Add domain-specific knowledge
- Modify disclaimer text

### API Parameters

In the `get_response()` method, you can adjust:

```python
response = client.chat.complete(
    model="mistral-large-latest",  # Model to use
    messages=[...],
    temperature=0.7,               # 0.0=deterministic, 1.0=creative
    max_tokens=1024                # Maximum response length
)
```

**Parameter tuning:**
- **temperature**: 
  - 0.0-0.3: More focused, consistent responses
  - 0.5-0.7: Balanced responses (recommended for banking)
  - 0.8-1.0: More creative, varied responses
  
- **max_tokens**: 
  - Lower = shorter responses, faster
  - Higher = longer detailed responses
  - Banking advice typically needs 800-1500 tokens

## Logging Configuration

### Conversation Logging
The advanced bot saves conversations to JSON files:

```python
# Default file
bot = BankingBot()  # Uses "conversation_log.json"

# Custom file
bot = BankingBot(log_file="banking_conversations.json")
```

## Advanced Customization

### Adding New Capabilities

1. **Custom Banking Tools**
   - Add methods to the `BankingBot` class
   - Example: `calculate_mortgage_payment()`, `check_fraud_alerts()`

2. **Integration with Banking APIs**
   - Add read-only integration with existing banking systems
   - Example: Display real account balances (sanitized)

3. **Multi-language Support**
   - Add system prompts for different languages
   - Use response translation

### Example Extension: Mortgage Calculator

```python
def calculate_mortgage_payment(principal: float, annual_rate: float, years: int) -> float:
    """Calculate monthly mortgage payment"""
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12
    if monthly_rate == 0:
        return principal / num_payments
    payment = principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
              ((1 + monthly_rate)**num_payments - 1)
    return payment

# Usage in bot
def handle_mortgage_calculation(self, user_message: str) -> Optional[str]:
    # Parse user input for mortgage details
    # Calculate payment
    # Return result with explanation
    pass
```

## Performance Tuning

### Response Speed
- Reduce `max_tokens` for faster responses
- Use lower `temperature` for simpler answers
- Consider caching common questions

### API Rate Limiting
- Mistral AI has rate limits per API key
- Implement request throttling if needed:
```python
import time

def rate_limited_get_response(self, user_message: str, min_delay: float = 0.5):
    time.sleep(min_delay)
    return self.get_response(user_message)
```

### Conversation History Management
- Clean up old conversations periodically
- Archive conversations older than 30 days
- Limit history size to recent 20 messages for context

## Monitoring & Analytics

### Track Metrics
```python
# Add to BankingBot class
self.metrics = {
    "total_requests": 0,
    "failed_requests": 0,
    "average_response_time": 0,
    "topics_discussed": {}
}
```

### Log Performance
```python
import time

def get_response(self, user_message: str) -> Optional[str]:
    start_time = time.time()
    response = self._call_api(user_message)
    elapsed = time.time() - start_time
    self.metrics["average_response_time"] = elapsed
    return response
```

## Security Considerations

1. **API Key Protection**
   - Never commit API keys to version control
   - Use environment variables or secure vaults
   - Rotate keys regularly

2. **Data Privacy**
   - Don't log sensitive financial information
   - Sanitize user inputs before logging
   - Comply with data protection regulations (GDPR, CCPA)

3. **Input Validation**
   - Validate user inputs for injection attacks
   - Sanitize responses before logging

4. **HTTPS Communication**
   - Ensure API calls use HTTPS
   - Verify SSL certificates

## Troubleshooting Configuration

### High API Costs
- Reduce `max_tokens`
- Implement response caching
- Batch similar queries

### Rate Limit Errors
- Implement exponential backoff retry logic
- Add request queuing
- Contact Mistral AI for higher limits

### Poor Response Quality
- Adjust `temperature` parameter
- Refine system prompt
- Provide more context in user messages
- Use more specific follow-up questions

## File Structure

```
Banking/
├── banking_bot.py              # Basic bot
├── advanced_banking_bot.py     # Advanced features
├── test_bot.py                 # Test script
├── CONFIGURATION.md            # This file
├── README.md                   # Main documentation
├── .env                        # Environment variables (optional)
├── conversation_log.json       # Saved conversations
└── .venv/                      # Virtual environment
```

## Requirements & Versions

- Python: 3.8+
- mistral-ai: 1.12.0+
- Other dependencies: See requirements.txt

---

**Last Updated**: February 7, 2026
