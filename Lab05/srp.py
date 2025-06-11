class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer

class OrderValidator:
    def validate(self, order):
        print("Walidacja zamówienia.")

class OrderRepository:
    def save(self, order):
        print("Zapisywanie zamówienia do bazy danych.")

class EmailSender:
    def send_confirmation(self, order):
        print("Wysyłanie e-maila potwierdzającego.")

class OrderProcessor:
    def __init__(self, order):
        self.order = order
        self.validator = OrderValidator()
        self.repo = OrderRepository()
        self.mailer = EmailSender()

    def process_order(self):
        self.validator.validate(self.order)
        self.repo.save(self.order)
        self.mailer.send_confirmation(self.order)

order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
processor = OrderProcessor(order)
processor.process_order()
