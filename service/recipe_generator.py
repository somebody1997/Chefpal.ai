# recipe_generator.py
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.prompts import ChatPromptTemplate
from typing_extensions import TypedDict
from typing import Annotated
from IPython.display import Image, display
from dotenv import load_dotenv

load_dotenv()

class State(TypedDict):
    messages: Annotated[list, add_messages]
    cusine_type: Annotated[list, add_messages]
    user_input: str

class RecipeGenerator:
    def __init__(self):
        self.memory = MemorySaver()
        self.graph = self._build_graph()
        
    def _build_graph(self):
        # Define prompts and tools
        planner_prompt = ChatPromptTemplate.from_template(
            """
            Here is a list of ingredients: 
            {messages}

            Based on this list, create only one recipe in {cusine_type} style and make sure to clearly label: 
            - Recipe Name
            - Ingredients with specific quantities or weights
            - Cooking Instructions with step-by-step guide
            The recipe should be creative, easy to follow, and suitable for a home-cooked meal.
            """
        )

        tool = TavilySearchResults(max_results=2)
        tools = [tool]
        llm = ChatOpenAI(model="gpt-4o", temperature=0)
        llm_with_tools = llm.bind_tools(tools)

        planner = planner_prompt | llm_with_tools

        structure_prompt = ChatPromptTemplate.from_template(
            """
            Please convert the following recipe content into JSON format, including the following fields:
            - `recipe_name`
            - `instructions`
            - `ingredients`

            Each field's value should be formatted in Markdown. 
            Only return the value part of the JSON, and do not include the field names within the values. 
            For example, in the `instructions` field, start the guidance directly without "instructions:". 
            Similarly, in the `recipe_name` and `ingredients` fields, provide the content directly without including "recipe_name:" or "ingredients:" within their respective values.

            Recipe content:
            {messages}
            """
        )

        structure = structure_prompt | ChatOpenAI(
            model="gpt-4o", temperature=0
        )

        graph_builder = StateGraph(State)

        def generate_recipe(state: State):
            recipe_params = {
                "cusine_type": state["cusine_type"],
                "messages": state["messages"],
            }
            return {"messages": [planner.invoke(recipe_params)]}

        def structured_output(state: State):
            return {"messages": [structure.invoke(state["messages"])]}

        graph_builder.add_node("recipe", generate_recipe)
        graph_builder.add_node("structured", structured_output)

        graph_builder.add_edge(START, "recipe")
        graph_builder.add_edge("recipe", "structured")
        graph_builder.add_edge("structured", END)

        graph = graph_builder.compile(checkpointer=self.memory)
        return graph

    def generate(self, user_input, cusine_type):
        """Generate a recipe based on user input ingredients."""
        config = {"configurable": {"thread_id": "1"}}
        events = self.graph.invoke({"messages": user_input, "cusine_type": cusine_type}, config, stream_mode="values")
        return events['messages'][-1].content

    def display_graph(self):
        """Optional: Display the graph structure."""
        try:
            display(Image(self.graph.get_graph().draw_mermaid_png()))
        except Exception:
            pass

# Usage example:
if __name__ == "__main__":
    recipe_gen = RecipeGenerator()
    user_input = "Tomato, Mushroom, Green Bell Pepper, Onion, Garlic, Egg, Chicken, Cheese, Yogurt"
    response = recipe_gen.generate(user_input, cusine_type="Chinese")
    print(response)