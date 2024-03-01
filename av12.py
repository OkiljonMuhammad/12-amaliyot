from typing import List
#1-masala

# def sumOddLengthSubarrays(arr: List[int]) -> int:
#         total_sum = 0
#         n = len(arr)
#         for i in range(n):
#             for j in range(i, n, 2):
#                 total_sum += sum(arr[i:j+1])
#         return total_sum
    
# arr = [1,4,2,5,3]

# result = sumOddLengthSubarrays(arr)

# print(result)

#2-masala


# def destCity(paths: List[List[str]]) -> str:
#     all_cities = [city for path in paths for city in path]
#     city_counts = {city: all_cities.count(city) for city in set(all_cities)}
#     for path in paths:
#         destination_city = path[-1]
#         if city_counts[destination_city] == 1:
#             return destination_city
        
# paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]

# result = destCity(paths)

# print(result)

#3-masala

def maxProduct(nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
    
nums = [3,4,5,2]

result = maxProduct(nums)
print(result)