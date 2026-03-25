import random 

class Car:
    def __init__(self, car_number, max_speed):
        self.car_number = car_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0 
    
    def accelerate(self,change):
        self.current_speed += change 
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0

    def drive (self, hours):
        distance = self.current_speed * hours
        self.travelled_distance += distance

cars = []
for i in range(1,11):
    num = f"L-{i}"
    max_v = random.randint(36,180)
    cars.append(Car(num, max_v))

race_on = True
while race_on:
    for car in cars:
        speed_change = random.randint(-18,20)
        car.accelerate(speed_change)

        car.drive(1)
        if car.travelled_distance >=1000:
            race_on = False 

print("-" * 60)
print(f"{'Biển sô':<12}{'Vận tốc tối đa':<18}{'Vận tốc hiện tại':<20}{'Quãng đường':<18}")
print("-" * 60)
for car in cars:
    print(f"{car.car_number:<12}{car.max_speed:<18}{car.current_speed:<20}{car.travelled_distance:<18}")
print("-" * 60)