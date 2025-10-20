🧠 Helpful Multi-Tool AI Agent

This project demonstrates how to create a custom AI Agent that can:

Answer general questions using its own reasoning.

Calculate mathematical expressions.

Provide information about Artificial Intelligence (AI).

Tell the capital of any country.

The agent is powered by Gemini 2.0 Flash (Google Generative Language Model) and built using the OpenAI Agent SDK.

🚀 Features

Capital Tool: Returns the capital city of any given country.

AI Tool: Answers questions about AI topics, AI models, and AI history.

Calculator Tool: Solves simple mathematical expressions (like 2+2 or 50+100).

Gemini API Integration: Uses Gemini’s API as the backend model for chat completions.

🧩 Requirements

Make sure you have the following installed:

pip install agents python-dotenv


You’ll also need a valid Gemini API key.

⚙️ Environment Setup

Create a .env file in your project folder and add:

GEMINI_API_KEY=your_gemini_api_key_here

📘 How It Works
1. Load Environment and Disable Tracing
load_dotenv()
set_tracing_disabled(True)


Loads the environment variables (API key) and disables tracing logs.

2. Initialize the Gemini Client
client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta"
)


This connects your program to the Gemini API.

3. Set Up the Model and Config
mymodel = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

confiq = RunConfig(
    model=mymodel,
    model_provider=client,
    tracing_disabled=True
)


These lines configure the Gemini model and define how the agent will communicate with it.

4. Define the Tools

Each Python function is wrapped using function_tool() to be used by the agent.

a. Capital Tool

def get_capital(country: str) -> str:
    return f"Please provide the capital city of {country}."


b. AI Tool

def get_Ai(Ai: str) -> str:
    return f"please provide the AI topics, AI models, and AI history {Ai}"


c. Calculator Tool

def get_calculater(expression: str) -> str:
    return str(eval(expression))

5. Create the Agent
agent = Agent(
    name="helpful agent",
    instructions="You will give the user a clear answer to the question.",
    tools=[capital_tool, AI_tool, calculater_tool]
)


This defines the agent’s name, purpose, and tools.

6. Run the Agent
result = Runner.run_sync(agent, input="calculate 50+100?", run_config=confiq)
print(result.final_output)


This line sends a user query to the agent and prints its response.

🧪 Example Output
Input: calculate 50+100?
Output: 150


or

Input: What is the capital of France?
Output: The capital of France is Paris.

🧰 Summary
Tool Name	Description
get_capital()	Gives the capital of a country
get_Ai()	Answers AI-related questions
get_calculater()	Performs mathematical calculations
🧠 Concept Recap

Agent: A program that uses tools and a model to answer queries.

Tool: A Python function that performs a specific task.

Runner: Executes the agent and retrieves the result.

Gemini API: The backend AI model that processes the conversation.
