import sys

def get_input():
   
    if len(sys.argv) <= 2 or len(sys.argv) > 3:
        sys.exit(f"The program expects the following command format:\n\npython filename.py numbers.txt target")
    else:  
        try: 
            with open(sys.argv[1]) as f:
                items = f.read()
            numbers = [int(item) for item in list(items.split(","))]
            target = int(sys.argv[2])
            # return values
            return numbers, target
        except FileNotFoundError or FileExistsError as e:
            print("Error: Please, kindly confirm you file name")
            sys.exit()
        except ValueError as e:
            print("Error: Invalid input value")
    
def addTwoNumbers(a, b) -> int:
    return a + b

def diffOfTwoNumbers(a, b) -> int:
    return a - b