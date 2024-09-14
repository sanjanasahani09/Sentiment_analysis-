from transformers import pipeline

# Use 'text-generation' instead of 'conversational'
chatbot = pipeline('text-generation', model='microsoft/DialoGPT-medium')

def get_response(user_message):
    # Use the chatbot to generate a response
    response = chatbot(user_message, max_length=100)
    return response[0]['generated_text']
