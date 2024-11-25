class BrowsingHistory:
    def __init__(self):
        self.history = []

    def add_page(self, page):
        self.history.append(page)
        print(f"Page added: {page}")

    def remove_page(self):
        if not self.is_empty():
            page = self.history.pop()
            print(f"Page removed: {page}")
            return page
        else:
            print("No pages to remove")
            return None

    def pages_viewed(self):
        return len(self.history)

    def is_empty(self):
        return len(self.history) == 0

# Example usage
if __name__ == "__main__":
    browsing_history = BrowsingHistory()
    browsing_history.add_page("https://example.com")
    browsing_history.add_page("https://example.com/about")
    print(f"Pages viewed: {browsing_history.pages_viewed()}")
    browsing_history.remove_page()
    print(f"Pages viewed: {browsing_history.pages_viewed()}")
    print(f"Is browsing session empty? {browsing_history.is_empty()}")
    browsing_history.remove_page()
    print(f"Is browsing session empty? {browsing_history.is_empty()}")
