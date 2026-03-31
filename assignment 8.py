class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
    def go_to_floor(self, floor):
        if self.bottom <= floor <= self.top:
            self.current_floor = floor
        else:
            print("Tầng không hợp lệ. Vui lòng nhập tầng từ", self.bottom, "đến", self.top)

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = [Elevator(bottom, top) for _ in range(num_elevators)]
    def run_elevator(self, elevator_number, floor):
        if 0 <= elevator_number < len(self.elevators):
            self.elevators[elevator_number].go_to_floor(floor)
            print("Đã đưa thang máy đến tầng số", floor)
        else:
            print("Số thang máy không hợp lệ.")
    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)
            print("Đã đưa thang máy về tầng 1")
h = Elevator(1, 10)
h.go_to_floor(5)
print("Tầng hiện tại:", h.current_floor)
my_building = Building(1, 10, 3)
my_building.run_elevator(2, 5)

import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.distance_traveled = 0
    def accelerate(self, change):
        self.current_speed = max(0, min(self.current_speed + change, self.max_speed))
    def drive(self, hours):
        self.distance_traveled += self.current_speed * hours
class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list
    def hours_passed(self):
        for car in self.car_list:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
    def print_status(self):
        print(f"{'Registration':<10}{'Max Speed':<15}{'Current Speed':<18}{'Distance Traveled':<15}")
        print("-" * (len("Registration") + len("Max Speed") + len("Current Speed") + len("Distance Traveled") + 10))
        for car in self.car_list:
            print(f"{car.registration_number:<10}{car.max_speed:<15}{car.current_speed:<18}{car.distance_traveled:<15}")
    def race_finished(self):
        for car in self.car_list:
            if car.distance_traveled >= self.distance:
                return True
        return False
    
cars = []
for i in range(1, 11):
    max_speed = random.randint(100, 200)
    cars.append(Car(f"ABC-{i}", max_speed))
derby = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while not derby.race_finished():
    derby.hours_passed()
    hours += 1
    if hours % 10 == 0:
        print(f"\n[Sau {hours} giờ đua]")
        derby.print_status()
print(f"\n=== CUỘC ĐUA KẾT THÚC TẠI GIỜ THỨ {hours} ===")
derby.print_status()