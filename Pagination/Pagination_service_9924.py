#TODO
from typing import List, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')

class Paginator(ABC):
    def __init__(self, items: List[T], page_size: int):
        self.items = items
        self.page_size = page_size
        self.current_page = 1
        self.total_pages = -(-len(items) // page_size) # Ceiling division

    def has_next_page(self) -> bool:
        return self.current_page < self.total_pages

    def has_previous_page(self) -> bool:
        return self.current_page > 1

    @abstractmethod
    def get_page(self, page: int) -> List[T]:
        pass

    def next_page(self) -> List[T]:
        if self.has_next_page():
            self.current_page += 1
            return self.get_page(self.current_page)
        return []

    def previous_page(self) -> List[T]:
        if self.has_previous_page():
            self.current_page -= 1
            return self.get_page(self.current_page)
        return []

class ListPaginator(Paginator):
    def get_page(self, page: int) -> List[T]:
        start = (page - 1) * self.page_size
        end = start + self.page_size
        return self.items[start:end]

def main():
    items = [i for i in range(100)] # Replace with your list of items
    page_size = 10
    paginator = ListPaginator(items, page_size)

    while True:
        page = paginator.get_page(paginator.current_page)
        for item in page:
            print(item)
        print(f"Page {paginator.current_page} of {paginator.total_pages}")

        command = input("Enter 'next' for next page, 'prev' for previous page or 'exit' to quit: ")
        if command == 'next' and paginator.has_next_page():
            paginator.next_page()
        elif command == 'prev' and paginator.has_previous_page():
            paginator.previous_page()
        elif command == 'exit':
            break

if __name__ == "__main__":
    main()