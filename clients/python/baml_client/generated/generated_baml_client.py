# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.
#
# BAML version: 0.0.1
# Generated Date: 2023-10-24 15:44:55.523214 -07:00
# Generated by: aaronvillalpando

from .functions.fx_foobar import BAMLFooBar
from .functions.fx_foobar2 import BAMLFooBar2


class BAMLClient:
    FooBar = BAMLFooBar
    FooBar2 = BAMLFooBar2

baml = BAMLClient()
