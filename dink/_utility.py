# Typing imports:

from typing import final, Self
from types import GenericAlias

# Utility imports:

from dataclasses import dataclass


# Definitions of namespace utility classes:

class NamespaceMeta(type):
    """ TODO """

    @final
    def __call__(cls) -> None:
        raise NotImplementedError(
            f"Namespace '{cls.__name__}' cannot be constructed."
        )


class Namespace(metaclass = NamespaceMeta):
    pass


class ConstantsNamespaceMeta(NamespaceMeta):
    """ TODO """

    @final
    def __setattr__(cls, *_) -> None:
        raise NotImplementedError(
            f"Namespace '{cls.__name__}' is read-only."
        )

    @final
    def __delattr__(cls, *_) -> None:
        raise NotImplementedError(
            f"Namespace '{cls.__name__}' is read-only."
        )


class ConstantsNamespace(metaclass = ConstantsNamespaceMeta):
    pass


# Definition of the abstract child class utility class:

class AbstractBaseClassMeta(type):
    """ TODO """

    @dataclass(frozen = True)
    class _Attribute:
        """ TODO """

        _name: str
        _type: type

        def __eq__(self, other: Self) -> bool:
            return self._name == other._name  # TODO ~ Implement type check.

        def __hash__(self) -> int:
            return hash(self._name)

    def __call__(cls, *args, **kwargs):
        """ TODO """

        if len(cls.__unresolved_attributes__) > 0:
            raise TypeError(
                f"Instance of abstract base class '{cls.__name__}' could not "
                f"be created since all abstract attributes of this class have "
                f"not been implemented."
            )

        return super(AbstractBaseClassMeta, cls).__call__(
            cls, args, kwargs
        )

    @property
    def __abstract_bases__(cls) -> frozenset[Self]:
        return frozenset(
            filter(
                lambda base: base.__class__ is AbstractBaseClassMeta,
                cls.__bases__
            )
        )

    @__abstract_bases__.setter
    def __abstract_bases__(cls, _: frozenset) -> None:
        raise NotImplemented

    @__abstract_bases__.deleter
    def __abstract_bases__(cls) -> None:
        raise NotImplemented

    @property
    def __required_attributes__(cls) -> frozenset[_Attribute]:
        _new_attributes: frozenset[cls._Attribute] = frozenset(
            map(
                lambda item: cls._Attribute(item[0], item[1].__args__[0]),
                filter(
                    lambda annotation: annotation[1].__dict__.get(
                        "__origin__"
                    ) is Abstract,
                    cls.__dict__["__annotations__"].items()
                )
            )
        ) if cls.__dict__.get("__annotations__") is not None else set()
        return _new_attributes.union(
            *map(
                lambda base: base.__unresolved_attributes__,
                cls.__abstract_bases__
            )
        )

    @__required_attributes__.setter
    def __required_attributes__(cls, _: frozenset) -> None:
        raise NotImplemented

    @__required_attributes__.deleter
    def __required_attributes__(cls) -> None:
        raise NotImplemented

    @property
    def __resolved_attributes__(cls) -> frozenset[_Attribute]:
        return frozenset(
            map(
                lambda item: cls._Attribute(item[0], type(item[1])),
                cls.__dict__.items()
            )
        )

    @__resolved_attributes__.setter
    def __resolved_attributes__(cls, _: frozenset) -> None:
        raise NotImplemented

    @__resolved_attributes__.deleter
    def __resolved_attributes__(cls) -> None:
        raise NotImplemented

    @property
    def __unresolved_attributes__(cls) -> frozenset[_Attribute]:
        return cls.__required_attributes__.difference(
            cls.__resolved_attributes__
        )

    @__unresolved_attributes__.setter
    def __unresolved_attributes__(cls, _: frozenset) -> None:
        raise NotImplemented

    @__unresolved_attributes__.deleter
    def __unresolved_attributes__(cls) -> None:
        raise NotImplemented


class AbstractBaseClass(metaclass = AbstractBaseClassMeta):
    """ TODO """


class Abstract[T](GenericAlias):
    pass


"""
Pseudo code:

1. Resolve base classes.
2. Collect required methods from the base classes.
    -- required = Union of abstract bases' unresolved and newly added.
3. Collect resolved methods from own class.
    -- resolved = Intersection of required and locally implemented.
4. Calculate unresolved methods from required and resolved.
    -- Difference of required and locally implemented.

"""
