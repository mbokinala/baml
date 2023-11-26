# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from .__do_not_import.generated_baml_client import baml
from .baml_types import ClassifyResponse, IBlah, IClassifyTool, Tool
from baml_lib._impl.deserializer import Deserializer
from json5 import loads


@baml.Blah.test
async def test_basic2(BlahImpl: IBlah):
    deserializer = Deserializer[str](str)
    param = deserializer.from_string("""\
big fan of this\
""")
    await BlahImpl(param)


@baml.Blah.test
async def test_default(BlahImpl: IBlah):
    deserializer = Deserializer[str](str)
    param = deserializer.from_string("""\
te\
""")
    await BlahImpl(param)


@baml.Blah.test
async def test_greasy_white(BlahImpl: IBlah):
    deserializer = Deserializer[str](str)
    param = deserializer.from_string("""\
big fan of this\
""")
    await BlahImpl(param)


@baml.ClassifyTool.test
async def test_ministerial_tomato(ClassifyToolImpl: IClassifyTool):
    case = loads("""
{
  "query": "zzz",
  "context": "zz"
}
""")
    deserializer_query = Deserializer[str](str)
    query = deserializer_query.from_string(case["query"])
    deserializer_context = Deserializer[str](str)
    context = deserializer_context.from_string(case["context"])
    await ClassifyToolImpl(
        query=query,
        context=context
    )


@baml.ClassifyTool.test
async def test_present_scarlet(ClassifyToolImpl: IClassifyTool):
    case = loads("""
{
  "query": "zzz",
  "context": "zzzzzz"
}
""")
    deserializer_query = Deserializer[str](str)
    query = deserializer_query.from_string(case["query"])
    deserializer_context = Deserializer[str](str)
    context = deserializer_context.from_string(case["context"])
    await ClassifyToolImpl(
        query=query,
        context=context
    )


@baml.Blah.test
async def test_total_amaranth(BlahImpl: IBlah):
    deserializer = Deserializer[str](str)
    param = deserializer.from_string("""\
big fan of this\
""")
    await BlahImpl(param)
