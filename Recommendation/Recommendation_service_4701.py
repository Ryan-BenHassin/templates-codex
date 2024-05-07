#TODO
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class RecommendationService:
 def __init__(self, data):
 self.data = data

 def fit(self):
 self.vectorizer = CountVectorizer()
 self.matrix = self.vectorizer.fit_transform(self.data['description'])

 def recommend(self, item_id, num_recommendations=5):
 idx = self.data.index[self.data['id'] == item_id].values[0]
 similarity_matrix = cosine_similarity(self.matrix)
 scores = list(enumerate(similarity_matrix[idx]))
 scores.sort(key=lambda x: x[1], reverse=True)
 scores = scores[1:num_recommendations + 1]
 return [self.data.iloc[i[0]]['id'] for i in scores]

# example usage
data = pd.DataFrame({
 'id': [1, 2, 3, 4, 5],
 'description': ['apple phone', 'apple watch', 'amsung phone', 'amsung watch', 'huawei phone']
})

rec_service = RecommendationService(data)
rec_service.fit()
print(rec_service.recommend(1))
