import streamlit as st

# Page config
st.set_page_config(layout="wide")

# Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #F5E3C2;
        }
        .block-container {
            padding: 2rem 3rem;
            font-family: 'Arial', sans-serif;
            max-width: 1400px;
        }
        h1 {
            color: #3b302a;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 3rem;
            font-family: 'Georgia', serif;
        }
        h2 {
            color: #3b302a;
            font-size: 2rem;
            margin-bottom: 2rem;
            font-family: 'Georgia', serif;
        }

        .divider-vertical {
            width: 2px;
            background-color: #3b302a;
            height: 100%;
            margin: auto;
        }
            
        .divider-vertical-line {
            border-left: 2px solid lightgray;
            height: 350px;
            margin: auto;
        }
            
        .content-text {
            font-size: 1.1rem;
            line-height: 1.8;
        }
        
        .site-title{
            text-decoration: underline;
            color: #3b302a;
            font-size: 1.8rem; 
        }
            
        [data-testid='stFileUploader'] {
           width: max-content;
           margin: 0 !important;
           padding: 0 !important;
        }
        [data-testid='stFileUploader'] section {
            padding: 0;
            float: left;
        }
        [data-testid='stFileUploader'] section > input + div {
            display: none;
        }
        [data-testid='stFileUploader'] section + div {
            float: right;
            padding-top: 0;
        }
        
        [data-testid="stFileUploader"] section {
            padding: 0 !important;
        }
        
                /* Align submit button */
        .stButton button {
            margin-top: 0 !important;
            height: 38px !important;
        }
        
        /* Container spacing */
        .block-container {
            padding-left: 0 !important;
            padding-right: 0 !important;
        }

        /* Remove default spacing */
        .stButton, .stTextInput {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .stTextInput {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Top navigation
col_logo, col_reload = st.columns([1,6])
with col_logo:
    st.markdown("<h2 class='site-title'>Chefpal.ai</h2>", unsafe_allow_html=True)



recipe_title = "Ackee and Saltfish"
ingredients_content = """
- **1 tbsp vegetable oil** <br>
- **2 onions**, thinly sliced <br>
- **3 tbsp finely crushed garlic** <br>
- Pinch of thyme leaves <br>
- **1 tsp Scotch bonnet chilli** <br>
- **½ green pepper**, finely chopped <br>
- **½ red pepper**, finely chopped <br>
- **1 tomato**, finely chopped <br>
- **240g boiled salt cod** <br>
- **200g tinned ackee**
"""
methods_content = """
1. Preheat oven to **220°C/200°C Fan/Gas 7**<br><br>
2. Mix peppers, onions, thyme, garlic, chillies with oil. Roast 20–25 minutes<br><br>
3. Boil vinegar and sugar with water. Add roasted vegetables to pickle<br><br>
4. Sweat onions and garlic in oil (5 mins). Add thyme, Scotch bonnet (10 mins)<br><br>
5. Add remaining vegetables, cook on low heat<br><br>
6. Gently stir in saltfish and ackee<br><br>
7. Serve warm with optional boiled eggs and avocado
"""


# Title
recipe_title_col, recipe_reload = st.columns([2,9])    
with recipe_title_col:
    st.markdown(f"<h3>{recipe_title}</h3>", unsafe_allow_html=True)     

with recipe_reload:
    if st.button("🔄"):
        st.session_state.clear()
        st.rerun()

# Main container with fixed height
with st.container():
    # Create three columns: ingredients | divider | methods
    col1, col2, col3 = st.columns([5, 0.5, 6])
    
    # Ingredients Section
    with col1:
        with st.container():
            st.markdown("<h2>Ingredients</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                    {ingredients_content}
            """, unsafe_allow_html=True)
    
    # Vertical Divider
    with col2:
        st.markdown("""
            <div class="divider-vertical-line"></div>
        """, unsafe_allow_html=True)
    
    # Methods Section
    with col3:
        with st.container():
            st.markdown("<h2>Method</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                    {methods_content}
            """, unsafe_allow_html=True)


st.markdown("""
    <h3 style=' padding: 20px; padding-top: 30px ;'>Ask again</h3>
""", unsafe_allow_html=True)
col_upload, col_input, col_submit = st.columns([0.6, 4, 2])  # [image upload, input, submit]

# with col_camera:
#     st.button("📸")

with col_upload:
    uploaded_file = st.file_uploader("", type=['png', 'jpg', 'jpeg'], 
                                   label_visibility="collapsed", 
                                   key="compact_uploader")

with col_input:
    input_text = st.text_input("", 
                              placeholder="Message Chefpal",
                              label_visibility="collapsed",
                              max_chars=100)

with col_submit:
    submit_button = st.button("➤")