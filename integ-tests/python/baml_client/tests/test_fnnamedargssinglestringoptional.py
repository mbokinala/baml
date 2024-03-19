# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..__do_not_import.generated_baml_client import baml
from ..baml_types import IFnNamedArgsSingleStringOptional, IFnNamedArgsSingleStringOptionalStream
from baml_lib._impl.deserializer import Deserializer
from json import dumps
from pytest_baml.ipc_channel import BaseIPCChannel
from typing import Any, Optional


@baml.FnNamedArgsSingleStringOptional.test(stream=True)
async def test_mobile_gold(FnNamedArgsSingleStringOptionalImpl: IFnNamedArgsSingleStringOptionalStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    case = {"myString": "null", }
    deserializer_myString = Deserializer[Optional[str]](Optional[str]) # type: ignore
    myString = deserializer_myString.from_string(to_str(case["myString"]))
    async with FnNamedArgsSingleStringOptionalImpl(
        myString=myString
    ) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()
@baml.FnNamedArgsSingleStringOptional.test(stream=True)
async def test_upper_pink(FnNamedArgsSingleStringOptionalImpl: IFnNamedArgsSingleStringOptionalStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    case = {"myString": "value", }
    deserializer_myString = Deserializer[Optional[str]](Optional[str]) # type: ignore
    myString = deserializer_myString.from_string(to_str(case["myString"]))
    async with FnNamedArgsSingleStringOptionalImpl(
        myString=myString
    ) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()
