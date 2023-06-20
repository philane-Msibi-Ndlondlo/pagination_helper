import math
# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return abs(math.ceil(len(self.collection) / self.items_per_page))
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        pass
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        pass
    

helper = PaginationHelper(['a','b','c','d','e','f'], 4)

#print(f"Page count is: {helper.page_count()}")
print(f"Item count is: {helper.item_count()}")
#print(f"Page item count is: {helper.page_item_count(2)}")