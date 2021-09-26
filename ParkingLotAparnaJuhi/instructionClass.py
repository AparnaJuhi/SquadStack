from parkingLot import ParkingLot 
import sys 
import os
class Instruction:
    def __init__(self,filename):
        self.filename = filename
        self.instructions_arr = [] 
        self.parkinglot = None 

    def is_an_integer(self,value):
        for v in value:
            if v>'9' or v<'0':
                return False 
        return True

    def is_valid_age(self,driver_age):
        if driver_age<18:
            return False
        return True

    def is_only_alpha(self,value):
        for v in value:
            if v>'Z' or v<'A':
                return False 
        return True

    def is_valid_registration(self,registration_number):
        if type(registration_number)!=str or registration_number=='':
            return False 
        registration_number_breakup = registration_number.split('-')
        if len(registration_number_breakup)!=4:
            return False 
        if len(registration_number_breakup[0])!=2 or self.is_only_alpha(registration_number_breakup[0])==False:
            return False 
        if len(registration_number_breakup[1])!=2 or self.is_an_integer(registration_number_breakup[1])==False:
            return False 
        if len(registration_number_breakup[2])!=2 or self.is_only_alpha(registration_number_breakup[2])==False:
            return False 
        if len(registration_number_breakup[3])!=4 or self.is_an_integer(registration_number_breakup[3])==False:
            return False 
        return True 

    def creating_parking_lot_helper(self,instruction_breakup):
        if len(instruction_breakup)!=2:
            return "Invalid Arguement to create parking lot"
        try:
            size_of_parking = int(instruction_breakup[1]) 
        except:
            return "parking lot size is not an integer" 
        self.parkinglot = ParkingLot(size_of_parking)
        return "Created parking of "+str(size_of_parking)+" slots"

    def park_helper(self,instruction_breakup):
        if len(instruction_breakup)!=4:
            return "Invalid Arguement to Park"
        if not self.is_valid_registration(instruction_breakup[1]):
            return "Registration number invalid"
        else:
            registration_number = instruction_breakup[1]
        if instruction_breakup[2]!="driver_age":
            return "Command is not 'driver_age'" 
        try:
            age_of_driver = int(instruction_breakup[3]) 
        except:
            return "driver's age is not integer"
        if not self.is_valid_age(age_of_driver):
            return "Driver's age is invalid" 
        slot_number = self.parkinglot.park_new_vehicle(registration_number,age_of_driver)
        if slot_number==False:
            return "Parking lot is full, Sorry for inconvenience"
        return "Car with vehicle registration number \""+registration_number+"\" has been parked at slot number "+str(slot_number)
    
    def leave_helper(self,instruction_breakup):
        if len(instruction_breakup)!=2:
            return "Invalid Arguement to create parking lot"
        try:
            slot_number = int(instruction_breakup[1]) 
        except:
            return "parking lot number is not an integer" 
        slot_details = self.parkinglot.vacate(slot_number) 
        if not slot_details:
            return "No car was parked at "+str(slot_number) 
        registration_number = slot_details[0] 
        driver_age = slot_details[1] 
        return "Slot number "+str(slot_number)+" vacated, the car with vehicle registration number \""+str(registration_number)+"\" left the space, the driver of the car was of age "+str(driver_age)

    def slot_number_for_car_with_number_helper(self,instruction_breakup):
        if len(instruction_breakup)!=2:
            return "Invalid Arguement to create parking lot"
        if self.is_valid_registration(instruction_breakup[1]):
            registration_number = instruction_breakup[1] 
        else:
            return "Not a valid registration number" 
        slot_number = self.parkinglot.get_slot_of_car(registration_number)
        if not slot_number:
            return "There is no car parked with number "+registration_number
        return slot_number

    def slot_numbers_for_driver_of_age_helper(self,instruction_breakup):
        if len(instruction_breakup)!=2:
            return "Invalid Arguement to create parking lot"
        try:
            age_of_driver = int(instruction_breakup[1]) 
        except:
            return "driver's age is not integer"
        list_of_slots = self.parkinglot.get_slots_on_drivers_age(age_of_driver) 
        if not list_of_slots:
            return ""
        for i in range(len(list_of_slots)):
            list_of_slots[i] = str(list_of_slots[i])
        return ",".join(list_of_slots)

    def vehicle_registration_number_for_driver_of_age_helper(self,instruction_breakup):
        if len(instruction_breakup)!=2:
            return "Invalid Arguement to create parking lot"
        try:
            age_of_driver = int(instruction_breakup[1]) 
        except:
            return "driver's age is not integer"
        list_of_cars = self.parkinglot.get_cars_on_drivers_age(age_of_driver)
        if not list_of_cars:
            return ""
        return ",".join(list_of_cars) 

    def read_instructions(self):
        try:
            file = open(os.path.join(sys.path[0],self.filename), 'r')
        except OSError:
            print("Could not open/read file:", self.filename)
            sys.exit()
        with file: 
            for each_instruction in file.readlines():
                print(each_instruction)
                self.instructions_arr.append(each_instruction) 

    def perform_operation(self,instruction):
        if not type(instruction)==str or instruction=="":
            return False 
        instruction_breakup = instruction.strip("\n").split(" ")

        if instruction_breakup[0]=="Create_parking_lot":
            return self.creating_parking_lot_helper(instruction_breakup)
        
        elif instruction_breakup[0]=="Park":
             return self.park_helper(instruction_breakup)

        elif instruction_breakup[0]=="Leave":
            return self.leave_helper(instruction_breakup)
        
        elif instruction_breakup[0]=="Slot_number_for_car_with_number":
            return self.slot_number_for_car_with_number_helper(instruction_breakup)

        elif instruction_breakup[0]=="Slot_numbers_for_driver_of_age":
            return self.slot_numbers_for_driver_of_age_helper(instruction_breakup)

        elif instruction_breakup[0]=="Vehicle_registration_number_for_driver_of_age":
            return self.vehicle_registration_number_for_driver_of_age_helper(instruction_breakup)

        else:
            return "Invalid Command"    
    
    def perform_operations(self):
        for each_instruction in self.instructions_arr:
            print(self.perform_operation(each_instruction)) 
        
