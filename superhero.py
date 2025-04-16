# Base class
class Superhero:
    def __init__(self, name, power, universe):
        self.name = name
        self.power = power
        self.universe = universe

    def introduce(self):
        return f"I am {self.name} from {self.universe} universe! 💥"

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass 1
class FlyingHero(Superhero):
    def __init__(self, name, power, universe, flight_speed):
        super().__init__(name, power, universe)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} takes off at {self.flight_speed} km/h and uses {self.power} in the sky! ✈️"

# Subclass 2
class TechHero(Superhero):
    def __init__(self, name, power, universe, gadget):
        super().__init__(name, power, universe)
        self.gadget = gadget

    def use_power(self):
        return f"{self.name} uses the {self.gadget} to unleash {self.power}! 🤖"

# Example usage
if __name__ == "__main__":
    hero1 = FlyingHero("SkyFlash", "Wind Tornado", "Aether", 500)
    hero2 = TechHero("CyberBlade", "Hacking Surge", "NeoTech", "Neural Blade")

    print(hero1.introduce())
    print(hero1.use_power())

    print(hero2.introduce())
    print(hero2.use_power())
