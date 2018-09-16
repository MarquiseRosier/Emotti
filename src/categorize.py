import numpy as np  
class Categorize:
  # Category -> words
  def __init__(self):
    self.data = {
      'Sports': ['basketball', 'baseball', 'cricket', 'soccer', 'volleyball', 'rugby'],
      'Religion': ['christian', 'islam', 'judaism', 'hindu', 'buddhism'],
      'Media' : ['movies', 'music', 'television', ],
      'Politics': ['international affairs', 'nations', 'political affairs', 'parties'],
      'Games': ['video games', 'board games'],
      'Black': ['haitian', 'nigerian', 'jamaicans'],
      'Asian': ['chinese', 'indian', 'japanese', 'cambodian'],
      'White': ['irish', 'german', 'french']
    }
    # Words -> category
    self.categories = {word: key for key, words in self.data.items() for word in words}
    # Load the whole embedding matrix
    self.embeddings_index = {}
    f = open('glove.6B.100d.txt');
    for line in f:
      values = line.split()
      word = values[0]
      embed = np.array(values[1:], dtype=np.float32)
      self.embeddings_index[word] = embed
    print('Loaded %s word vectors.' % len(self.embeddings_index))

  def process_query(self, query):
    # Embeddings for available words
    data_embeddings = {key: value for key, value in self.embeddings_index.items() if key in self.categories.keys()}
    query_embed = self.embeddings_index[query]
    scores = {}
    for word, embed in data_embeddings.items():
      category = self.categories[word]
      dist = query_embed.dot(embed)
      dist /= len(self.data[category])
      scores[category] = scores.get(category, 0) + dist
    print(scores);

if __name__ == '__main__':
    categorizer = Categorize();
    categorizer.process_query('ping-pong')
    categorizer.process_query('')