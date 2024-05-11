# Typing imports:

from typing import Final
from numpy import float64
from numpy.typing import NDArray

# Definition of Scalar en Tensor types:

Scalar: Final[type] = float64
Tensor: Final[type] = NDArray[Scalar]
