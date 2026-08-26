from py_template.predictor import ConstantPredictor, LinearPredictor, run_prediction


def test_constant_predictor():
    model = ConstantPredictor()
    assert run_prediction(model, 5.0) == 42.0
    assert run_prediction(model, -3.0) == 42.0


def test_linear_predictor():
    model = LinearPredictor(slope=2.0)
    assert run_prediction(model, 3.0) == 6.0
    assert run_prediction(model, 0.0) == 0.0
