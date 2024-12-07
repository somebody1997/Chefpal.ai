import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] div[data-testid="column"]:first-child .logo_button button {
                /* Reset default button styles */
                padding-top: 2 rem !important;
                border: none;
                background: none;
                
                /* Text styling */
                color: #3E3E3E;
                font-size: 3.5rem !important;
                font-weight: 600;
                
                /* Layout */
                height: 5rem;  /* Increased to fit larger text */
                width: auto;
                min-width: 240px;
                margin-bottom: 2rem;
                margin-left: -2rem;
                line-height: 1.2;
                cursor: pointer;
                text-align: left;
            }
                    
            div[data-testid="stHorizontalBlock"] div[data-testid="column"]:has(p:contains("Chefpal.ai")) .stButton button p {
                font-size: 3.5rem !important;
                padding-top: 77px;
            }

            div[data-testid="stHorizontalBlock"] div[data-testid="column"]:first-child .stButton button:hover {
                background: none;
                color: #3b302a;
            }

            div[data-testid="stHorizontalBlock"] div[data-testid="column"]:first-child .stButton button:hover {
                color: #BE3455;  /* Color changes on hover */
                background: none;
            }
        </style>
        """, unsafe_allow_html=True)

        # Then add the CSS with specific targeting
        # st.markdown("""
        #     <style>
        #     .element-container:has(#button-homepage) + div button {
        #         /* Reset default button styles */
        #         padding-top: 2rem !important;
        #         border: none;
        #         background: none;
                
        #         /* Text styling */
        #         color: #3E3E3E;
        #         font-size: 560px !important;
        #         font-weight: 600;
                
        #         /* Layout */
        #         height: 5rem;
        #         width: auto;
        #         min-width: 240px;
        #         margin-bottom: 2rem;
        #         margin-left: -2rem;
        #         line-height: 1.2;
        #         cursor: pointer;
        #         text-align: left;
        #         transition: all 0.2s ease;
        #     }

        #     .element-container:has(#button-homepage) + div button:hover {
        #         color: #BE3455;
        #         background: none;
        #     }
                    
        #     </style>
        # """, unsafe_allow_html=True)
        
        
        if "current_app" not in st.session_state:
            # Default to the first added app if none selected
            st.session_state["current_app"] = self.apps[0]["title"]

        # Add a common top navigation here
        col_logo, col_reload = st.columns([2,6])
        with col_logo:
        #This button now appears on all pages
            #st.markdown(f'<span id="button-homepage"></span>', unsafe_allow_html=True)
            logo_button = st.button("Chefpal.ai")
            if logo_button:
                st.session_state["current_app"] = "Searchbar"
                st.experimental_rerun()

        
        # Identify the currently selected app and run it
        current_app_title = st.session_state["current_app"]
        for app in self.apps:
            if app["title"] == current_app_title:
                app["function"]()
                break