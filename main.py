from agent import Agent
from Tool import SearchTool
def main():
    agent = Agent()
    agent.add_tool(SearchTool())
    agent.run()

if __name__ == '__main__':
    main()