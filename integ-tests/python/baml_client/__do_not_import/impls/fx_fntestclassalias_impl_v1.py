# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_gpt35 import GPT35
from ..functions.fx_fntestclassalias import BAMLFnTestClassAlias
from ..types.classes.cls_testclassalias import TestClassAlias
from ..types.partial.classes.cls_testclassalias import PartialTestClassAlias
from baml_core.provider_manager.llm_response import LLMResponse
from baml_core.stream import AsyncStream
from baml_lib._impl.deserializer import Deserializer


import typing
# Impl: v1
# Client: GPT35
# An implementation of FnTestClassAlias.

__prompt_template = """\
Return a json blob that has this schema:
{
  "key-dash": string,
  "key21": string,
  "key with space": string,
  "key4": string,
  "key.with.punctuation/123": string
}

JSON:\
"""

__input_replacers = {
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[TestClassAlias](TestClassAlias)  # type: ignore

# Add a deserializer that handles stream responses, which are all Partial types
__partial_deserializer = Deserializer[PartialTestClassAlias](PartialTestClassAlias)  # type: ignore







async def v1(arg: str, /) -> TestClassAlias:
    response = await GPT35.run_prompt_template(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
    deserialized = __deserializer.from_string(response.generated)
    return deserialized


def v1_stream(arg: str, /) -> AsyncStream[TestClassAlias, PartialTestClassAlias]:
    def run_prompt() -> typing.AsyncIterator[LLMResponse]:
        raw_stream = GPT35.run_prompt_template_stream(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
        return raw_stream
    stream = AsyncStream(stream_cb=run_prompt, partial_deserializer=__partial_deserializer, final_deserializer=__deserializer)
    return stream

BAMLFnTestClassAlias.register_impl("v1")(v1, v1_stream)