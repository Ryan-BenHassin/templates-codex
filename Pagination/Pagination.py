class PaginationService:
    def __init__(self, items, page_size=10):
        self.items = items  # The list of items to paginate
        self.page_size = page_size  # Dynamically set the number of items per page
        self.offset = 0  # This keeps track of the current offset

    def paginate(self):
        return self.items[self.offset:self.offset + self.page_size]

    def next_page(self):
        if self.offset + self.page_size < len(self.items):
            self.offset += self.page_size

    def previous_page(self):
        if self.offset - self.page_size >= 0:
            self.offset -= self.page_size

    def get_current_page(self):
        return self.paginate()

    def has_next_page(self):
        return len(self.items) > self.offset + self.page_size

    def has_previous_page(self):
        return self.offset > 0

    def get_page(self, page: int):
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]
    

    
def test_pagination():
    items = list(range(1, 101))  # A list of numbers from 1 to 100
    pagination = PaginationService(items, page_size=15)  # Set a custom page size
    
    # Access specific pages
    print("Page 1:", pagination.get_page(1))
    print("Page 2:", pagination.get_page(2))
    print("Page 7:", pagination.get_page(7))  # This will check boundary conditions

    # Testing navigation
    print("Current Page:", pagination.get_current_page())
    pagination.next_page()
    print("After Next Page:", pagination.get_current_page())
    pagination.previous_page()
    print("After Previous Page:", pagination.get_current_page())

    # Boundary checks
    print("Has Next Page:", pagination.has_next_page())
    print("Has Previous Page:", pagination.has_previous_page())

if __name__ == "__main__":
    test_pagination()
