# Typing imports:

from typing import Callable, Final
from ._numerics import Scalar, Tensor

# Numeric imports:

from numpy import sqrt
from numpy.random import uniform

# Utility imports:

from ._utility import ConstantsNamespace

# Initializer type definition:

Initializer: Final[type] = Callable[[int, int], Tensor]
""" TODO """


# Initializer function definitions:

def _xavier(inputs: int, outputs: int) -> Tensor:
    return uniform(
        low = -1.0 / sqrt(inputs),
        high = 1.0 / sqrt(inputs),
        size = (inputs, outputs)
    )


def _uniform(lower_bound: float, upper_bound: float) -> Initializer:
    return lambda inputs, outputs: uniform(
        low = lower_bound,
        high = upper_bound,
        size = (inputs, outputs)
    ).astype(Scalar)


class Initializers(ConstantsNamespace):
    """ TODO """

    XAVIER: Final[Initializer] = _xavier
    """ TODO """

    UNIFORM: Final[Callable[[float, float], Initializer]] = _uniform
    """ TODO """
