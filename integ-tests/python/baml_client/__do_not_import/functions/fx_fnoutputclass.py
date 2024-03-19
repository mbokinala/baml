# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_testoutputclass import TestOutputClass
from ..types.partial.classes.cls_testoutputclass import PartialTestOutputClass
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IFnOutputClassOutput = TestOutputClass

@runtime_checkable
class IFnOutputClass(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        TestOutputClass
    """

    async def __call__(self, arg: str, /) -> TestOutputClass:
        ...

   

@runtime_checkable
class IFnOutputClassStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        arg: str

    Returns:
        AsyncStream[TestOutputClass, PartialTestOutputClass]
    """

    def __call__(self, arg: str, /) -> AsyncStream[TestOutputClass, PartialTestOutputClass]:
        ...
class IBAMLFnOutputClass(BaseBAMLFunction[TestOutputClass, PartialTestOutputClass]):
    def __init__(self) -> None:
        super().__init__(
            "FnOutputClass",
            IFnOutputClass,
            ["v1"],
        )

    async def __call__(self, *args, **kwargs) -> TestOutputClass:
        return await self.get_impl("v1").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[TestOutputClass, PartialTestOutputClass]:
        res = self.get_impl("v1").stream(*args, **kwargs)
        return res

BAMLFnOutputClass = IBAMLFnOutputClass()

__all__ = [ "BAMLFnOutputClass" ]
