from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SearchService:
    def __init__(self, data):
        if not data:
            raise ValueError("Data list cannot be empty")
        self.data = data
        self.tf_idf_vectorizer = TfidfVectorizer()
        self.tf_idf_matrix = self.tf_idf_vectorizer.fit_transform(data)

    def search(self, query):
        query_vector = self.tf_idf_vectorizer.transform([query])
        similarity = cosine_similarity(query_vector, self.tf_idf_matrix).flatten()
        # Sort by similarity, then by index to ensure stable results
        sorted_indices = sorted(range(len(similarity)), key=lambda x: (-similarity[x], x))
        return [(index, similarity[index]) for index in sorted_indices if similarity[index] > 0]

class DataService:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_data(file_path)

    def read_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = [line.strip() for line in file.readlines() if line.strip()]
            return data
        except FileNotFoundError:
            raise Exception(f"The file {file_path} does not exist")

def main():
    file_path = 'data.txt'  # replace with your file path
    data_service = DataService(file_path)
    search_service = SearchService(data_service.data)
    while True:
        query = input('Enter your search query: ')
        if not query:
            break
        results = search_service.search(query)
        for index, similarity in results:
            print(f'Similarity: {similarity:.2f} - {data_service.data[index]}')

if __name__ == '__main__':
    main()
