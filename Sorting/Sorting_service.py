class SortingService:
    def __init__(self):
        pass

    def sort_by_similarity(self, items, reverse=True):
        """ Sort items (index, score) by similarity score, descending by default """
        return sorted(items, key=lambda x: x[1], reverse=reverse)

    def stable_sort_by_similarity_and_index(self, items):
        """ Perform a stable sort by similarity and then by index """
        return sorted(items, key=lambda x: (-x[1], x[0]))
    
    def sort_numbers(self, numbers, reverse=False):
        """ Sorts a list of numbers, ascending by default. """
        return sorted(numbers, reverse=reverse)