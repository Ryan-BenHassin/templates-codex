#TODO
class Pagination:
 def __init__(self, items, page_size=10):
 self.items = items
 self.page_size = page_size

 def paginate(self, page_number):
 start = (page_number - 1) README.md categories.txt generate.sh start.sh systemPrompt.txt templates self.page_size
 end = start + self.page_size
 return self.items[start:end]

def main():
 items = list(range(1, 101)) # example data
 pagination = Pagination(items)
 page_number = 1 # example page number
 page = pagination.paginate(page_number)
 print(f"Page {page_number}: {page}")

if __name__ == "__main__":
 main()
