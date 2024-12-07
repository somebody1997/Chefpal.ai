import streamlit as st

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        st.markdown("""
            <style>
             /* Global styles for text elements */
            

            /* Logo button exception */
            .custom-logo-button-container button {
                font-size: 2rem !important;
                font-weight: bold !important;
            }
            </style>

        """, unsafe_allow_html=True)
        
        if "current_app" not in st.session_state:
            # Default to the first added app if none selected
            st.session_state["current_app"] = self.apps[0]["title"]

        # Add a common top navigation here
        # This button now appears on all pages
        # st.markdown(f'<span id="button-homepage"></span>', unsafe_allow_html=True)
        st.markdown('<div class="custom-logo-button-container">', unsafe_allow_html=True)
        logo_button = st.button("Chefpal.ai")
        st.markdown('</div>', unsafe_allow_html=True)

        if logo_button:
            st.session_state["current_app"] = "Searchbar"
            st.experimental_rerun()

        # Identify the currently selected app and run it
        current_app_title = st.session_state["current_app"]
        for app in self.apps:
            if app["title"] == current_app_title:
                app["function"]()
                break