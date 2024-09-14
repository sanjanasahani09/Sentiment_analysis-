from flask import Flask, request, jsonify, render_template
from chatbot_model import get_response
from sentiment_analysis import analyze_sentiment

app = Flask(__name__)

# Serve the chatbot web page
@app.route('/')
def home():
    return render_template('index.html')

# Handle the chat requests
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']  # Get the message from the user
    
    # Get response from the chatbot AI
    bot_response = get_response(user_message)
    
    # Analyze the sentiment of the user's message
    sentiment = analyze_sentiment(user_message)
    
    # Send back both the bot response and the sentiment
    return jsonify({'response': bot_response, 'sentiment': sentiment})

if __name__ == "__main__":
    app.run(debug=True)
