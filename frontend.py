import streamlit as st
from multiapps import MultiApp
from pages import searchbar, recipe

# Set page config once here, at the start
st.set_page_config(page_title="Chefpal.ai", layout="wide")

app = MultiApp()
app.add_app("Searchbar", searchbar.app)
app.add_app("Recipe", recipe.app)

app.run()