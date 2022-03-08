class Meta(type):
    def __new__(self, class_name, bases, attrs):

        a = {}
        for key, val in attrs.items():
            if key.startswith("__"):
                a[key] = val
            else:
                a[key.upper()] = val

        return type(class_name, bases, a)


class Dog(metaclass=Meta):
    x = 5
    y = 7

    def __repr__(self):
        return f"X is equal to : {self.X}     and Y is equal to {self.Y}"

    def hello(self):
        print("hello dog")


d = Dog()
print(d)
