# Word2Vec Model on Wikipedia Articles.

### Download Training Data

url: https://dumps.wikimedia.org/enwiki/latest/ 

Note: I have trained the Model on using enwiki-latest-pages-articles.xml.bz2, but there are a lot of other datasets available. After extraction this data file size will be around 11GB.

### Normalize Data.

Command: python wikidata_normalize.py enwiki-latest-pages-articles.xml.bz2 wiki.text

Note: It took 7 to 8 hours for me, I was running it on aws 2GB ec2 compute node.

### Train Model

Command: python word2vec_model.py wiki.text wiki.model 
