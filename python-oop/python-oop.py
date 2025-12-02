# OBJECTED ORIENTATED PROGRAMMING IN PYTHON

# Concept
"""
- OOP helps us write reusable, modular, and organized code.
- Objects are instances of classes that represent real-world entities, with attributes (data) and methods (behavior).
- Example: a Person object can have attributes like age and eye_color, and methods like walk() or run().
- A class is a blueprint that defines the structure (attributes) and behavior (methods) for its objects.
"""

# EXAMPLE IN PRACTICE
# Class definition (blueprint)
class Person:
    def __init__(self, name, age, eye_color):
        # Attributes (properties)
        self.name = name
        self.age = age
        self.eye_color = eye_color

    # Method (behavior)
    def walk(self):
        print(f"{self.name} is walking.")

    def run(self):
        print(f"{self.name} is running.")

# Creating objects (instances)
person1 = Person("Jeevika", 28, "green")
person2 = Person("Salto", 32, "brown")

# Accessing attributes
print(person1.name)       # Output: Jeevika
print(person2.eye_color)  # Output: brown

# Calling methods
person1.walk()  # Output: Jeevika is walking.
person2.run()   # Output: Salto is running.

# --------------------------------------------------------------------------------------------------------------- #


# CREATING A CLASS: ADDITIONAL EXAMPLE
# Example: Football Players

class FootballPlayers:
  def __init__(self, name, nationality, goals_scored):
    self.name = name
    self.nationality = nationality
    self.goals_scored = goals_scored

  def __str__(self):
    return f"Player: {self.name}, Nationality: {self.nationality}, Goals Scored: {self.goals_scored}"

# OBJECT: INSTANTIATING AN INSTANCE OF A CLASS.

player_calvin_williams = FootballPlayers("Calvin Williams", "South Africa", goals_scored=34)
print(player_calvin_williams)
