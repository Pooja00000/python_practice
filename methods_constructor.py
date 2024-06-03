class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'])

    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

# Main program
if __name__ == "__main__":
    # Creating a Person instance using the regular constructor
    person1 = Person('Alice', 30)
    print(person1)

    # Creating a Person instance using the alternate constructor
    data = {'name': 'Bob', 'age': 25}
    person2 = Person.from_dict(data)
    print(person2)
