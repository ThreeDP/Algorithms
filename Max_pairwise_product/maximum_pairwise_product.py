import random

def max_pairwise_prod(numbers):
    max_prod = 0
    n = len(numbers)
    for one in range(n):
        for two in range(one + 1, n):
            max_prod = max(max_prod, numbers[one] * numbers[two])
    return max_prod

def max_pairwise_prod_fast(numbers):
    one_index = -1
    n = len(numbers)
    for one in range(n):
        if one_index == -1 or numbers[one_index] < numbers[one]:
            one_index = one
    
    two_index = -1
    for two in range(n):
        '''
        Um erro pode ser comparar os dois valores:
            numbers[two] != numbers[one_index]
        '''
        if two != one_index and (two_index == -1 or numbers[two_index] < numbers[two]):
            two_index = two
    
    return numbers[one_index] * numbers[two_index]
    
def test_prog():
    while True:
        n = random.randint(2, 10)
        numbers = []
        for number in range(n):
            numbers.append(random.randint(1, 100))
        for number in numbers:
            print(number, "      ")
        normal = max_pairwise_prod(numbers)
        speed = max_pairwise_prod_fast(numbers)

        if normal != speed:
            print("Wrong answer.....", normal, "    |    ", speed)
            break
        else:
            print("OK")
    return 0

if __name__ == "__main__":
    #test_prog()
    n = int(input("Entre um valor inteiro: "))
    numbers = []
    i = 0

    for number in range(n):
        numbers.append(int(input(">> ")))
    
    print(max_pairwise_prod_fast(numbers))


