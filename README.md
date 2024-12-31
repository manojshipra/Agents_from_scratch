# AI Agent with Google Search Integration
A Python-based AI agent that combines the power of Google's Gemini AI with custom search capabilities. The agent can understand user queries, utilize search tools when needed, and maintain conversation context through a memory system.

🌟 Features
  🤖 Integration with Google's Gemini AI
  🔍 Google Custom Search API Integration
  🧠 Memory System for Context Retention
  🛠️ Extensible Tool Architecture
  🔄 JSON-based Response Processing

# 🔧 Installation
#Clone the repository

#Navigate to the project directory
cd ai-search-agent

#Create virtual environment
python -m venv venv

#Activate virtual environment
#For Windows:
venv\Scripts\activate
#For Unix/MacOS:
source venv/bin/activate

#Install dependencies
pip install -r requirements.txt

# ⚙️ Configuration

Create a .env file in the project root:
API_KEY=your_google_custom_search_api_key
SEARCH_ENGINE_ID=your_google_custom_search_engine_id
GOOGLE_API_KEY=your_google_ai_api_key

# 🚀 Quick Start
from agent import Agent
from tool import SearchTool

#Initialize the agent
agent = Agent()

#Add search tool
search_tool = SearchTool()
agent.add_tool(search_tool)

#Run the agent
agent.run()

# 💡 Usage Examples
Basic Interaction
# Start the agent
agent = Agent()
agent.add_tool(SearchTool())
agent.run()

#Example interaction:
#Agent: Hello! How can I assist you Today?
#User: What's the latest news about Python programming?
#[Agent will use search tool to find and return relevant information]

# Custom Tool Creation
from tool import Tool

class CustomTool(Tool):
    def name(self):
        return "Custom Tool"

    def description(self):
        return "Description of your custom tool"

    def use(self, *args, **kwargs):
        # Implement your tool logic here
        pass

# 🛠️ How It Works

Initialization:

Agent is created with an empty tools list and memory system
Tools are added to the agent


Processing Flow:

User input is received
Context is maintained in memory
LLM processes input and determines action
Appropriate tool is used if needed
Response is formatted and returned


Tool Integration:

Tools must inherit from Tool abstract class
Each tool provides specific functionality
Agent manages tool selection and execution
