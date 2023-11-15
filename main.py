import openai
import spacy

# Set your OpenAI API key
openai.api_key = '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'

# Initialize spaCy
nlp = spacy.load("en_core_web_sm")

# Initialize the conversation
conversation_history = []

while True:
    # Get user input
    user_input = input("You: ")

    # Break the loop if the user types 'exit'
    if user_input.lower() == 'exit':
        break

    # Add user input to conversation history
    conversation_history.append(f"You: {user_input}")

    # Generate a response using GPT-3.5 Turbo
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use "text-davinci-003" for GPT-3.5 Turbo
        prompt='\n'.join(conversation_history),
        max_tokens=150  # You can adjust the max_tokens parameter based on your needs
    )

    # Extract and print the generated response
    generated_response = response['choices'][0]['text']
    print(f"ChatGPT: {generated_response}")

    # Add ChatGPT's response to the conversation history
    conversation_history.append(f"ChatGPT: {generated_response}")

    # Perform entity extraction using spaCy
    doc = nlp(generated_response)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print("Entities:", entities)
