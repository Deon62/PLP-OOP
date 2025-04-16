##  OOP Assignment – PLP Software Engineering   
**Course**: Power Learn Project – Software Engineering Track  
**Module**: Object-Oriented Programming (OOP)  
**Assignment**: Class Design & Polymorphism Challenge  

---

###  Overview
This assignment demonstrates **core Object-Oriented Programming concepts** in Python, including:
- Class creation and object instantiation
- Constructors and attributes
- Inheritance and method overriding
- Polymorphism through shared method signatures

The project is divided into **two activities**:

---

###  File Structure

```
.
├── superhero.py         # Assignment 1: Superhero class with inheritance
├── vehicles.py          # Activity 2: Polymorphism example with vehicles
├── README.md            # Project documentation
```

---

##  Assignment 1: Design Your Own Class!

**Concepts Demonstrated:**
- Class definition
- Object construction with `__init__`
- Inheritance (subclasses for different hero types)
- Method overriding (`use_power()`)

###  Classes:
- `Superhero`: Base class with name, power, and universe.
- `FlyingHero`: Inherits from Superhero, adds flight speed.
- `TechHero`: Inherits from Superhero, adds gadget.

###  Example Output:
```
I am SkyFlash from Aether universe! 
SkyFlash takes off at 500 km/h and uses Wind Tornado in the sky! ✈
I am CyberBlade from NeoTech universe! 
CyberBlade uses the Neural Blade to unleash Hacking Surge! 
```

---

## Activity 2: Polymorphism Challenge

**Concepts Demonstrated:**
- Abstract base behavior using a common `move()` method
- Polymorphism through different implementations of `move()` across classes

###  Classes:
- `Vehicle` (base class)
- `Car`, `Plane`, `Boat`, `Bike`: Each implements `move()` differently

###  Example Output:
```
Driving 
Flying 
Sailing 
Cycling 
```

---

###  How to Run

Ensure you have **Python 3.x** installed.  
Run each file individually from your terminal or IDE:

```bash
python superhero.py
python vehicles.py
```

---

