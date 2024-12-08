import streamlit as st

def app():

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

            h1 {
                color: #3b302a;
                text-align: center;
                margin-bottom: 3rem !important;
            
            }
            h2 {
                color: #3b302a;
                font-size: 2rem !important;
                margin-bottom: 2rem;
        
            }
                
            .content-text {
                font-size: 1.1rem !important;
                line-height: 1.8;
            }
            
            .site-title{
                text-decoration: underline;
                color: #3b302a;
                font-size: 1.8rem; 
            }
            
            /* Align submit button */
            .stButton button {
                margin-top: 0 !important;
                height: 38px !important;
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


    if "recipe_title" not in st.session_state:
        st.session_state["recipe_title"] = "Ackee and Saltfish"

    if "ingredients_content" not in st.session_state:
        st.session_state["ingredients_content"] = """
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
    if "methods_content" not in st.session_state:
        st.session_state["methods_content"] = """
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
        st.markdown(f"<h2>{st.session_state['recipe_title']}</h2>", unsafe_allow_html=True)     


    # Main container with fixed height
    with st.container():
        # Create three columns: ingredients | divider | methods
        col1, col2, col3, col4 = st.columns([6,1, 7,1])

        with col1:
            with st.container():
                st.markdown("<h3>Ingredients</h3>", unsafe_allow_html=True)
                st.markdown(f"""
                        {st.session_state['ingredients_content']}
                """, unsafe_allow_html=True)
        
        # Ingredients Section
        with col2:
            st.write(' ')
        
        # Methods Section
        with col3:
            with st.container():
                st.markdown("<h3>Method</h3>", unsafe_allow_html=True)
                st.markdown(f"""
                        {st.session_state['methods_content']}
                """, unsafe_allow_html=True)

        with col4:
            st.write(' ')


    st.markdown("""
        <h3 style='text-align:center; padding: 20px; padding-top: 50px ;'>Ask again</h3>
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

