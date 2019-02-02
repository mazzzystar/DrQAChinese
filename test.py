# coding: utf-8
from drqa.tokenizers import CoreNLPTokenizer
tok = CoreNLPTokenizer()
print(tok.tokenize('你好世界').words()) # Should complete immediately
