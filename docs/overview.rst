The opencdms model and provider plugins
=======================================

pyopencdms is a Python implementation of the Climate Data Mangement System (CDMS)
specificiation, WMO No. 1131.

These specifications, that represent the high-level business logic of a CDMS,
are implemented following Domain Driven Design (DDD) principles.

Domain-driven design (DDD) is a software design approach that focuses on
modeling software to match a domain according to input from that domain's experts [1].

We start by implementing the Climate Data Model Standard (CDM) as a set of Python classes

.. mermaid::

   ---
   title: Animal example
   ---
   classDiagram
    note "From Duck till Zebra"
    Animal <|-- Duck
    note for Duck "can fly\ncan swim\ncan dive\ncan help in debugging"
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
        +String beakColor
        +swim()
        +quack()
    }
    class Fish{
        -int sizeInFeet
        -canEat()
    }
    class Zebra{
        +bool is_wild
        +run()
    }



[1] https://en.wikipedia.org/wiki/Domain-driven_design