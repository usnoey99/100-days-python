### Day 17 - The Quiz Project & The Benefits of OOP

    PascalCase, camelCase, snake_case

- `self` refers to the instance itself.
- In Python, methods inside a class usually take `self` as the first parameter because the method needs to know which object is calling it.
- `self` allows each object to store its own data and lets methods access or modify that specific object's attributes.

Example:

class Dog:
    def bark(self):
        print("Woof!")

Create an object:

dog1 = Dog()

Call the method:

dog1.bark()

What Python does internally:

Dog.bark(dog1)

Here, `self = dog1`.

This means `self` represents the object currently executing the method.

If a method does not need access to object-specific data, `self` may not be necessary (e.g. static methods). Otherwise, `self` is required to avoid errors and to work with instance attributes correctly.
