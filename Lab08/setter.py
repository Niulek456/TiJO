class User:
    def __init__(self, name, age):
        self._name = name
        self._age = None
        self.set_age(age)

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if 0 <= new_age <= 130:
            self._age = new_age
        else:
            print(f"Odrzucono wartość: {new_age}. Wiek musi być z przedziału 0–130.")

# Użycie
user = User("Jan", 30)
print(f"Początkowy wiek: {user.get_age()}")

user.set_age(-5)
print(f"Po ustawieniu -5: {user.get_age()}")

user.set_age(200)
print(f"Po ustawieniu 200: {user.get_age()}")

user.set_age(45)
print(f"Po ustawieniu 45: {user.get_age()}")
