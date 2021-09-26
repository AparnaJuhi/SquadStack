class ParkingLot:
    def __init__(self,size) -> None:
        self.parking_slot_size = size+1 
        self.nearest_empty_slot = 1 
        self.slot_arr = [False]*(size+1) 
        self.car_details = {} #it maps car number to slot and driver's age
        self.cars_by_driver_age = {} # it maps driver's age to list of cars 
    
    def get_nearest_empty_slot(self):
        if self.nearest_empty_slot < self.parking_slot_size:
            return self.nearest_empty_slot
        else:
            return -1 

    def get_next_nearest_empty_slot(self):
        for slot in range(self.nearest_empty_slot+1,self.parking_slot_size):
            if self.slot_arr[slot] == False:
                return slot 
        return -1 

    def set_nearest_empty_slot(self,new_emptied_slot = False):
        if new_emptied_slot and new_emptied_slot < self.get_nearest_empty_slot():
            self.nearest_empty_slot = new_emptied_slot
        else:
            self.nearest_empty_slot = self.get_next_nearest_empty_slot()

    def is_parking_lot_full(self):
        return self.get_nearest_empty_slot()==-1

    def add_details(self,slot_index,car_registration_number,drivers_age):
        self.slot_arr[slot_index] = car_registration_number 
        self.car_details[car_registration_number] = (slot_index,drivers_age) 
        if drivers_age in self.cars_by_driver_age:
            self.cars_by_driver_age[drivers_age].append(car_registration_number) 
        else:
            self.cars_by_driver_age[drivers_age] = [car_registration_number] 

    def park_new_vehicle(self,car_registration_number,drivers_age):
        if self.is_parking_lot_full():
            return False 
        slot_index = self.get_nearest_empty_slot() 
        self.add_details(slot_index,car_registration_number,drivers_age) 
        self.set_nearest_empty_slot() 
        return slot_index 

    def remove_details(self,car_registration_number):
        slot_index,drivers_age = self.car_details.pop(car_registration_number) 
        self.slot_arr[slot_index] = False 
        self.cars_by_driver_age[drivers_age].remove(car_registration_number) 
        if len(self.cars_by_driver_age[drivers_age])==0:
            self.cars_by_driver_age.pop(drivers_age)
        return car_registration_number,drivers_age

    def vacate(self,slot_index):
        if slot_index<=0 or slot_index>=self.parking_slot_size or self.slot_arr[slot_index]==False:
            return False 
        car_registration_number = self.slot_arr[slot_index] 
        car_registration_number,driver_age = self.remove_details(car_registration_number)
        self.set_nearest_empty_slot(slot_index) 
        return (car_registration_number,driver_age)

    def get_car_at_slot(self,slot_index):
        if slot_index>=0 and slot_index<self.parking_slot_size:
            return self.slot_arr[slot_index] 
        else:
            return False 

    def get_slot_of_car(self,car_registration_number):
        if car_registration_number in self.car_details:
            return self.car_details[car_registration_number][0] 
        else:
            return False

    def get_drivers_age_of_car(self,car_registration_number):
        if car_registration_number in self.car_details:
            return self.car_details[car_registration_number][1] 
        else:
            return False

    def get_cars_on_drivers_age(self,drivers_age):
        if drivers_age in self.cars_by_driver_age:
            return self.cars_by_driver_age[drivers_age]
        else:
            return False 

    def get_slots_on_drivers_age(self,drivers_age):
        cars_on_drivers_age = self.get_cars_on_drivers_age(drivers_age) 
        if not cars_on_drivers_age:
            return False 
        slots_on_drivers_age = []
        for each_car in cars_on_drivers_age:
            slots_on_drivers_age.append(self.car_details[each_car][0])
        return slots_on_drivers_age

    