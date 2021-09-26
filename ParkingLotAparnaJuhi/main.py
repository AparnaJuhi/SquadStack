from instructionClass import Instruction

def main():
    instructions = Instruction("input.txt") 
    instructions.read_instructions() 
    instructions.perform_operations() 

if __name__=="__main__":
    main()