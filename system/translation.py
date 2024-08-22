from soynlp import DoublespaceLineCorpus

# iter_sent=Trueだと1行に複数文を許容する
corpus = DoublespaceLineCorpus("2016-10-20.txt", iter_sent=True)

