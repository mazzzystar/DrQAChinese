#!/usr/bin/env python3
# Copyright 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
"""JSimple wrapper around the Jieba Tokenizer pipeline.
https://github.com/fxsjy/jieba
"""

import jieba
import logging
from .tokenizer import Tokens, Tokenizer

logger = logging.getLogger(__name__)


class JiebaTokenizer(Tokenizer):
    def __init__(self, **kwargs):
        """
        Args:
            annotators: None or empty set (only tokenizes).
        """
        # load jieba
        _tmp = jieba.cut("sdsdsd")
        print("Finished loading jieba")

        self.annotators = set()

    def tokenize(self, text):
        data = []
        result = jieba.tokenize(text)
        for tk in result:
            token, start_ws, end_ws = tk[0], tk[1], tk[2]
            data.append((
                token,
                text[start_ws: end_ws],
                (start_ws, end_ws + len(token)),
                None,
                None,
                None,
            ))
        return Tokens(data, self.annotators)
