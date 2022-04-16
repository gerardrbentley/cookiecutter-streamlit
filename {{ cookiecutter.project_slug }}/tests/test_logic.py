# from streamlit_app import do_something


def do_something(x):
    return x + 5


class TestLogic:
    """Test backend logic"""

    def test_something(self):
        result = do_something(42)
        assert result == 47
