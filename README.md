# Recipe Suggestion Web App

## 📖 Overview
This project is a user-friendly web application designed to suggest recipes based on the contents of a user's fridge. Users can either upload an image of their fridge or input a list of ingredients, and the app will provide recipe suggestions and cooking instructions.

---

## 🌟 Features
- **Image Recognition:** Automatically identifies ingredients from uploaded images.
- **Recipe Suggestions:** Generates personalized recipes based on provided ingredients.
- **Multi-language Support:** Accessible to a diverse user base with multi-language capabilities.
- **Error Handling:** Clear error messages for user inputs and system errors.

---

## 🔧 Technologies Used
| Component                 | Technology                      |
|---------------------------|----------------------------------|
| **Web Application**       | Streamlit                      |
| **Image Recognition**     | TensorFlow Lite or Google Cloud Vision API |
| **Recipe Generator**      | OpenAI's GPT-4 API             |
| **API Integration**       | RESTful API principles          |
| **Programming Language**  | Python                         |
| **Testing Framework**     | Pytest                         |
| **Version Control**       | Git/GitHub                     |

---

## 🏗️ Architecture
### 1. **Web Application**
   - Built using Streamlit, integrating both frontend and backend in one application.
   - Users can upload images or input ingredient lists directly.

### 2. **Image Recognition Component**
   - Processes uploaded images to identify ingredients.
   - Utilizes TensorFlow Lite for on-device recognition or Google Cloud Vision API for cloud-based services.

### 3. **Recipe Suggestion Component**
   - Leverages OpenAI's GPT-4 API for generating advanced and personalized recipes.

### 4. **API Integration Layer**
   - Handles communication between the app and external APIs for image recognition and language processing.

---

## 🧑‍💻 Developer Guidelines
### Code Standards
- **Variables & Functions:** Use `snake_case`.
- **Classes:** Use `PascalCase`.
- **Constants:** Use `ALL_UPPERCASE`.

### Testing
- Aim for 80%+ code coverage.
- Use `pytest` for unit testing.
- Include detailed documentation for each test.

### Modularity
- Follow the Single Responsibility Principle.
- Ensure decoupled components for easy maintenance.

### Logging & Error Handling
- Log key events using Python’s `logging` module.
- Provide clear error messages for debugging and user feedback.
---
## 🌐 Accessibility
- **User-Friendly Interface:** Simple and intuitive navigation.
- **Error Messages:** Meaningful guidance for incorrect inputs.
- **Integration Challenges:** Efforts to mitigate dependency issues on external APIs.
---
## 🚀 Known Challenges
1. **Integration Challenges:** Combining various APIs and technologies.
2. **API Rate Limits:** Usage constraints of external APIs like GPT-4 and Google Cloud Vision.
3. **Learning Curve:** Proficiency in new tools may require time.
4. **Dependency on External Services:** Risk if APIs experience downtime or changes.
---
## 💡 Future Enhancements
- **Offline Mode:** Incorporate offline image recognition using TensorFlow Lite.
- **Expanded Recipe Database:** Add a custom database for more diverse suggestions.
- **User Preferences:** Tailor recipes based on dietary restrictions or cuisine preferences.
---
# Run Application and Unit testing

## Prerequisites

- Python 3.8+
- pip package manager
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/recipe-generator.git
cd recipe-generator
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```
## Run Application
```
streamlit run frontend.py
```
## Running Tests

The project includes a comprehensive test suite using pytest. To run the tests:

```bash

# Run specific test file
cd server
pytest test_recipe_generator.py


```

### Test Coverage

The test suite includes:
- Unit tests for core functionality
- Integration tests for full system flow
- Parametrized tests for various input scenarios
- Mock tests for external API calls

### Current Test Status

All tests are currently passing. The test suite covers:
- Recipe generator initialization
- Recipe generation with various inputs
- Graph visualization
- Invalid input handling
- Integration testing
- Graph structure validation

## Error Handling

The system includes comprehensive error handling for:
- Invalid inputs
- API failures
- Memory system errors
- Graph visualization issues

## Acknowledgments

- OpenAI for ChatGPT API
- LangChain for the graph framework
- All contributors and testers


# Use Case Description
```
Use Case: Generate a Customized Recipe
1. Preconditions
   - User has accessed the Chefpal.ai web application
   - User has ingredients in mind

2. Main Flow
   User inputs available ingredients [S1]. User selects desired cooking style [S2]. System generates a customized recipe [S3].

3. Subflows
   [S1] User enters ingredients in the text input field (e.g., "chicken, mushroom, tomato")
   [S2] User selects cooking style from dropdown menu (e.g., "Thai", "Italian", "Chinese")
   [S3] System displays complete recipe with title, ingredients list, and cooking steps

4. Alternative Flows
   [E1] Empty ingredient input: System prompts user to enter ingredients
   [E2] API failure: System shows error message and asks user to try again
```

### Test Execution Steps
1. Open Chefpal.ai web application
2. Enter "chicken, mushroom, tomato" in the ingredients input field
3. Select "Thai" from the cooking style dropdown
4. Click "Generate Recipe" button

### Expected Output
The system should generate a complete recipe in the following format:

```
Thai Basil Chicken with Mushrooms and Tomatoes

Ingredients:
- 300g chicken, sliced
- 2 cups mushrooms, sliced
- 2 tomatoes, wedged
- 3 cloves garlic, minced
- 2 tbsp fish sauce
- 1 cup Thai basil leaves
- 2 tbsp cooking oil

Instructions:
1. Heat oil in a wok over medium-high heat
2. Add garlic and stir-fry until fragrant
3. Add chicken and cook until nearly done
4. Add mushrooms and tomatoes, stir-fry for 3 minutes
5. Season with fish sauce
6. Add Thai basil leaves
7. Serve hot with steamed rice
```

### Output Validation Criteria
1. Recipe Title:
   - Should include main ingredients
   - Should reflect selected cuisine type

2. Ingredients List:
   - Must include all user-input ingredients
   - Should include appropriate seasonings for selected cuisine
   - Quantities should be clearly specified

3. Cooking Instructions:
   - Should be clear and sequential
   - Must use all listed ingredients
   - Should reflect cooking methods appropriate for the cuisine type
   - Must be logically ordered

