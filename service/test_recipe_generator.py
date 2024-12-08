import pytest
from recipe_generator import RecipeGenerator
from unittest.mock import Mock, patch
import json

@pytest.fixture
def recipe_generator():
    return RecipeGenerator()

def test_recipe_generator_initialization(recipe_generator):
    assert recipe_generator is not None
    assert recipe_generator.graph is not None
    assert recipe_generator.memory is not None

@pytest.mark.parametrize("user_input,cuisine_type", [
    ("Tomato, Onion, Garlic", "Italian"),
    ("Rice, Soy Sauce, Chicken", "Chinese"),
    ("Potato, Beef, Carrot", "American")
])
@patch('recipe_generator.ChatOpenAI')
def test_generate_recipe_with_different_inputs(mock_chat, recipe_generator, user_input, cuisine_type):
    mock_message = Mock()
    mock_message.content = {
        "recipe_name": "Test Recipe",
        "ingredients": ["ingredient 1", "ingredient 2"],
        "instructions": ["step 1", "step 2"]
    }

    mock_response = {
        'messages': [mock_message]
    }

    recipe_generator.graph.invoke = Mock(return_value=mock_response)
    
    response = recipe_generator.generate(user_input, cuisine_type)
    assert response is not None
    assert isinstance(response, (str, dict))
    
    if isinstance(response, str):
        try:
            json_response = json.loads(response)
            print(json_response)
        except json.JSONDecodeError:
            pytest.fail("Response string is not valid JSON")
            json_response =  {
                "recipe_name": "Wrong input",
                "ingredients": ["-"],
                "instructions": ["-"]
            }
    elif isinstance(response, dict):
        json_response = response
    else:
        pytest.fail("Response is neither a string nor a dict")
    
    assert 'recipe_name' in json_response
    assert 'ingredients' in json_response
    assert 'instructions' in json_response

def test_display_graph_success(recipe_generator):
    with patch('recipe_generator.display') as mock_display:
        with patch('recipe_generator.Image') as mock_image:
            recipe_generator.display_graph()
            mock_display.assert_called_once()



@pytest.mark.parametrize("invalid_input", [
    None,
    "",
    123,
    [],
])
def test_generate_with_invalid_inputs(recipe_generator, invalid_input):
    with pytest.raises(Exception):
        recipe_generator.generate(invalid_input, "Italian")

@pytest.mark.integration
def test_full_recipe_generation_flow():
    recipe_gen = RecipeGenerator()
    user_input = "Tomato, Mushroom, Green Bell Pepper"
    cuisine_type = "Italian"
    
    response = recipe_gen.generate(user_input, cuisine_type)
    
    assert isinstance(response, (str, dict))
    assert len(response) > 0

def test_graph_build_structure(recipe_generator):
    graph = recipe_generator._build_graph()
    assert graph is not None
    assert hasattr(graph, 'invoke')
    assert hasattr(graph, 'get_graph')