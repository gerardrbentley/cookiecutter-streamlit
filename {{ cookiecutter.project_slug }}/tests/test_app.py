import pytest
from seleniumbase import BaseCase


class VisualTest(BaseCase):
    @pytest.mark.e2e
    def test_app_runs(self):
        # automated visual regression testing
        # tests page has identical structure to baseline
        # https://github.com/seleniumbase/SeleniumBase/tree/master/examples/visual_testing
        self.open("http://localhost:8501")
        self.wait_for_element("[data-testid=stAppViewContainer]")
        self.assert_element("[data-testid=stAppViewContainer]")
        self.check_window(name="app_runs", level=3)
