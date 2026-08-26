from typing import Protocol

class Predictor(Protocol):
    def predict(self, data: float) -> float:
        ...

class ConstantPredictor:
    def predict(self, x: float) -> float:
        return 42.0

class LinearPredictor:
    def __init__(self, slope: float) -> None:
        self.slope = slope
    
    def predict(self, x: float) -> float:
        return self.slope * x

def run_prediction(model: Predictor, x: float) -> float:
    return model.predict(x)