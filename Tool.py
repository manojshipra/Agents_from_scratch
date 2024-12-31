import os

import requests
from abc import ABC, abstractmethod
from dotenv import load_dotenv
load_dotenv()

class Tool(ABC):
    @abstractmethod
    def name(self)->str:
        pass

    @abstractmethod
    def description(self)->str:
        pass

    @abstractmethod
    def use(self,*args,**kwargs):
        pass


class SearchTool(Tool):
    def name(self):
        return "Search Tool"

    def description(self):
        return "Provides web search results"

    def use(self,*args,**kwargs):
        api_key=os.getenv("API_KEY")
        search_engine_id=os.getenv("SEARCH_ENGINE_ID")
        base_url="https://www.googleapis.com/customsearch/v1"
        params={
            'key':api_key,
            'cx':search_engine_id,
            'q':args[0],
            **kwargs
        }
        response = requests.get(base_url,params=params)
        response.raise_for_status()
        data = response.json()['items']
        return f"The information retrieved from the web is {data}"



