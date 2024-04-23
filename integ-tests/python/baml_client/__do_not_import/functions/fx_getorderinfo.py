# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_email import Email
from ..types.classes.cls_orderinfo import OrderInfo
from ..types.enums.enm_orderstatus import OrderStatus
from ..types.partial.classes.cls_email import PartialEmail
from ..types.partial.classes.cls_orderinfo import PartialOrderInfo
from baml_core.stream import AsyncStream
from baml_lib._impl.functions import BaseBAMLFunction
from typing import AsyncIterator, Callable, Protocol, runtime_checkable


IGetOrderInfoOutput = OrderInfo

@runtime_checkable
class IGetOrderInfo(Protocol):
    """
    This is the interface for a function.

    Args:
        email: Email

    Returns:
        OrderInfo
    """

    async def __call__(self, *, email: Email) -> OrderInfo:
        ...

   

@runtime_checkable
class IGetOrderInfoStream(Protocol):
    """
    This is the interface for a stream function.

    Args:
        email: Email

    Returns:
        AsyncStream[OrderInfo, PartialOrderInfo]
    """

    def __call__(self, *, email: Email
) -> AsyncStream[OrderInfo, PartialOrderInfo]:
        ...
class IBAMLGetOrderInfo(BaseBAMLFunction[OrderInfo, PartialOrderInfo]):
    def __init__(self) -> None:
        super().__init__(
            "GetOrderInfo",
            IGetOrderInfo,
            ["default_config"],
        )

    async def __call__(self, *args, **kwargs) -> OrderInfo:
        return await self.get_impl("default_config").run(*args, **kwargs)
    
    def stream(self, *args, **kwargs) -> AsyncStream[OrderInfo, PartialOrderInfo]:
        res = self.get_impl("default_config").stream(*args, **kwargs)
        return res

BAMLGetOrderInfo = IBAMLGetOrderInfo()

__all__ = [ "BAMLGetOrderInfo" ]