import numpy as np


def preprocess(image: np.ndarray, size: tuple[int, int] = (224, 224)) -> np.ndarray:
    import cv2

    resized = cv2.resize(image, size)
    normalized = resized.astype(np.float32) / 255.0
    chw = np.transpose(normalized, (2, 0, 1))  # Change from HWC to CHW format
    return chw
