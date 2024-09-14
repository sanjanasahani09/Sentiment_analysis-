# AI Chatbot with Sentiment Analysis

This project is a **Conversational AI Chatbot** that integrates **Sentiment Analysis** to enhance user interaction by providing real-time sentiment feedback. Built using the Flask web framework, this chatbot allows users to engage in natural conversations with an AI, while the sentiment of the user’s input (positive, neutral, or negative) is analyzed and returned with each response.

## Key Features

- **Interactive Chatbot**: The chatbot leverages a pre-trained language model (DialoGPT) to generate meaningful and coherent responses based on user input, making the interaction feel more natural.

- **Sentiment Analysis**: Sentiment analysis is performed on every user message, helping to determine the emotional tone (positive, neutral, or negative) of the conversation. This analysis can be used to track the user’s mood and potentially adapt the chatbot’s responses.

- **Modern User Interface**: The web interface for the chatbot is designed with a modern, user-friendly UI, providing a clean and intuitive chat experience. The interface is responsive and optimized for both desktop and mobile devices.

- **Real-Time Conversations**: The chatbot handles real-time requests and responses through a Flask server, ensuring instant feedback for each user query.

## Technologies Used

- **Flask**: A lightweight Python web framework used to create the web application and handle API requests.
- **Hugging Face Transformers**: Used for integrating the pre-trained **DialoGPT** model to generate conversational responses.
- **PyTorch**: A deep learning framework to support the DialoGPT model.
- **Natural Language Processing (NLP)**: For both generating responses and performing sentiment analysis.
- **HTML/CSS/JavaScript**: Front-end technologies used to build a clean and modern user interface, enhancing the overall user experience.

## How It Works

1. The user inputs a message in the chat interface.
2. The message is sent to the Flask backend, where it is processed by the AI model (DialoGPT) to generate a response.
3. Simultaneously, the message is passed through a sentiment analysis model to determine its emotional tone.
4. Both the response and sentiment are returned to the user in the chat interface, providing insightful feedback along with the bot’s reply.

## Potential Applications

- **Customer Support Chatbots**: Providing automated customer service while monitoring customer satisfaction through sentiment analysis.
- **Mental Health Monitoring**: Tracking user sentiments over time to detect emotional trends and respond accordingly.
- **Engagement and Marketing**: Understanding user sentiments in marketing or survey bots to adapt to customer feedback in real-time.

This project demonstrates how combining conversational AI with sentiment analysis can create intelligent and emotionally aware chatbots, useful in a wide variety of applications ranging from customer service to emotional support systems.
