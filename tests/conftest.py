import pytest

from py_template.predictor import LinearPredictor


@pytest.fixture
def linear_model():
    return LinearPredictor(slope=2.0)
