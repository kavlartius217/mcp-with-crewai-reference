from crewai import Agent,Task,Crew,Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters


server_params=StdioServerParameters(
    command="python3",
    args=["server/server.py"],
    env={"UV_PYTHON":"3.11",**os.environ}
)

mcp_adapter=MCPServerAdapter(server_params)

tools_list=mcp_adapter.tools

agent_1=Agent(
    role="math assistant",
    goal="Perform basic arithmetic operations",
    backstory="You are a math assistant that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.",
    tools=tools_list,
    verbose=True
)

task_1=Task(
    description="perform the mathematical operations based on the digits {a} and {b} entered by the user",
    expected_output="The result of the operation",
    agent=agent_1
)

crew=Crew(
    agents=[agent_1],
    tasks=[task_1],
    process=Process.sequential
)

response=crew.kickoff({
    "a":10,
    "b":5
})
print(response)
