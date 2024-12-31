from Tool import SearchTool, Tool
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
load_dotenv()


class Agent:
    def __init__(self):
        self.tools=[]
        self.memory=[]
        self.max_memory=10

    def add_tool(self,tool:Tool):
        self.tools.append(tool)

    def json_parser(self, input_string):
        try:
            # Remove code block markers if present
            if '```json' in input_string:
                input_string = input_string.split('```json')[1]
            if '```' in input_string:
                input_string = input_string.replace('```', '')

            # Parse JSON
            return json.loads(input_string.strip())
        except json.JSONDecodeError as e:
            print(f"Debug - Response text: {input_string}")
            return {"action": "respond_to_user", "args": "Error processing response. Please try again."}

    def process_input(self,user_input):
        self.memory.append(f"User: {user_input}")
        self.memory = self.memory[-self.max_memory:]
        context = '\n'.join(self.memory)
        tools_description = '\n'.join([f"-{tool.name()}:{tool.description}" for tool in self.tools])

        prompt = f"""
        Context:
        {context}

        Tools Available:
        {tools_description}

        Instruction:
        Based on the user's input and the provided context, respond by constructing a JSON object in the following format:
        {{
            "action": "<tool_name or respond_to_user>",
            "args": "<tool arguments or response to user>"
        }}

        Guidelines:
        1. Always utilize the appropriate tool before directly responding to the user.
        2. If the tool's output is required to construct your response, ensure it is incorporated accurately.
        3. Select "respond_to_user" as the action only if no tool usage is necessary to address the user's query.
        """

        response = self.query_llm(prompt)
        self.memory.append(f"Agent:{response}")
        response_dict = self.json_parser(response)

        for tool in self.tools:
            if tool.name().lower() in response_dict['action'].lower():
                print(response_dict['action'])
                print(response_dict['args'])
                return tool.use(response_dict['args'])
        return response_dict


    def query_llm(self, prompt):
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        model = genai.GenerativeModel("gemini-2.0-flash-exp")
        response = model.generate_content(prompt)
        return response.text

    def run(self):
        print("LLM Agent: Hello! How can I assist you Today?")
        user_input=input("User: ")
        while True:
            if user_input.lower() in ['exit','bye','close']:
                print("see you later")
                break
            response = self.process_input(user_input)
            if isinstance(response, dict) and response['action']=='respond_to_user':
                print("Response from agent: ", response['args'])
                user_input=input("User: ")
            else:

                user_input=response

