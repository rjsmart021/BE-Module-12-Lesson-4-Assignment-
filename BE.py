
class OrderQueue:
    def __init__(self):
        self.orders = queue.Queue()

    def add_order(self, order):
        self.orders.put(order)
        print(f"Order added: {order}")

    def remove_order(self):
        if not self.orders.empty():
            order = self.orders.get()
            print(f"Order completed: {order}")
            return order
        else:
            print("No orders to remove")
            return None

# Example usage
if __name__ == "__main__":
    kitchen_queue = OrderQueue()
    kitchen_queue.add_order("Burger")
    kitchen_queue.add_order("Pizza")
    kitchen_queue.remove_order()
    kitchen_queue.remove_order()
    kitchen_queue.remove_order(
