import numpy as np


class CameraService:
    def __init__(self, width: int = 640, height: int = 480) -> None:
        self.width = width
        self.height = height

    def capture(self) -> np.ndarray:
        # Placeholder: return a blank image for now
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        return frame



# tweak 16 at 2025-09-24 20:37:42

# tweak 35 at 2025-09-24 20:37:51







