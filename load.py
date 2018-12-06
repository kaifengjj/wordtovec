from gensim.models import word2vec

model=word2vec.Word2Vec.load('w2vec.model')
print(model.wv.similarity('文化','艺术'))
print(model.wv.most_similar(['伦敦','中国'],['北京']))