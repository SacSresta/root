API_KEY = "2092774d87027059265e897f7452eaa9-d4a0390dbef600c8119e62ab83b0b5a2"
ACCOUNT_ID = "101-011-24509333-001"
OANDA_URL = "https://api-fxpractice.oanda.com/v3"

SECURE_HEADER = {
    'Authorization': f'Bearer {API_KEY}',  # Corrected 'Authorization' spelling
    'Content-Type': 'application/json'
}

BUY = 1
SELL = -1
NONE = 0