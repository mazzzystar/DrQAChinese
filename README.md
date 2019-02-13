# DrQAChinese
This is a PyTorch implementation of the Chinese version DrQA system described in the ACL 2017 paper [Reading Wikipedia to Answer Open-Domain Questions](https://arxiv.org/abs/1704.00051), with several changes from [facebookresearch's DrQA](https://github.com/facebookresearch/DrQA).

<p align="center"><img width="70%" src="img/drqa.png" /></p>

## Changes
* Use [jieba](https://github.com/fxsjy/jieba/issues) to replace DrQA's CoreNLP Tokenizer, I found difficult to use it, maybe later to test on.
* Train with Wikipedia Chinese Dataset, later will add Baidu baike Dataset.
* For training `Document Reader`, use `Word2Vec` rather than `Glove`.
* ...


## Dataset
Download Wikipedia Chinese Dataset as
```
wget http://download.wikipedia.com/zhwiki/latest/zhwiki-latest-pages-articles.xml.bz2
```

Use [WikiExtractor](https://github.com/attardi/wikiextractor) to extract into a json format `docs`.


## Document Retriver
Build db and tfidf matrix for Chinese corpus.
```
# build db for wiki data.
python scripts/retriever/build_db.py wiki/docs/path path/to/save/cnwiki.db

# build tfidf matrix.
python scripts/retriever/build_tfidf.py path/of/cnwiki.db path/to/save/tfidf/matrix --tokenizer jieba

# interactivate with query to recall doc.
python scripts/retriever/interactive.py --model path/to/save/tfidf/matrix/cnwiki-tfidf-ngram=2-hash=16777216-tokenizer=jieba.npz
```

Interactivate with query to recall top K doc:
```
>>> process("陶然亭", k=5)
+------+---------+------------+-----------+
| Rank |  Doc Id |   Title    | Doc Score |
+------+---------+------------+-----------+
|  1   |  77049  | 陶然亭公园 |   314.63  |
|  2   | 1276185 | 陶然亭街道 |    144    |
|  3   |  381803 |  西长安街  |   124.08  |
|  4   | 1136252 |  陶然亭站  |   124.08  |
|  5   |  381801 |  东长安街  |   124.08  |
+------+---------+------------+-----------+
>>> process("白居易", k=5)
+------+---------+----------------+-----------+
| Rank |  Doc Id |     Title      | Doc Score |
+------+---------+----------------+-----------+
|  1   |  13521  |     白居易     |   233.31  |
|  2   | 1855255 |    白氏文集    |   168.76  |
|  3   |  316514 |     长恨歌     |   158.55  |
|  4   | 1587985 | 赋得古原草送别 |   139.28  |
|  5   |  41917  |      元稹      |   100.52  |
+------+---------+----------------+-----------+
>>> process("faker", k=5)
+------+---------+-------------------+-----------+
| Rank |  Doc Id |       Title       | Doc Score |
+------+---------+-------------------+-----------+
|  1   | 4847391 |       李相赫      |   251.09  |
|  2   | 5107319 |       卢本伟      |   131.9   |
|  3   | 5511053 | 李知勋 (电竞选手) |   131.9   |
|  4   | 5884300 |      Bjergsen     |   65.95   |
|  5   | 3042993 |    弗兰克·阿瑙    |   65.95   |
+------+---------+-------------------+-----------+
>>> process("赤壁赋谁写的", k=5)
+------+---------+------------------+-----------+
| Rank |  Doc Id |      Title       | Doc Score |
+------+---------+------------------+-----------+
|  1   |   6433  |       苏轼       |   178.94  |
|  2   | 5602419 | 福音书历史可靠性 |   137.18  |
|  3   |  846550 |     前赤壁赋     |   131.42  |
|  4   |  228648 | 弗里茨·克莱斯勒  |   124.37  |
|  5   | 3339731 |     后赤壁赋     |   118.04  |
+------+---------+------------------+-----------+
```

Evaluate `Document Retriver` with Baidu's `webQA` dataset, below is the methods:
* For every QA pair, use `question` as query and get top `K` docs.
* Judge if these docs contain `answer`, 1 if yes else 0.
* Calculate the percentage of the case the recalled docs contain answers.

Evaluation the ability for `Document Retriver` with:
```
python scripts/retriever/eval.py webQA.train.json --model path/to/save/tfidf/matrix/cnwiki-tfidf-ngram=2-hash=16777216-tokenizer=jieba.npz --doc-db path/of/cnwiki.db --tokenizer jieba --n-docs 5
```
The result with `jieba` tokenizer is:

| recalled doc num K        | Examples           | Matches in top K  | Match % in top K  | Total time usage（s） |
| ------------- |:-------------:| :-------------:| :-------------:| -----:| 
| 5     | 36181 | 23427| 64.75%| 1964.3972|
| 20     | 36181 |   27824 | 76.90 | 4808.3328|

## Document Reader
TBD