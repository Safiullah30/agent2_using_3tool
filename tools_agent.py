import os 
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig,set_tracing_disabled,AsyncOpenAI
from agents import function_tool
from dotenv import load_dotenv

# loead doten
load_dotenv()
set_tracing_disabled(True)

#setup apikey and client

client = AsyncOpenAI(
    api_key= os.getenv("GEMINI_API_KEY"),
     base_url="https://generativelanguage.googleapis.com/v1beta"
     
)

mymodel = OpenAIChatCompletionsModel(
      model="gemini-2.0-flash",
    openai_client=client
)

confiq = RunConfig(
    model = mymodel,
    model_provider= client,
    tracing_disabled= True
)
# Define a Python function as a tool
def get_capital(country: str) -> str:
    """
    This function simply returns an instruction for the agent
    to answer the capital of any country using its own knowledge.
    """
    return f"Please provide the capital city of {country}."

# Convert Python function to agent tool
capital_tool = function_tool(get_capital)


def get_Ai(Ai:str)  -> str:
    """__
    this tool provides answer to any question related to (AI) artificial intelligence.
    provide the most accurate and updated answer.for example, question about AI models, or AI history.
    """
    
    return f"please provide the ai topics,and AI models, AI history{Ai}"
    
    # Convert Python function to agent tool
AI_tool = function_tool(get_Ai)
    
def get_calculater(exoression:str)   ->str:
    """use this tool whenever the user ask a math-related question.
    for example: 2+2, and 3-2.
    """
    return str (eval(exoression))

calculater_tool = function_tool(get_calculater)

#crteat the agent. 
agent = Agent(
    name="helfpul agent",
    instructions= "you will give the user a clear answer to the question",
    tools= [capital_tool,AI_tool,calculater_tool]
)

# Run the agent
result = Runner.run_sync(agent, input="claculat the  50+100?", run_config=confiq)
print(result.final_output)
