from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,model,max_speed):
        self._brand = brand
        self._model = model
        self._max_speed = max_speed

    @abstractmethod
    def time_for_a_distance(self,distance):
        pass
    @abstractmethod
    def print_brand_model(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, model, max_speed,price):
        super().__init__(brand, model, max_speed)
        self._price = price

    def time_for_a_distance(self, distance):
        time = distance/self._max_speed
        return time
    
    def print_brand_model(self):
        print(f"brand: {self._brand}, model: {self._model}")

    def is_expensive(self):
        if self._price < 25000:
            print("The car is cheap")
        else:
            print("The car is expensive")
class Truck(Vehicle):
    def __init__(self, brand, model, max_speed,size):
        super().__init__(brand, model, max_speed)
        self._size = size
      
    def time_for_a_distance(self, distance):
        time = distance/self._max_speed
        return time
    
    def print_brand_model(self):
        print(f"brand: {self._brand}, model: {self._model}")

    def is_big(self):
        if self._size<500:
            print("this truck is small")
        else:
            print("this truck is big")

class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node
class List_of_vehicle(Node):
    def __init__(self,head=None):
        self.head = head

    def add_vehicle(self,new_vehicle):
        if self.head == None:
            self.head = Node(new_vehicle)
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = Node(new_vehicle)

    def get_vehicle_with_index(self,index):
        if self.head == None:
            print("Empty list")
            return
        if index < 0:
            print("index out of range")
            return
        if index == 0:
            return self.head.data
        current = self.head
        for i in range(index):
            if current.next_node == None:
                print("index out of range")
                return
            current = current.next_node
        return current.data


car1 = Car("A","B",300,2000)
car1.print_brand_model()
print(car1.time_for_a_distance(360))
car1.is_expensive()
truck1 = Truck("C","D",200,450)
truck1.print_brand_model()
print(truck1.time_for_a_distance(360))
car2 = Car("E","F",320,50000)
car3 = Car("N","N",280,30000)
truck2 = Truck("H","G",250,530)
truck1.is_big()
parking = List_of_vehicle()
parking.add_vehicle(car1)
parking.add_vehicle(truck1)
parking.add_vehicle(car2)
parking.add_vehicle(car3)
parking.add_vehicle(truck2)
parking.get_vehicle_with_index(4).print_brand_model()