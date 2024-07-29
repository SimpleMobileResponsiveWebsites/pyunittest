import pytest
import streamlit as st
from streamlit.testing import TestCase
from app import main


class TestStreamlitApp(TestCase):

    def setUp(self):
        # Setup any necessary state here
        self.app = main

    def test_app_title(self):
        # Run the Streamlit app
        self.app()

        # Check the app title
        st.markdown("### Test Streamlit App")
        assert st.session_state.title == "My Streamlit App"

    def test_button_click(self):
        # Run the Streamlit app
        self.app()

        # Simulate a button click
        st.button("Click me")

        # Check the button click response
        assert st.session_state.button_clicked == True

    # Add more test cases as needed


if __name__ == "__main__":
    pytest.main()


#streamlit==1.12.0
#pytest==7.1.2

# To run your tests, navigate to the directory containing test_app.py and run:
# pytest
