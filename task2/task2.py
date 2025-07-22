# Write a function that finds the sum of the two largest integers in an array.

def sum_two_largest_ints(input: list[int]) -> int:
    """
    Returns the sum of the two largest integers from a given list of integers 
    """

    if len(input) == 0:
        raise ValueError("input must not be empty")

    if len(input) == 1:
        return input[0]

    if len(input) == 2:
        return input[0] + input[1]

    largest = float('-inf')
    second_largest = float('-inf')

    for num in input:
        if num > largest:
            second_largest = largest
            largest = num
        elif num <= largest and num >= second_largest:
            second_largest = num

    return largest + second_largest

def main():
    input1 = [1, 4, 2, 3, 5]
    print(f"Input 1: {input1}")
    print(f"Sum of the 2 largest integers: {sum_two_largest_ints(input1)}")
    print("---------------------\n")

    input2 = [5]
    print(f"Input 2: {input2}")
    print(f"Sum of the 2 largest integers: {sum_two_largest_ints(input2)}")
    print("---------------------\n")

    input3 = [1, 3, 4, 5, 5]
    print(f"Input 3: {input3}")
    print(f"Sum of the 2 largest integers: {sum_two_largest_ints(input3)}")
    print("---------------------\n")

    input4 = [-10, -24, -5, 5]
    print(f"Input 3: {input4}")
    print(f"Sum of the 2 largest integers: {sum_two_largest_ints(input4)}")
    print("---------------------\n")

if __name__ == "__main__":
    main()
