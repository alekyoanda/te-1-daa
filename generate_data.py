import random

SIZE = [200, 2000, 20000]

def random_data_generator(start, end):
    size_index = 0
    for i in range(start, end+1):
        f = open(f"data/random{i}.txt", "w")
        
        output = ""
        nums = set() 
        for i in range(1, SIZE[size_index]):
            num = random.randint(1, SIZE[size_index]+1)
            while num in nums:
                num = random.randint(1, SIZE[size_index]+1)

            nums.add(num)
            if i < SIZE[size_index]-1:
                output += f"{num},"
            else:
                output += f"{num}"

        size_index += 1

        f.write(output)
        f.close()

def sorted_data_generator(start, end):
    size_index = 0
    for i in range(start, end+1):
        f = open(f"data/sorted{i}.txt", "w")
        
        output = ""
        for num in range(1, SIZE[size_index]+1):
            if num < SIZE[size_index]:
                output += f"{num},"
            else:
                output += f"{num}"

        size_index += 1

        f.write(output)
        f.close()

def reversed_sorted_data_generator(start, end):
    size_index = 0
    for i in range(start, end+1):
        f = open(f"data/reverse{i}.txt", "w")
        
        output = ""       
        for num in range(SIZE[size_index], -1, -1):
            if num > 0:
                output += f"{num},"
            else:
                output += f"{num}"

        size_index += 1
        f.write(output)
        f.close()

random_data_generator(1, 3)
sorted_data_generator(1, 3)
reversed_sorted_data_generator(1, 3)
