import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

class RecommendationService:
 def __init__(self, items_data):
 self.items_data = items_data

 def compute_similarity_matrix(self):
 vectorizer = TfidfVectorizer()
 tfidf = vectorizer.fit_transform(self.items_data.description)
 self.similarity_matrix = cosine_similarity(tfidf, tfidf)

 def recommend(self, item_id, num_recommendations):
 indices = pd.Series(self.items_data.index, index=self.items_data.id)
 idx = indices[item_id]
 sim_scores = list(enumerate(self.similarity_matrix[idx]))
 sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
 sim_scores = sim_scores[1:num_recommendations + 1]
 item_indices = [i[0] for i in sim_scores]
 return self.items_data.iloc[item_indices]

# Example usage
items_data = pd.read_csv('items.csv')
service = RecommendationService(items_data)
service.compute_similarity_matrix()
recommendations = service.recommend('item123', 5)
print(recommendations)
