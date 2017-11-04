# Word2Vec Model on Wikipedia Articles.

### Download Training Data

url: https://dumps.wikimedia.org/enwiki/latest/ 

Note: I have trained the Model on enwiki-latest-pages-articles.xml.bz2, but there are a lot of other datasets available. After extraction this data file size will be around 11GB.

### Normalize Data.

Command: python wikidata_normalize.py enwiki-latest-pages-articles.xml.bz2 wiki.text

Note: It took 7 to 8 hours for me, I was running it on aws 2GB ec2 compute node.

### Train Model.

Command: python word2vec_model.py wiki.text wiki.model 

### Output Screenshot.
![screenshot from 2017-11-04 15-11-20](https://user-images.githubusercontent.com/15223639/32409911-ee95da24-c172-11e7-8c4a-8838d5c6526c.png)

It goes without saying, if you have more targetted data according to your requirement, it will give much better results. 
