import warnings
import logging
import os.path
import sys
import multiprocessing

import gensim
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
# 忽略警告
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

program = os.path.basename(sys.argv[0]) # 读取当前文件的文件名
logger = logging.getLogger(program)
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
logger.info("running %s" % ' '.join(sys.argv))

# inp为输入语料, outp1为输出模型, outp2为vector格式的模型
inp = '\\WSDForCN\data\corpusSegDone_1.txt'
out_model = '\\WSDForCN\data\corpusSegDone_1.model'
out_vector = '\\WSDForCN\data\corpusSegDone_1.vector'
 
# 训练模型
model = Word2Vec(LineSentence(inp), vector_size=50, window=5, min_count=5,workers=multiprocessing.cpu_count())

# 保存模型
model.save(out_model)
# 保存词向量
model.wv.save_word2vec_format(out_vector, binary=False)
