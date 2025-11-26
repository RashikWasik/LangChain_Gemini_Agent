from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import sys

# Setting up the model
API_KEY = "MY API KEY"  # Replace with your own Google API key

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=API_KEY
)

# Create a prompt template to send questions to the model
prompt = ChatPromptTemplate.from_messages([
    ("human", "{question}")
])

# Combine the prompt and the model into a simple chain
chain = prompt | model


# Get user input
question = input("\nAsk anything: ")

# Stops the program if the user enters nothing
if not question.strip():
    print("\nInput cannot be empty. Exiting.")
    sys.exit(0)


# Running the model 
response = chain.invoke({"question": question})

# Show the model's answer
print("\nModel Response:")
print(response.content + "\n")
