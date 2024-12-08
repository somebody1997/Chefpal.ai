import streamlit as st
from service.recipe_generator import RecipeGenerator
import json
def app():
    
    recipe_gen = RecipeGenerator()
    # set the page and title
    # st.set_page_config(page_title="Chefpal.ai", layout="wide")
    hide_sidebar_style = """
        <style>
            [data-testid="stSidebar"] {
                display: none;  /* 隱藏整個 Sidebar */
            }
        </style>
    """
    st.markdown(hide_sidebar_style, unsafe_allow_html=True)


    # declare menu type
    cuisine_options = ["Chinese", "Thai", "Japanese", "American", "French", "Italy"]
    
    # initiate
    if "selected_cuisine" not in st.session_state:
        st.session_state.selected_cuisine = None  

    # topic
    st.markdown(
        """
        <style>
            .stApp {
                background-color: #F5E3C2;
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
            .element-container:has(style){
                display: none;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Define colors
    button_colors = ['#B44D4D', '#A3C585', '#23558e', '#FFA500', '#8B5A83', '#795548']

    # Generate dynamic CSS for each button
    button_css = ""
    for i, color in enumerate(button_colors):
        button_css += f"""
        .element-container:has(#button-after-{i}) + div button {{
            background-color: transparent;
            color: {color};
            border: none;
            transition: all 0.2s ease;
            font-size: 1.2rem !important;
        }}

        .element-container:has(#button-after-{i}) + div button:focus {{
            box-shadow: 0 0 3px rgba({color}, 0.3) !important;
            border: 0.8px solid {color} !important;
            background-color: transparent !important;
        }}
        
        .element-container:has(#button-after-{i}) + div button:active {{
            background-color: transparent !important;
            border: 0.5px solid {color} !important;
            opacity: 0.8;
        }}
        """

    # Add CSS to page
    st.markdown(f"""
        <style>
            {button_css}
        </style>
    """, unsafe_allow_html=True)


    with st.container():
        col1, col2, col3 = st.columns([7,6,3])
        with col1:
            st.write(' ')

        with col2:
            st.markdown("### What's in your fridge?")

        with col3:
            st.write(' ')

    with st.container():
        col1, col_input, col_submit, col4 = st.columns([5,8, 2,3]) 
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

    if submit_button:
        st.session_state["input_text"] = input_text
        # Redirect to recipe.py

        # sent model input
        # st.session_state.selected_cuisine
        # Add spinner while generating recipe
        # Center the spinner
        with st.container():
            left_col, center_col, right_col = st.columns([1, 2, 1])
            with center_col:
                # Add custom CSS for vertical centering
                st.markdown("""
                    <style>
                        div.stSpinner > div {
                            text-align: center;
                            min-height: 10vh;  /* Reduced from 50vh */
                            display: flex;
                            align-items: center;
                            justify-content: center;
                        }
                    </style>
                """, unsafe_allow_html=True)
                
                with st.spinner('Creating your recipe...'):
                    st.session_state.recipe_detail = recipe_gen.generate(st.session_state.input_text, st.session_state.selected_cuisine)
                    st.session_state.recipe_data = json.loads(st.session_state.recipe_detail)
                    st.session_state["current_app"] = "Recipe"
                    st.rerun()
    

    with st.container():
        col1, col2, col3 = st.columns([3,8, 2])

        with col1:
            st.write(' ')

        with col2:
            # st.columns adjust horizontal
            columns = st.columns(len(cuisine_options))
            for idx, cuisine in enumerate(cuisine_options):
                with columns[idx]:
                    # button action
                    # st.markdown(f'<span id="button-after" class="color-{idx}"></span>', unsafe_allow_html=True)
                    st.markdown(f'<span id="button-after-{idx}"></span>', unsafe_allow_html=True)
                    if st.button(cuisine, key=cuisine, use_container_width=True):
                        if st.session_state.selected_cuisine == cuisine:
                            st.session_state.selected_cuisine = "random"
                        else:
                            st.session_state.selected_cuisine = cuisine
        with col3:
            st.write(' ')

    # with st.container():
    #     # show the menu type selected
    #     st.markdown("### Current Selection:")
    #     if st.session_state.selected_cuisine:
    #         st.write(f"Selected Cuisine: {st.session_state.selected_cuisine}")
    #     else:
    #         st.write("No cuisine selected.")