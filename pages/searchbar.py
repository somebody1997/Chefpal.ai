import streamlit as st

st.markdown("""
       <style>
        .stApp {
            background-color: #F5E3C2 !important;
        }
    </style>
""", unsafe_allow_html=True)


# set the page and title
# st.set_page_config(page_title="Chefpal.ai", layout="centered")

# declare menu type
cuisine_options = ["Chinese", "Thai", "Japanese", "American", "French", "Italy"]

# initiate
if "selected_cuisine" not in st.session_state:
    st.session_state.selected_cuisine = None  

# topic
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #444;">Chefpal.ai</h1>
        
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("### What's in your fridge?")
col1, col2 = st.columns([4, 1])  # adjust the ratio for searchbar and submit button
with col1:
    input_text = st.text_input("", placeholder="Message Chefpal", label_visibility="collapsed")
with col2:
    submit_button = st.button("➤")

if submit_button:
    st.write(f"You entered: {input_text}")


st.markdown("### Choose a cuisine:")

# st.columns adjust horizontal
columns = st.columns(len(cuisine_options))
for idx, cuisine in enumerate(cuisine_options):
    with columns[idx]:
        # button action
        if st.button(cuisine, key=cuisine):
            if st.session_state.selected_cuisine == cuisine:
                st.session_state.selected_cuisine = None
            else:
                st.session_state.selected_cuisine = cuisine

# show the menu type selected
st.markdown("### Current Selection:")
if st.session_state.selected_cuisine:
    st.write(f"Selected Cuisine: {st.session_state.selected_cuisine}")
else:
    st.write("No cuisine selected.")
