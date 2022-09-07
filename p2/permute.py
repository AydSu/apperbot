from sys import argv
from random import randint 
import time
start_time = time.time()

N = int(argv[1])

sames = [0 for i in range(N)] 
diff = [i for i in range(1,N+1)]
print(diff)

nums_init = diff#[1,2,3,4,5]


def permute(old_nums_list, digit):
    """для всех комбинаций, полученных на предыдущем шаге, создает комбинации с еще одной цифрой"""
    if (len(old_nums_list) == 0): return [[digit]]
    if (len(old_nums_list) == 1): 
        return [old_nums_list[0] + [digit], [digit] + old_nums_list[0]]

    nums_list = []

    for nums in old_nums_list:        
        nums = [digit] + nums
        nums_list.append(nums.copy())
        mix(nums, nums_list)
    return nums_list


def mix(nums, nums_list):
    """переносит первую цифру на шаг вправо пока не дойдет до конца"""
    i = 0
    for j in range(i+1, len(nums)):
        nums[j],nums[j-1] = nums[j-1],nums[j]
        nums_list.append(nums.copy())
    
# по очереди комбинируем сначала 2 первые цифры, потом 3 итд
old_nums_list = []
for i in range(len(nums_init)):
    digit = nums_init[i]
    old_nums_list = permute(old_nums_list, digit)
    print(len(old_nums_list))

# print(old_nums_list)

zero_nums_list = permute(old_nums_list, 0)

# перемешать предыдущие комбинации с разными числами и нулем с другими нулями
new_nums_list = []
for nums in old_nums_list:
    for i in range(N):
        first_zeros = [0 for j in range(i)]
        last_zeros = [0 for j in range(N-1-i)]
        new_nums = first_zeros + nums + last_zeros       
        new_nums_list.append(new_nums)

print(len(new_nums_list))

with open('output.txt', 'w') as f:
    for nums in new_nums_list:
        string = ''.join(str(x) for x in nums) + '\n'
        f.write(string)

print("--- %s seconds ---" % (time.time() - start_time))