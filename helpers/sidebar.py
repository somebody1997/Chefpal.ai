import streamlit as st


def show() -> None:
	with st.sidebar:
		st.markdown(f"""
			<a href="/" style="color:black;text-decoration: none;">
				<div style="display:table;margin-top:-16rem;margin-left:0%;">
					<img src="" width="30"><span>CHEFAI</span>
					<span style="font-size: 0.8em; color: black">&nbsp;&nbsp;v0.1.0</span>
					<br>
					
				</div>
			</a>
			<br>
				""", unsafe_allow_html=True)

		reload_button = st.button("↪︎  Reset Page")
		# if reload_button:
		# 	st.session_state.clear()
		# 	st.experimental_rerun()

