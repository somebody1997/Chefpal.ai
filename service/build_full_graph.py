from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from tool_tavily_search import load_tavily_search_tool
from agent_backend import State, BasicToolNode, route_tools, plot_agent_schema
from dotenv import load_dotenv

load_dotenv()


import json
from langgraph.checkpoint import MemorySaver
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, List, Optional

from langchain_core.messages import HumanMessage, AIMessage

class State(TypedDict):
    topic: Optional[str]
    messages: List[dict]
    recipe: Optional[str]
    structured_output: Optional[dict]

def build_sequential_graph():
    """
    Builds a sequential graph with CLI input support
    """
    # Initialize language models
    gpt4o = ChatOpenAI(model="gpt-4o", temperature=0.7)
    gpt35 = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

    graph_builder = StateGraph(State)

    def recipe_generation_node(state: State):
        """
        First node: Generate a recipe using GPT-4o
        """
        topic = state.get('topic', 'random cuisine')
        prompt = f"Generate a unique and creative recipe inspired by {topic}"
        
        # Generate recipe
        recipe = gpt4o.invoke(prompt).content
        
        # Append messages
        new_messages = state['messages'] + [
            HumanMessage(content=prompt),
            AIMessage(content=recipe)
        ]
        
        return {
            "messages": new_messages,
            "recipe": recipe
        }

    def structured_output_node(state: State):
        """
        Second node: Generate structured output from the recipe using GPT-3.5
        """
        prompt = f"Convert this recipe into a structured JSON with keys: name, ingredients (list), steps (list), difficulty, prep_time, cook_time:\n{state['recipe']}"
        
        # Generate structured output
        structured_output = json.loads(gpt35.invoke(prompt).content)
        
        # Append messages
        new_messages = state['messages'] + [
            HumanMessage(content=prompt),
            AIMessage(content=json.dumps(structured_output))
        ]
        
        return {
            "messages": new_messages,
            "structured_output": structured_output
        }

    # Add nodes to the graph
    graph_builder.add_node("recipe_generation", recipe_generation_node)
    graph_builder.add_node("structured_output", structured_output_node)

    # Define the sequential flow
    graph_builder.add_edge(START, "recipe_generation")
    graph_builder.add_edge("recipe_generation", "structured_output")
    graph_builder.add_edge("structured_output", END)

    # Compile the graph with memory saving
    memory = MemorySaver()
    graph = graph_builder.compile(checkpointer=memory)

    return graph

def main():
    # Create the graph
    sequential_graph = build_sequential_graph()

    # CLI Input
    print("Recipe Generation CLI")
    print("-" * 30)
    
    # Get topic from user
    topic = input("Enter a cuisine or food topic (or press Enter for random): ").strip()
    
    # Prepare initial state
    initial_state = {
        "topic": topic if topic else None,
        "messages": [],
        "recipe": None,
        "structured_output": None
    }

    # Run the graph
    result = sequential_graph.invoke(initial_state)

    # Print results
    print("\n=== RECIPE ===")
    print(result.get('recipe', 'No recipe generated'))
    
    print("\n=== STRUCTURED OUTPUT ===")
    print(json.dumps(result.get('structured_output', {}), indent=2))

if __name__ == "__main__":
    main()