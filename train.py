from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import time
import logging

start=time.time()
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
mini_model=Word2Vec(LineSentence('wikicorpus_training.txt'),min_count=1,size=100,window=5,workers=4)
print('time used is:{}'.format(time.time()-start))
# mini_model.wv('罕见')
print(mini_model.most_similar('日本'))
mini_model.save('w2vec.model')
