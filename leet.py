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

def addTwoEqualToTarget(nums: list, target: int) -> []:
    """
    # using bruteforce approach
    # The time complexity of this approach is O(n^2)
    # find the complement of the first value in the list
    size = len(nums)
    for index in range(size):
        complement = target - nums[index]
        for j in range(1, size):
            sumOfTwoDistinctValue = nums[index] + nums[j]
            if (sumOfTwoDistinctValue == target):
                return index, j
    return []
    """
    # using other DS = dictionary approach
    # The time complexity is O(n)
    # find the complement of the first value in the list
    hashMap = {}
    size = len(nums)
    for index in range(size):
        complement = diffOfTwoNumbers(target, nums[index])
        if complement in hashMap.keys():
            j = hashMap[complement]
            return [index, j]
        hashMap[nums[index]] = index
    return []


if __name__=="__main__":
    # Don't change this code
    numbers, target = get_input()
    # TODO work on this function to return indices of 
    # the two numbers that add up to the target 
    indices = addTwoEqualToTarget(numbers, target)
    if len(indices) == 2:
        i, j = indices
        print("Great job ✅")
        print((numbers[i],'@index',i),"+",(numbers[j],'@index',j)," = ",addTwoNumbers(numbers[i], numbers[j]))
    else: print("No solution")
     
    