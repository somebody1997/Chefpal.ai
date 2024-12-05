import streamlit as st

# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed")

hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {
            display: none;  /* 隱藏整個 Sidebar */
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Styling
st.markdown("""
    <style>
        .stApp {
            background-color: #F5E3C2;
        }
        .block-container {
            padding: 2rem 3rem;
          
            max-width: 1400px;
        }
        h1 {
            color: #3b302a;
            text-align: center;
            font-size: 3rem;
            margin-bottom: 3rem;
        
        }
        h2 {
            color: #3b302a;
            font-size: 2rem;
            margin-bottom: 2rem;
       
        }
            
        /* Remove link blue color and underline */
        a {
            color: inherit !important;
            text-decoration: none !important;
        }
        
        /* Remove visited link color */
        a:visited {
            color: inherit !important;
        }
        
        /* Remove hover effects */
        a:hover {
            color: #BE3455 !important;
            text-decoration: none !important;
            transition: color 0.3s ease;
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
    st.markdown("<h2 class='site-title'><a target='_self' href='frontend' id='my-link'>Chefpal.ai</a></h2>", unsafe_allow_html=True)


recipe_title = "Ackee and Saltfish"
ingredients_content = """
- 1 tbsp vegetable oil <br>
- 2 onions**, thinly sliced <br>
- 3 tbsp finely crushed garlic <br>
- Pinch of thyme leaves <br>
- 1 tsp Scotch bonnet chilli <br>
- ½ green pepper**, finely chopped <br>
- ½ red pepper**, finely chopped <br>
- 1 tomato**, finely chopped <br>
- 240g boiled salt cod <br>
- 200g tinned ackee
"""
methods_content = """
1. Preheat oven to **220°C/200°C Fan/Gas 7**<br>
2. Mix peppers, onions, thyme, garlic, chillies with oil. Roast 20–25 minutes<br>
3. Boil vinegar and sugar with water. Add roasted vegetables to pickle<br>
4. Sweat onions and garlic in oil (5 mins). Add thyme, Scotch bonnet (10 mins)<br>
5. Add remaining vegetables, cook on low heat<br>
6. Gently stir in saltfish and ackee<br>
7. Serve warm with optional boiled eggs and avocado
"""


# Title
recipe_title_col, recipe_reload = st.columns([2.5,9])    
with recipe_title_col:
    st.markdown(f"<h2>{recipe_title}</h2>", unsafe_allow_html=True)     

with recipe_reload:
    if st.button("🔄"):
        st.session_state.clear()
        st.rerun()

# Main container with fixed height
with st.container():
    # Create three columns: ingredients | divider | methods
    col1, col2, col3, col4 = st.columns([6,1, 7,1])

    with col1:
        with st.container():
            st.markdown("<h3>Ingredients</h3>", unsafe_allow_html=True)
            st.markdown(f"""
                    {ingredients_content}
            """, unsafe_allow_html=True)
    
    # Ingredients Section
    with col2:
        st.write(' ')
    
    # Methods Section
    with col3:
        with st.container():
            st.markdown("<h3>Method</h3>", unsafe_allow_html=True)
            st.markdown(f"""
                    {methods_content}
            """, unsafe_allow_html=True)

    with col4:
        st.write(' ')


st.markdown("""
    <h3 style='text-align:center; padding: 20px; padding-top: 200px ;'>Ask again</h3>
""", unsafe_allow_html=True)
with st.container():
    col1, col_input, col_submit, col4 = st.columns([5,8, 2,3])  # [image upload, input, submit]
    with col1:
        st.write(' ')
    with col_input:
        input_text = st.text_input("", 
                                placeholder="Message Chefpal",
                                label_visibility="collapsed",
                                max_chars=100)

    with col_submit:
        submit_button = st.button("➤")

    with col4:
        st.write(' ')
