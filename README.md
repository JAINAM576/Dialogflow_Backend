# Dialogflow Backend

## Overview
This project is a **currency conversion chatbot** built using **Dialogflow**, **Flask**, and **Telegram**. The chatbot identifies user intents, extracts currency-related entities, and fetches real-time exchange rates to provide currency conversion. Additionally, it supports small talk and normal conversational responses.

## Project Flow
1. **User interacts via Telegram** → [Jainam Currency Bot](http://t.me/Jainam_currency_bot)
2. **Dialogflow identifies the intent**
   - If it's a **currency conversion request**, extract **source currency, amount, and target currency**
   - If it's a **normal conversation**, respond directly
3. **For currency conversion requests** → Dialogflow sends data to the Flask backend via **fulfillment webhook**
4. **Flask backend processes the request**
   - Uses **CurrencyConverter API** to fetch conversion rates
   - Computes the converted amount
   - Sends the result back to the chatbot
5. **Response is displayed to the user** in the Telegram interface

## Technologies Used
- **Dialogflow**: AI-powered chatbot development
- **Flask**: Python backend for handling webhook requests
- **CurrencyConverter API**: Fetching real-time exchange rates
- **Google Cloud**: Hosting the Dialogflow agent

## Directory Structure
```
└── jainam576-dialogflow_backend/
    ├── main.py               # Flask backend logic
    └── requirements.txt      # Python dependencies
```

## Setup Instructions
### 1. Clone the repository
```sh
git clone https://github.com/your-repo/jainam576-dialogflow_backend.git
cd jainam576-dialogflow_backend
```

### 2. Install dependencies
```sh
pip install -r requirements.txt
```

### 3. Set up Dialogflow
- Create an agent in **Dialogflow** (Google Cloud)
- Train it with **intents**:
  - Currency conversion (extract currency and amount entities)
  - Small talk (greetings, fun replies, etc.)
- Enable **fulfillment webhook** to send currency requests to the Flask backend

### 4. Run the Flask backend
```sh
python main.py
```

### 5. Deploy and Integrate with Telegram
- Deploy the backend (e.g., Google Cloud, AWS, Heroku)
- Connect the Dialogflow agent to **Telegram Bot API**
- Use the Telegram bot at [Jainam Currency Bot](http://t.me/Jainam_currency_bot)

## Usage Example
**User:** "Convert 100 USD to EUR"

**Bot:** "100.0 USD is 91.69 EUR 💱"

## Future Enhancements
- Improve accuracy using multiple exchange rate APIs
- Add support for historical currency rates
- Implement voice input for conversions

## Developer
**Jainam Sanghavi** 

