#!~/data/anaconda3/bin/python

'''
Author: Abhishek Sharma

Program: Word2Vec Model Training Code.

Last Modified: Nov 4, 2017
'''

import logging
import multiprocessing
import os
import sys
from gensim.models.word2vec import LineSentence
from gensim.models.word2vec import Word2Vec


class Word2Vec_Model(object):
    
        def __init__(self):
                self.execute()

        def parameter_verification:
                
                if len(sys.argv) < 3:
                        print("usuage: python word2vec_model.py input-file model-file")
                        return "Failed"
                else:
                        return "Success"
        def execute(self):

                program = os.path.basename(sys.argv[0])
        	logger = logging.getLogger(program)
	        logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
        	logging.root.setLevel(level=logging.INFO)
        	logger.info("Running %s" % ' '.join(sys.argv))
                input_verification = self.parameter_verification()
 
                if input_verification == "Success":
                        inp, outp = sys.argv[1:3]
	                max_length = 0
	                params = {
                		'size': 400,
		                'window': 10,
                		'min_count': 10,
	                    	'workers': max(1, multiprocessing.cpu_count() - 1),
                		'sample': 1E-5,
		                }
                        word2vec = Word2Vec(LineSentence(inp, max_sentence_length=10000),**params)
                        word2vec.save(outp)

if __name__ == '__main__':
        Word2Vec_Model()
