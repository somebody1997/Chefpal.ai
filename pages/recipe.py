import streamlit as st


st.markdown("""
       <style>
        .stApp {
            background-color: #F5E3C2 !important;
        }
            
        .block-container {
            padding: 2rem 3rem;
            font-family: 'Arial', sans-serif;
            max-width: 1200px !important;  /* Increased max-width */
        }
        h1 {
            color: #3b302a;
            text-align: center;
            font-size: 2.5rem;
        }
        h2 {
            color: #3b302a;
            font-size: 1.8rem;
            border-bottom: 2px solid #3b302a;
            padding-bottom: 0.5rem;
        }
        .ingredients {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            width: 100%;
        }
        .methods {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            margin: 1rem 0;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)


# Sample dynamic content fetched or generated
recipe_title = "Ackee and Saltfish"
ingredients_content = """
- **1 tbsp vegetable oil** <br>
- ** 2 onions **, thinly sliced <br>
- **3 tbsp finely crushed garlic** <br>
- Pinch of thyme leaves <br>
- **1 tsp finely chopped Scotch bonnet chilli** <br>
- **½ green pepper**, finely chopped <br>
- **½ red pepper**, finely chopped <br>
- **1 tomato**, finely chopped <br>
- **240g boiled salt cod**, broken into flakes <br>
- **200g tinned ackee**, drained and left whole 
"""

methods_content = """
- **240g boiled salt cod**, broken into flakes <br>
1. Preheat the oven to **220°C/200°C Fan/Gas 7**. Mix the peppers, onions, thyme, garlic, and chillies with oil. Roast for 20–25 minutes. <br>
2. Boil vinegar and sugar with water in a saucepan. Add roasted peppers and onions. Set aside to pickle. <br>
3. In a frying pan, sweat onions and garlic in oil for 5 minutes. Add thyme, Scotch bonnet, and cook for another 10 minutes. Add the remaining vegetables and cook over low heat.<br>
4. Stir in the saltfish and ackee gently. <br>
5. Serve warm, optionally with boiled eggs and avocado.
"""

# Title
st.markdown(f"<h1>{recipe_title}</h1>", unsafe_allow_html=True)


# Layout with columns
col1, col2 = st.columns([6,6])

# Ingredients Section
with col1:
    st.markdown("<h2>Ingredients</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='ingredients'>{ingredients_content}</div>", unsafe_allow_html=True)

# Methods Section
with col2:
    st.markdown("<h2>Method</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='methods'>{methods_content}</div>", unsafe_allow_html=True)



