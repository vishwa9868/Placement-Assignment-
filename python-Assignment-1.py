#!/usr/bin/env python
# coding: utf-8

# # python-Assignment-1

# 1-Q1. What is the purpose of Python's OOP

# ANS:-The purpose of Python's Object-Oriented Programming (OOP) is to provide a programming paradigm that organizes code into reusable objects with their own properties (attributes) and behaviors (methods). OOP allows you to structure your code in a way that models real-world entities or concepts, making it easier to manage complexity, promote code reuse, and improve code maintainability.
# 
# 
# 
# Modularity and Reusability: OOP allows you to break down a problem into smaller, self-contained objects. These objects can be reused in different parts of your code or in other projects, promoting modularity and reducing code duplication.
# 
# Encapsulation: OOP encapsulates data (attributes) and methods (functions) into objects, allowing you to control access to data and provide a clear interface for interacting with objects. Encapsulation helps with code organization, data integrity, and information hiding.
# 
# Inheritance: OOP supports inheritance, which enables the creation of new classes (child classes) based on existing classes (parent classes). Inheritance allows child classes to inherit attributes and methods from parent classes, facilitating code reuse and promoting hierarchical relationships between objects.
# 
# Polymorphism: Polymorphism allows objects of different classes to be used interchangeably based on a shared interface or superclass. This concept enables flexibility and allows you to write code that can work with different types of objects, enhancing code extensibility and adaptability.
# 
# Code Maintainability: OOP promotes clean code organization and separation of concerns. With well-designed classes and objects, code becomes easier to understand, modify, and maintain. OOP principles, such as encapsulation and abstraction, can also improve code documentation and readability.

# Q2. Where does an inheritance search look for an attribute?

# ANS:-
# Instance attributes: Python first checks if the attribute exists in the instance object itself. If the attribute is found, it is used.
# 
# Class attributes: If the attribute is not found in the instance object, Python searches for it in the class of the instance. If the attribute is found in the class, it is used. Class attributes are shared among all instances of the class.
# 
# Parent classes: If the attribute is not found in the instance or the class, Python continues the search in the parent classes according to the method resolution order (MRO). It checks each parent class in the order specified by the inheritance hierarchy until the attribute is found or the search reaches the topmost parent class (usually the base object class).
# 
# This attribute lookup order ensures that attributes defined in subclasses can override attributes defined in parent classes, allowing for flexibility and customization in object-oriented programming.

# Q3. How do you distinguish between a class object and an instance object?

# ANS:-Class Object: A class object represents the blueprint or template for creating instances of that class. It defines the structure, attributes, and behaviors that instances of the class will have. The class object is created when the class is defined. It can have class attributes and class methods that are shared among all instances of the class. You can access class attributes and methods using the class name itself. For example, if Car is a class, Car.color refers to a class attribute, and Car.start_engine() refers to a class method.
# 
# Instance Object: An instance object, also known as an instance, is a specific object created from a class using the class constructor. Each instance has its own set of attributes and can have different values for those attributes. Instances are independent entities that can be modified separately without affecting other instances or the class itself. To create an instance, you use the class name followed by parentheses. For example, car = Car() creates an instance of the Car class, and car.color refers to an instance attribute specific to that particular car object.

# Q4. What makes the first argument in a class’s method function special?

# ANS:-In Python, the first argument in a class's method function is conventionally named self. This argument is special because it refers to the instance of the class on which the method is called. It allows the method to access and manipulate the instance's attributes and behaviors.
# 
# Here are a few key points that make the self argument special:
# 
# Instance Binding: When a method is called on an instance object, the instance itself is automatically passed as the first argument to the method. By convention, this argument is named self, although you can technically choose any name you prefer (although it is strongly recommended to stick with self for consistency and readability).
# 
# Accessing Instance Attributes: Using the self argument, you can access the instance's attributes within the method. For example, if the instance has an attribute named color, you can access it using self.color within the method. This allows methods to retrieve and modify the state of the specific instance.
# 
# Invoking Other Instance Methods: The self argument enables you to invoke other methods defined within the same class on the instance. By using self.method_name(), you can call other instance methods and perform more complex operations or encapsulate related functionality.
# 
# Creating and Modifying Instance Attributes: Within a method, you can create new instance attributes or modify existing ones using the self argument. For example, you can assign a value to a new attribute using self.attribute_name = value. This allows methods to update the state of the instance during execution.
# 
# By using the self argument, you establish the link between a method and the instance it is called on. It provides a way to access and manipulate the specific instance's data and behaviors, enabling methods to interact with the instance and perform tasks specific to that particular object

# Q5. What is the purpose of the __init__ method?
The __init__ method in Python is a special method, also known as the constructor, which is automatically called when an instance of a class is created. Its purpose is to initialize the attributes of the instance and perform any setup or initialization tasks that are required.

Here are the key purposes and features of the __init__ method:

Initialization: The primary purpose of the __init__ method is to initialize the instance's attributes with specific values. Inside the __init__ method, you can assign initial values to attributes, set up data structures, or perform any necessary setup tasks.

Automatic Invocation: When an instance of a class is created using the class constructor, the __init__ method is automatically called for that instance. This ensures that the instance is properly initialized with the specified attributes and that any required setup actions are performed before using the instance.

Passing Arguments: The __init__ method can accept arguments, allowing you to pass values during instance creation. These arguments can be used to set the initial state of the instance or provide data for attribute initialization. By convention, the first argument of __init__ is self, representing the instance itself.

Customization: By defining your own __init__ method in a class, you can customize the initialization process for instances. This enables you to control how attributes are initialized, validate input values, perform computations, or set default values based on provided arguments or predefined logic

class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.speed = 0

    def accelerate(self, speed_increase):
        self.speed += speed_increase

# Creating an instance of the Car class
my_car = Car("red", "sedan")

print(my_car.color)  # Output: red
print(my_car.model)  # Output: sedan
print(my_car.speed)  # Output: 0
# Q6. What is the process for creating a class instance?
# ANS:-Class Definition: Define a class that specifies the attributes and behaviors of the objects you want to create instances of. The class serves as a blueprint or template for creating instances.

Class Instantiation: Create an instance of the class by calling the class's constructor method. The constructor method is usually named __init__ and is responsible for initializing the instance's attributes. It is automatically called when an instance is created.

Constructor Arguments: Pass any necessary arguments to the constructor method during instance creation. These arguments can be used to initialize the instance's attributes with specific values.

Instance Assignment: Assign the newly created instance to a variable or use it directly. This allows you to reference and work with the instance throughout your program


# Step 1: Class Definition
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def start_engine(self):
        print("Engine started!")

# Step 2: Class Instantiation
my_car = Car("red", "sedan")  # Creating an instance of the Car class

# Step 3: Constructor Arguments
# The arguments "red" and "sedan" are passed to the constructor

# Step 4: Instance Assignment
# The instance is assigned to the variable "my_car"

# Accessing instance attributes
print(my_car.color)  # Output: red
print(my_car.model)  # Output: sedan

# Calling instance methods
my_car.start_engine()  # Output: Engine started!Q7. What is the process for creating a class?ANS:-The process for creating a class in Python involves the following steps:

Class Definition: Start by defining the class using the class keyword followed by the name of the class. The name should follow Python naming conventions (typically using CamelCase).

Class Attributes: Optionally, define class attributes. These attributes are shared among all instances of the class and are defined inside the class but outside of any methods. Class attributes are accessed using the class name itself.

Constructor Method: Define the constructor method, usually named __init__, inside the class. The constructor is responsible for initializing the instance's attributes when an instance is created. It takes the self parameter as the first argument, which refers to the instance being created.

Instance Methods: Define other methods inside the class to specify the behaviors of the instances. These methods are used to perform actions or operations related to the class and its instances. They typically take the self parameter as the first argument to access the instance's attributes and perform instance-specific operations

# Step 1: Class Definition
class Car:
    # Step 2: Class Attributes
    wheels = 4

    # Step 3: Constructor Method
    def __init__(self, color, model):
        self.color = color
        self.model = model

    # Step 4: Instance Methods
    def start_engine(self):
        print("Engine started!")

    def drive(self):
        print("Driving...")

# Creating instances and using the class

# Creating an instance of the Car class
my_car = Car("red", "sedan")

# Accessing class attributes
print(Car.wheels)  # Output: 4

# Accessing instance attributes
print(my_car.color)  # Output: red
print(my_car.model)  # Output: sedan

# Calling instance methods
my_car.start_engine()  # Output: Engine started!
my_car.drive()  # Output: Driving...Q8. How would you define the superclasses of a classANS:-The superclasses of a class, also known as parent classes or base classes, are the classes from which the current class directly inherits. In Python, class inheritance allows a class to inherit attributes and behaviors from one or more superclasses.

To define the superclasses of a class, you need to specify them within parentheses after the class name during class definition. This is done by including the superclass names inside the parentheses, separated by commas.

# Defining superclass A
class A:
    def method_a(self):
        print("Method A")

# Defining superclass B
class B:
    def method_b(self):
        print("Method B")

# Defining a class C that inherits from superclasses A and B
class C(A, B):
    def method_c(self):
        print("Method C")

# Creating an instance of class C
my_object = C()

# Calling methods from superclass A
my_object.method_a()  # Output: Method A

# Calling methods from superclass B
my_object.method_b()  # Output: Method B

# Calling method from class C
my_object.method_c()  # Output: Method C