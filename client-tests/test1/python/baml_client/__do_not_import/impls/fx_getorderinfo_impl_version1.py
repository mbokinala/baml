# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..clients.client_gpt4 import GPT4
from ..functions.fx_getorderinfo import BAMLGetOrderInfo
from ..types.classes.cls_email import Email
from ..types.classes.cls_orderinfo import OrderInfo
from ..types.classes.cls_productinfo import ProductInfo
from ..types.enums.enm_orderstatus import OrderStatus
from baml_lib._impl.deserializer import Deserializer


# Impl: version1
# Client: GPT4
# An implementation of .


__prompt_template = """\
Given the email below:

Email Subject: {arg.subject}
Email Body: {arg.body}

Extract this info from the email in JSON format:
{
  "id": string,
  "date": string,
  "products": {
    "name": string,
    "cost": float | null,
    "order_status": "OrderStatus as string"
  }[],
  "total_cost": float
}


Schema definitions:
OrderStatus
---
ORDERED
SHIPPED
DELIVERED

JSON:\
"""

__input_replacers = {
    "{arg.body}",
    "{arg.subject}"
}


# We ignore the type here because baml does some type magic to make this work
# for inline SpecialForms like Optional, Union, List.
__deserializer = Deserializer[OrderInfo](OrderInfo)  # type: ignore






@BAMLGetOrderInfo.register_impl("version1")
async def version1(arg: Email, /) -> OrderInfo:
    response = await GPT4.run_prompt_template(template=__prompt_template, replacers=__input_replacers, params=dict(arg=arg))
    deserialized = __deserializer.from_string(response.generated)
    return deserialized