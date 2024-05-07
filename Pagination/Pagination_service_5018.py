#TODO
class PaginationService:
    def __init__(self, limit=10):
        self.limit = limit
        self.offset = 0

    def paginate(self, items):
        return items[self.offset:self.offset + self.limit]

    def next_page(self):
        self.offset += self.limit

    def previous_page(self):
        if self.offset - self.limit >= 0:
            self.offset -= self.limit

    def get_current_page(self, items):
        return self.paginate(items)

    def has_next_page(self, items):
        return len(items) > self.offset + self.limit

    def has_previous_page(self):
        return self.offset > 0