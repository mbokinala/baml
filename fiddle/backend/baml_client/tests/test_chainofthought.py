# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..__do_not_import.generated_baml_client import baml
from ..baml_types import IChainOfThought, IChainOfThoughtStream, LinterOutput
from baml_lib._impl.deserializer import Deserializer
from json import dumps
from pytest_baml.ipc_channel import BaseIPCChannel
from typing import Any


@baml.ChainOfThought.test(stream=True)
async def test_learn_baml_extract_level1(ChainOfThoughtImpl: IChainOfThoughtStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    content = to_str("Given the email below:\n\nEmail Subject: {#input.subject}\nEmail Body: {#input.body}\n\n Extract this info from the email in JSON format:\n {\n      \"id\": string,\n      \"date\": string,\n      \"product_name\": string,\n      \"cost\": float\n }\n\n JSON:")
    deserializer = Deserializer[str](str) # type: ignore
    param = deserializer.from_string(content)
    async with ChainOfThoughtImpl(param) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()

@baml.ChainOfThought.test(stream=True)
async def test_reasoning_out_of_order(ChainOfThoughtImpl: IChainOfThoughtStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    content = to_str("Given the text below:\n\n{input}\n\nextract this information from it that follows this json schema:\n{\n   sentiment: \"happy\" | \"sad\" | \"ecstatic\"\n   reasoning: string\n}\n\nOutput JSON:")
    deserializer = Deserializer[str](str) # type: ignore
    param = deserializer.from_string(content)
    async with ChainOfThoughtImpl(param) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()

@baml.ChainOfThought.test(stream=True)
async def test_test1(ChainOfThoughtImpl: IChainOfThoughtStream, baml_ipc_channel: BaseIPCChannel):
    def to_str(item: Any) -> str:
        if isinstance(item, str):
            return item
        return dumps(item)

    content = to_str("    Given the email below: fe \n\n    Email Subject: {#input.subject}\n    Email Body: {#input.body}\n\n    Explain the reasoning behind how you extract this info from the email, and then provide the extracted info in JSON format:\n    {#print_type(output)}\n\n    JSON:")
    deserializer = Deserializer[str](str) # type: ignore
    param = deserializer.from_string(content)
    async with ChainOfThoughtImpl(param) as stream:
        async for response in stream.parsed_stream:
            baml_ipc_channel.send("partial_response", response.json())

        await stream.get_final_response()
