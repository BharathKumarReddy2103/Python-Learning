# Object-Oriented Programming (OOP)

## Objective

Learn Object-Oriented Programming (OOP) in Python and understand how to design reusable, maintainable, and scalable application code.

This lesson covers classes, objects, constructors, attributes, methods, inheritance, method overriding, `super()`, encapsulation, properties, polymorphism, abstract classes, and composition.

The concepts are taught using practical DevOps and backend-development examples because OOP is an important foundation for building real Python applications and backend services.

---

## Why OOP Matters

As Python applications become larger, writing everything as standalone functions and scripts becomes difficult to maintain.

OOP helps organize application code into reusable components.

For example, a backend application may contain:

- Users
- Products
- Orders
- Payments
- Database connections
- Services
- Repositories
- Configuration
- Logging

OOP allows these components to be represented as classes and objects with clearly defined responsibilities.

OOP is commonly used in:

- Backend applications
- REST APIs
- FastAPI applications
- Database applications
- Automation frameworks
- Cloud automation
- DevOps tools
- Testing frameworks
- Large Python applications

---

## Concepts Covered

- Classes
- Objects
- Constructors
- Instance attributes
- Instance methods
- Class attributes
- Class methods
- Static methods
- Inheritance
- Multilevel inheritance
- Multiple inheritance
- Method overriding
- `super()`
- Encapsulation
- Properties
- Property getters
- Property setters
- Polymorphism
- Abstract classes
- Abstract methods
- Composition
- OOP application design

---

## Project Structure

```text
28-oop/
│
├── 01-class-and-object.py
├── 02-constructor.py
├── 03-instance-attributes.py
├── 04-instance-methods.py
├── 05-class-attributes.py
├── 06-class-method.py
├── 07-static-method.py
├── 08-inheritance.py
├── 09-multilevel-inheritance.py
├── 10-multiple-inheritance.py
├── 11-method-overriding.py
├── 12-super.py
├── 13-encapsulation.py
├── 14-properties.py
├── 15-polymorphism.py
├── 16-abstract-classes.py
├── 17-composition.py
├── 18-oop-mini-project.py
└── README.md
````

---

## 1. Class and Object

A class defines the structure and behavior of an object.

An object is an instance of a class.

Example:

```python
class Server:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment


server = Server("web01", "production")

print("Server:", server.name)
print("Environment:", server.environment)
```

---

## 2. Constructor

The `__init__()` method is called automatically when an object is created.

Example:

```python
class Server:

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment
```

The constructor initializes the object's attributes.

---

## 3. Instance Attributes

Instance attributes belong to individual objects.

Example:

```python
server1 = Server(
    "web01",
    "production"
)

server2 = Server(
    "web02",
    "development"
)
```

Each object has its own values.

---

## 4. Instance Methods

Instance methods operate on an object.

Example:

```python
class Server:

    def start(self):
        print(f"{self.name} server started")
```

The `self` parameter refers to the current object.

---

## 5. Class Attributes

Class attributes are shared by objects of the class.

Example:

```python
class Server:

    platform = "Linux"
```

Objects can access:

```python
server.platform
```

---

## 6. Class Methods

Class methods operate on the class rather than a specific instance.

They use:

```python
@classmethod
```

and receive `cls` as the first parameter.

Example:

```python
class Server:

    platform = "Linux"

    @classmethod
    def get_platform(cls):
        return cls.platform
```

---

## 7. Static Methods

Static methods belong logically to a class but don't require access to instance or class state.

They use:

```python
@staticmethod
```

Example:

```python
class Server:

    @staticmethod
    def validate_ip(ip):
        return len(ip.split(".")) == 4
```

Static methods are useful for utility or validation logic related to a class.

---

## 8. Inheritance

Inheritance allows one class to reuse functionality from another class.

Example:

```python
class Server:

    def start(self):
        print("Server started")


class WebServer(Server):

    def deploy(self):
        print("Application deployed")
```

`WebServer` inherits from `Server`.

Relationship:

```text
WebServer
    is-a
Server
```

---

## 9. Multilevel Inheritance

Multilevel inheritance creates an inheritance chain.

Example:

```text
Server
   ↓
ApplicationServer
   ↓
FrontendServer
```

The child class can inherit functionality from multiple levels in the hierarchy.

---

## 10. Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one parent class.

Example:

```python
class Monitoring:

    def health_check(self):
        print("Health check completed")


class Logging:

    def collect_logs(self):
        print("Collecting logs")


class Server(Monitoring, Logging):
    pass
```

The `Server` class receives functionality from both parent classes.

---

## 11. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method inherited from the parent.

Example:

```python
class Server:

    def start(self):
        print("Server started")


class WebServer(Server):

    def start(self):
        print("Web server started")
```

The child implementation replaces the inherited implementation for that object.

---

## 12. `super()`

`super()` allows a child class to access functionality from the parent class.

Example:

```python
class Server:

    def start(self):
        print("Server started")


class WebServer(Server):

    def start(self):
        super().start()
        print("Web server configuration loaded")
```

This allows the child class to extend the parent's behavior instead of completely replacing it.

---

## 13. Encapsulation

Encapsulation means controlling how an object's internal data is accessed and modified.

Python commonly uses:

```text
name
_name
__name
```

Where:

* `name` → public
* `_name` → protected convention
* `__name` → private-style attribute using name mangling

Example:

```python
class Server:

    def __init__(self):
        self.__status = "Stopped"

    def start(self):
        self.__status = "Running"

    def stop(self):
        self.__status = "Stopped"

    def get_status(self):
        return self.__status
```

The internal status is managed by the class methods.

---

## 14. Properties

Python properties allow methods to be accessed like attributes.

Example:

```python
class Server:

    def __init__(self, environment):
        self._environment = environment

    @property
    def environment(self):
        return self._environment
```

The value can be accessed with:

```python
server.environment
```

instead of:

```python
server.environment()
```

---

## Property Setter

A setter controls how a property can be changed.

Example:

```python
class Server:

    def __init__(self, environment):
        self._environment = environment

    @property
    def environment(self):
        return self._environment

    @environment.setter
    def environment(self, value):

        valid_environments = [
            "development",
            "staging",
            "production"
        ]

        if value not in valid_environments:
            raise ValueError("Invalid environment")

        self._environment = value
```

This allows validation before changing the internal value.

---

## 15. Polymorphism

Polymorphism allows the same method or interface to behave differently depending on the object.

Example:

```python
class WebServer:

    def start(self):
        print("Web server started")


class DatabaseServer:

    def start(self):
        print("Database server started")


servers = [
    WebServer(),
    DatabaseServer()
]

for server in servers:
    server.start()
```

Output:

```text
Web server started
Database server started
```

The same:

```python
server.start()
```

produces different behavior.

---

## Duck Typing

Python also supports polymorphism through duck typing.

Different objects can provide the same method without necessarily inheriting from the same class.

Example:

```python
class AWS:

    def deploy(self):
        print("Deploying to AWS")


class Kubernetes:

    def deploy(self):
        print("Deploying to Kubernetes")


targets = [
    AWS(),
    Kubernetes()
]

for target in targets:
    target.deploy()
```

The important requirement is that the objects provide the expected behavior.

---

## 16. Abstract Classes

Abstract classes define a contract that child classes must implement.

Python provides the `abc` module:

```python
from abc import ABC, abstractmethod
```

Example:

```python
from abc import ABC, abstractmethod


class PaymentProvider(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass
```

Child classes must implement the abstract method.

Example:

```python
class StripePayment(PaymentProvider):

    def process_payment(self, amount):
        print(f"Processing payment using Stripe")
```

Abstract classes are useful when multiple implementations must follow the same interface.

---

## 17. Composition

Composition represents a **has-a** relationship.

Example:

```text
Server
  │
  └── has-a → Logger
```

Python example:

```python
class Logger:

    def log(self, message):
        print(f"LOG: {message}")


class Server:

    def __init__(self):
        self.logger = Logger()

    def start(self):
        self.logger.log("Server started")
```

The `Server` contains and uses a `Logger` object.

---

## Inheritance vs Composition

### Inheritance

Represents an:

```text
is-a
```

relationship.

Example:

```text
WebServer is-a Server
```

### Composition

Represents a:

```text
has-a
```

relationship.

Example:

```text
Server has-a Logger
```

Composition is heavily used in real-world backend application architecture.

---

## OOP Mini Project

The final project combines the major OOP concepts learned in this lesson.

### Project

**DevOps Server Management System**

The application models:

* Web servers
* Database servers
* Server operations
* Logging
* Deployment
* Environment management

Architecture:

```text
Server
│
├── WebServer
├── DatabaseServer
│
└── Logger


Deployment
│
├── WebDeployment
└── DatabaseDeployment
```

The project demonstrates:

* Classes
* Objects
* Constructors
* Instance attributes
* Class attributes
* Methods
* Inheritance
* Method overriding
* `super()`
* Encapsulation
* Properties
* Polymorphism
* Abstract classes
* Composition

---

## Real-World Backend Applications

OOP concepts are heavily used when building Python backend applications.

Examples include:

```text
User
Product
Order
Payment
Database
Repository
Service
Logger
Configuration
```

A backend application might eventually have an architecture such as:

```text
API
 │
 ↓
Service
 │
 ↓
Repository
 │
 ↓
Database
```

Composition can be used to connect these components:

```text
UserService
│
├── UserRepository
├── Logger
└── EmailService
```

Inheritance, polymorphism, and abstraction can be used when multiple implementations need to follow a common interface.

---

## Real-World DevOps Applications

OOP can also be used for building automation frameworks.

Examples include:

* AWS automation
* Kubernetes automation
* Docker automation
* CI/CD tools
* Monitoring tools
* Deployment systems
* Infrastructure management
* Cloud provider integrations

For example:

```text
CloudProvider
│
├── AWSProvider
├── AzureProvider
└── GCPProvider
```

A common interface can define operations such as:

```text
create_instance()
delete_instance()
get_status()
```

Different providers can implement those operations differently.

---

## Learning Outcome

After completing this lesson, you will be able to:

* Understand classes and objects
* Create constructors
* Work with instance and class attributes
* Create instance, class, and static methods
* Implement inheritance
* Implement multilevel inheritance
* Implement multiple inheritance
* Override parent methods
* Use `super()`
* Understand encapsulation
* Use private-style attributes
* Create properties
* Implement property setters and validation
* Understand polymorphism
* Understand duck typing
* Create abstract classes
* Define abstract methods
* Understand composition
* Design reusable Python components
* Understand basic object-oriented application architecture
* Apply OOP concepts to backend development
* Apply OOP concepts to DevOps automation

---

## Development Skills Built

This lesson provides the OOP foundation required for the next stage of Python development.

The concepts will be used later for:

* FastAPI applications
* REST APIs
* Database applications
* Service layers
* Repository patterns
* Authentication systems
* Testing
* Application architecture
* Dependency injection
* DevOps automation frameworks

---

## DevOps + Backend Connection

The long-term goal is not only to write Python scripts.

The goal is to become capable of working across the complete application lifecycle:

```text
Python Development
        ↓
Backend Application
        ↓
REST API
        ↓
Database
        ↓
Testing
        ↓
Git
        ↓
CI/CD
        ↓
Docker
        ↓
Kubernetes
        ↓
AWS
        ↓
Monitoring
        ↓
Production
```

This combines Python backend development with the DevOps skills already learned.

---

## Next Lesson

**29 - Advanced Python**

The next stage will focus more heavily on Python development.

Topics will include:

* Advanced functions
* `*args`
* `**kwargs`
* Lambda functions
* `map()`
* `filter()`
* `sorted()`
* `any()`
* `all()`
* List comprehensions
* Dictionary comprehensions
* Set comprehensions
* Iterators
* Generators
* `yield`
* `enumerate()`
* `zip()`
* Advanced Python patterns

The focus from this point onward will increasingly shift toward **Python development and backend development**, while continuing to include Python scripting and automation for DevOps.

---

## Author

**Bharath Kumar Reddy N.**

Senior DevSecOps Engineer | AWS | Kubernetes | DevSecOps | Python | Backend Development | DevOps Automation