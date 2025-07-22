# Write a function that identifies the most frequent string lengths in an array of strings

def most_frequent_length(input: list[str]) -> list[str]:
    """
    Returns a list of strings with the most frequent string length from given input list
    """

    if len(input) == 0:
        return [] 

    if len(input) == 1:
        return input 

    # Dictionary to map a length (int) to a list of strings with that length
    # e.g.: { 1: ["a"], 2: ["ab", "cd", "gh"], 3: ["abc", "def"] }
    len_to_strings_dict = {}

    # Dictionary to map a length (int) to the number of strings with that length
    #
    # e.g.: { 1: 1, 2: 3, 3: 2 }
    # There is 1 string with length of 1, 3 strings with length of 2 and 2 strings with length of 3
    len_to_count_dict = {}

    # Keep track of the highest frequency
    max_count = 0

    for string in input:

        length = len(string)

        if len_to_strings_dict.get(length) == None:
            len_to_strings_dict[length] = [string]
            len_to_count_dict[length] = 1
        else:
            len_to_strings_dict[length].append(string)
            len_to_count_dict[length] += 1

        if len_to_count_dict[length] > max_count:
            max_count = len_to_count_dict[length]

    most_frequent_len = [length for length, count in len_to_count_dict.items() if count == max_count] 
    return len_to_strings_dict[most_frequent_len[0]]


def main():
    input1 = ['a', 'ab', 'abc', 'cd', 'def', 'gh']
    print(f"Input 1: {input1}")
    print(f"Strings with the most frequent length from input 1: {most_frequent_length(input1)}")
    print("---------------------\n")

    input2 = []
    print(f"Input 2: {input2}")
    print(f"Strings with the most frequent length from input 2: {most_frequent_length(input2)}")
    print("---------------------\n")

    input3 = ['a']
    print(f"Input 3: {input3}")
    print(f"Strings with the most frequent length from input 3: {most_frequent_length(input3)}")
    print("---------------------\n")

if __name__ == "__main__":
    main()
