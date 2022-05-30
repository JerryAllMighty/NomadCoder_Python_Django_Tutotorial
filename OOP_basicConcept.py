# 객체 지향의 기본
class Car():
  def __init__(self, *args, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.windows = 4
    self.seats = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "$20")
  
  
  
  def __str__(self) -> str:
    return f"car with {self.wheels} wheels"
  
  
  
porche = Car(color = "green", price="$40")
porche.color = "Red"

ferrari = Car()
ferrari.color = "Yellow"

mini = Car()
mini.color = "White"


# print(dir(Car))

# Class Extend
class Convertable(Car):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.time = kwargs.get("time", 10)
  
  def take_off(self):
    return "taking off"
  
another_porche = Convertable(color="Sexy Red", price="$20")

print(another_porche.color, another_porche.seats)

  