import numpy as np
from numpy.typing import NDArray


def preprocess(
    image: NDArray[np.uint8], size: tuple[int, int] = (224, 224)
) -> NDArray[np.float32]:
    import cv2

    resized = cv2.resize(image, size)
    normalized = resized.astype(np.float32) / 255.0
    chw = np.transpose(normalized, (2, 0, 1))  # Change from HWC to CHW format
    return chw
