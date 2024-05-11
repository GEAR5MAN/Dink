# Typing imports:

from typing import Callable, Final
from ._numerics import Tensor

# Utility imports:

from dataclasses import dataclass, field
from ._utility import ConstantsNamespace

# Numeric imports:

from numpy import ones_like, clip, heaviside, exp


# Activation container definition:

@dataclass(frozen = True)
class Activation:
    """ TODO """

    call_function: Callable[[Tensor], Tensor] = field(kw_only = True)
    """ TODO """

    call_derivative: Callable[[Tensor], Tensor] = field(kw_only = True)
    """ TODO """


# Activation function and derivative definitions:

def _identity_function(x: Tensor) -> Tensor:
    return x


def _identity_derivative(x: Tensor) -> Tensor:
    return ones_like(x)


def _relu_function(x: Tensor) -> Tensor:
    return clip(x, 0.0, None)


def _relu_derivative(x: Tensor) -> Tensor:
    return heaviside(x, 0.0)


def _logistic_function(x: Tensor) -> Tensor:
    return 1.0 / (1.0 + exp(-x))


def _logistic_derivative(x: Tensor) -> Tensor:
    return exp(x) / (1.0 + exp(x)) ** 2.0


# Activation namespace class definition:

class Activations(ConstantsNamespace):
    """ Namespace class containing most standard activation functions. """

    IDENTITY: Final[Activation] = Activation(
        call_function = _identity_function,
        call_derivative = _identity_derivative
    )
    """ TODO """

    RELU: Final[Activation] = Activation(
        call_function = _relu_function,
        call_derivative = _relu_derivative
    )
    """ TODO """

    LOGISTIC: Final[Activation] = Activation(
        call_function = _logistic_function,
        call_derivative = _logistic_derivative
    )
    """ TODO """
