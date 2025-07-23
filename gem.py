import google.generativeai as genai

API_KEY = "AIzaSyDSLrugyXug-rlilLfGaZnx0oaaNR-S-is"
genai.configure(api_key=API_KEY)

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")  # use available models like "gemini-1.5-flash"
chat = model.start_chat()

print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)  # Send actual user input
    print("Gemini:", response.text)
