# -*- coding: utf-8 -*-
"""What is this supposed to say.

---
layout:     post
source:     Writing Science in Plain English
source_url: ???
title:      Wordy Phrases
date:       2016-04-01 12:00:00
categories: writing
---

TODO description

"""
from proselint.tools import memoize, preferred_forms_check


@memoize
def check(text):
    """Check the text."""
    err = "greene.wordy_phrase"
    msg = "Try '{}' instead of '{}'."

    complications = [
        # verbs
        ["we assessed",         ["in this study we assessed"]],
        ["investigate",         ["conduct an investigation of"]],
        ["caused",              ["were responsible for"]],
        ["were",                ["played the role of"]],
        ["to",                  ["in order to"]],
        ["because",             ["for the following reasons"]],
        ["during",              ["during the course of",
                                 "during the process of"]],
        ["most",                ["a majority", "most of the"]],
        ["study",               ["undertake the examination of"]],
        ["evidence",            ["various lines of evidence"]],
        ["our analysis",        ["the analysis presented in this"]],
        ["without",             ["in the absence of"]],
        ["in",                  ["located in"]],
        ["at",                  ["located at"]],
        # adverbs, adjectives
        ["near",                ["in the vicinity of",
                                 "in close proximity to"]],
        ["never",               ["in no case", "on no occasion"]],
        ["now",                 ["at the present time",
                                 "at this point in time"]],
        ["for example",         ["an example of this is the fact that"]]
    ]

    return preferred_forms_check(text, complications, err, msg)

