import streamlit as st
import json
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
        st.session_state["recipe_title"] = st.session_state.recipe_data.get('recipe_name', '')

    if "ingredients_content" not in st.session_state:
        st.session_state["ingredients_content"] = st.session_state.recipe_data.get('ingredients', '')
    if "methods_content" not in st.session_state:
        st.session_state["methods_content"] = st.session_state.recipe_data.get('instructions', '')


    # Title
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

