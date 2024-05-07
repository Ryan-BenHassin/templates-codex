#TODO
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class RecommendationService:
 def __init__(self, items):
 self.items = items
 self.vectorizer = CountVectorizer()
 self.item_vectors = self.vectorizer.fit_transform([item['description'] for item in items])

 def recommend(self, item_id, num_recommendations=5):
 item_index = next((i for i, item in enumerate(self.items) if item['id'] == item_id), None)
 if item_index is None:
 return []
 item_vector = self.item_vectors.toarray()[item_index]
 similarities = cosine_similarity([item_vector], self.item_vectors.toarray())[0]
 sorted_indices = (-similarities).argsort()[1:num_recommendations + 1]
 return [self.items[i]['id'] for i in sorted_indices]

# Example usage:
items = [
 {'id': 1, 'description': 'This is item 1'},
 {'id': 2, 'description': 'This is item 2'},
 {'id': 3, 'description': 'This is item 3'},
 {'id': 4, 'description': 'This is item 4'},
 {'id': 5, 'description': 'This is item 5'},
]

service = RecommendationService(items)
recommendations = service.recommend(1)
print(recommendations)
