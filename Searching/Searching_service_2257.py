#TODO
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import re

class SearchService:
 def __init__(self, data):
 self.data = data
 self.tf_idf_vectorizer = TfidfVectorizer()
 self.tf_idf_matrix = self.tf_idf_vectorizer.fit_transform(data)

 def search(self, query):
 query_vector = self.tf_idf_vectorizer.transform([query])
 similarity = cosine_similarity(query_vector, self.tf_idf_matrix).flatten()
 indices = np.argsort(similarity, axis=0)[::-1]
 return [(index, similarity[index]) for index in indices]

class DataService:
 def __init__(self, file_path):
 self.file_path = file_path
 self.data = self.read_data(file_path)

 def read_data(self, file_path):
 with open(file_path, 'r') as file:
 data = [line.strip() for line in file.readlines()]
 return data

def main():
 file_path = 'data.txt' # replace with your file path
 data_service = DataService(file_path)
 search_service = SearchService(data_service.data)
 while True:
 query = input('Enter your search query: ')
 results = search_service.search(query)
 for index, similarity in results:
 print(f'Similarity: {similarity:.2f} - {data_service.data[index]}')

if __name__ == '__main__':
 main()
