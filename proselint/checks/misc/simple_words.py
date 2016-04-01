# -*- coding: utf-8 -*-
"""What is this supposed to say.

---
layout:     post
source:     Writing Science in Plain English
source_url: ???
title:      simple words
date:       2016-04-01 12:00:00
categories: writing
---

TODO description

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Check the text."""
    err = "greene.complicated_words"
    msg = "Try '{}' instead of '{}'."

    complications = [
        # verbs
        ["put",         ["implement"]],
        ["stick",       ["adhere"]],
        ["make",        ["develop"]],
        ["keep",        ["retain"]],
        ["use",         ["utilize"]],
        ["end",         ["terminate"]],
        ["find",        ["ascertain"]],
        ["help",        ["facilitate"]],
        ["try",         ["endeavor"]],
        ["send",        ["transmit"]],
        ["start",       ["initiate"]],
        # nouns
        ["change",      ["alteration"]],
        ["work",        ["investigations"]],
        ["plan",        ["prescription"]],
        # adverbs, adjectives
        ["next",        ["subsequent"]],
        ["patchy",      ["heterogeneous"]],
        ["in space",    ["spatial"]],
        ["in time",     ["temporal"]]
    ]

    return preferred_forms_check(text, complications, err, msg)

