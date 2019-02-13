# coding: utf-8
from drqa.tokenizers import JiebaTokenizer
tok = JiebaTokenizer()
print(tok.tokenize('赵本山是谁？我和他是世界上最美的人嘛').words()) # Should complete immediately
