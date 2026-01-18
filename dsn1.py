from utils.utils import get_input

def duplicateValue(nums) -> bool:
    # using set data structure
    seen = set()
    # traverse nums
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

if __name__=="__main__":
    # Don't change this code
    numbers, target = get_input()
    # TODO work on this function to return indices of
    # a value that has duplicate in the list 
    hasDuplicate = duplicateValue(numbers)
    if hasDuplicate:
        print("✅ There are duplicate values in the list")
    else:
        print("There are no duplicate values in the list")

