#!~/data/anaconda3/bin/python

'''
Program: Processing Wikipedia Data for Word2Vec

Author: Abhishek Sharma

Last Modified: Nov 4, 2017
'''

import os
import sys
import logging
from gensim.corpora import WikiCorpus

class Wikidata(object):

	def __init__(self):
		
		program = os.path.basename(sys.argv[0])
		self.logger = logging.getLogger(program)
		logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
		logging.root.setLevel(level=logging.INFO)
		self.logger.info("running %s" % ' '.join(sys.argv))

		self.wiki_input_file = sys.argv[1]
		self.wiki_output_file = sys.argv[2]

		self.execute()

	def execute(self):
		
                i = 0
		output_file_object = open(self.wiki_output_file, 'w')
		wiki = WikiCorpus(self.wiki_input_file, lemmatize=False, dictionary={})
		for text in wiki.get_texts():
			output_file_object.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')
			i = i + 1
			if (i % 1000 == 0):
				self.logger.info("Saved " + str(i) + " articles")
		output_file_object.close()
		self.logger.info("Finished Saved " + str(i) + " articles")

if __name__ == '__main__':
	Wikidata()
