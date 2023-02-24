from typing import List, Dict
import numpy as np


class WasteDetector:
    def __init__(self, model_path: str, backend: str = "onnx") -> None:
        self.model_path = model_path
        self.backend = backend

    def detect(self, frame: np.ndarray) -> List[Dict]:
        # Placeholder: return empty detection list
        return []


