import random
import re
import sys
import time


# def remove_dup(nums):
#     temp = []
#     temp_set = set()
#     for i in nums:
#         if i not in temp_set:
#             temp.append(i)
#             temp_set.add(i)
#     return temp

# a = [1,1,2,10,6,10,3,12,12]
# print(remove_dup(a))

# import pickle
#
# a = [1,1,2,10,6,10,3,12,12]
# my_deep_copy = lambda obj: pickle.loads(pickle.dumps(obj))
# b = my_deep_copy(a)
# print(a)

#
# import copy
#
# a = [1,2,3]
#
# b = [a,9,10]
#
# c = copy.deepcopy(b)
# a.append(9)
# print(b)
# print(c)


# def multiply():
#     return [lambda x: i * x for i in range(4)]
#
# print([m(100) for m in multiply()])


# def count(nums):
#     temp = dict()
#     for i in nums:
#         count = 0
#         if i not in temp:
#             for j in nums:
#                 if i == j:
#                     count += 1
#             temp[i] = count
#     return temp
#
# def count_1(nums):
#     result = {}
#     for i in nums:
#         result[i] = result.get(i, 0) + 1
#     return result
#
# a = [1,2,2,3,5,666,7,7,8,811,1,1,2]
# c = count_1(a)
# print(c)


import os

# p = r'C:\Users\19125\Desktop\2024-2月面试\test'
# g = os.walk(p)
# for path, dir_list, file_list in g:
#     for dir_name in dir_list:
#         print(os.path.join(path, dir_name))
#     for file_name in file_list:
#         print(os.path.join(path, file_name))

# def travel(path):
#     for item in os.listdir(path):
#         full_path = os.path.join(path, item)
#         if os.path.isdir(full_path):
#             print(full_path)
#             travel(full_path)
#         else:
#             print(full_path)
# travel(p)

# def list_directories(path):
#     # 获取指定目录下的所有文件和文件夹名称
#     for entry in os.listdir(path):
#         # 获取完整的文件或文件夹路径
#         full_path = os.path.join(path, entry)
#         # 判断当前条目是否是文件夹
#         if os.path.isdir(full_path):
#             print(f"文件夹: {full_path}")
#             # 递归调用以遍历文件夹
#             list_directories(full_path)
#         else:
#             print(f"文件: {full_path}")
#
# list_directories(p)


# from functools import lru_cache
#
# @lru_cache()
# def change_money(total):
#     if total == 0:
#         return 1
#     if total < 0:
#         return 0
#     return change_money(total - 2) + change_money(total - 3) + \
#         change_money(total - 5)
#
# print(change_money(99))


# import datetime
# def distance_days(year, month, day):
#     target_date = datetime.date(year, month, day)
#     year_begin = datetime.date(year, 1, 1)
#     return (target_date - year_begin).days + 1
#
# print(distance_days(2024, 2,8))


# a = {'a':1, 'b':'3', 'd':[1,2]}
# b = a.copy()
# a['c'] = 5
# a['d'].append(5)
# print(b)
# print(a)



# from functools import wraps
# from time import time
#
#
# def record_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}执行时间: {time() - start}秒')
#         return result
#
#     return wrapper
#
# @record_time
# def func1():
#     pass
#
# func1()

# a = [1,2,3]
# b = [4,5,6]
# c = {'a':1, 'd':3, 'g':6}
# a.extend(b)
# b.extend(c)
# print(a)
# print(b)
#

# class A:
#     def who(self):
#         print('A', end='')
#
# class B(A):
#     def who(self):
#         super(B, self).who()
#         print('B', end='')
#
# class C(A):
#     def who(self):
#         super(C, self).who()
#         print('C', end='')
#
# class D(B, C):
#     def who(self):
#         super().who()
#         super(D, self).who()
#         print('D', end='')
#
# item = D()
# item.who()


# message = 'hello, world!'
# print(message.replace('ll', 'O'))


# import re
#
# message = 'hello, world!'
# pattern = re.compile('[aeiou]')
# print(pattern.sub('#', message))


# import re
#
# filenames = ['a12.txt', 'a8.txt', 'b10.txt', 'b2.txt', 'b19.txt', 'a3.txt']
#
# # 步骤1：字符串替换，补位
# p = re.compile(r'(\d+)')
# filenames_padded = []
# for filename in filenames:
#     padded = p.sub(lambda m: m.group().rjust(6, '0'), filename)
#     filenames_padded.append(padded)
#
# print(filenames_padded)
# # 步骤2：排序
# filenames_sorted = sorted(filenames_padded)
# print(filenames_sorted)
# # 步骤3：字符串替换，去掉补位
# filenames_final = []
# for filename in filenames_sorted:
#     final = p.sub(lambda m: str(int(m.group())), filename)
#     filenames_final.append(final)
#
# print(filenames_final)
#

# a = 3
# b = 10
# print(random.randint(a, b))
# x = [1,2,3,4,5,6]
#
#
# c = random.choices(x, k=3, )
# print(c)
#
# d = random.sample(x, k=4)
# print(d)
#
# f = random.uniform(3, 8)
# print(f)
#
# g = 323
# print(int(g))


# with open('./hamble/hamble.html', 'r') as file:
#     for data in iter(lambda: file.read(100), ''):
#         print(data)

        

# def find(nums:list):
#     result_count = {}
#     list_length = len(nums)
#     for item in nums:
#         result_count[item] = result_count.get(item, 0) + 1
#         if result_count[item] > list_length // 2:
#             return item
#     return None
#
# a = [1,2,3,4,5,5,5,6,5,5,5]
# print(find(a))
# print(isinstance(a, list))
# b = '12345'
# print(b[::-1])
# print(''.join(reversed(b)))
#
# def reverse_string(content):
#     if len(content) <= 1:
#         return content
#     return reverse_string(content[1:]) + content[0]
#
# print(reverse_string(b))

import threading

# def test(value1, value2=None):
#     print("%s threading is printed %s, %s"%(threading.current_thread().name, value1, value2))
#     time.sleep(2)
#     return 'finished'
#
# def test_result(future):
#     print(future.result())
#
# if __name__ == "__main__":
#     import numpy as np
#     from concurrent.futures import ThreadPoolExecutor
#     threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
#     for i in range(0,10):
#         future = threadPool.submit(test, i, i + 1)
#         future.add_done_callback(test_result)
#         # print(future.result())
#
# threadPool.shutdown(wait=True)




# def test(value1, value2=None):
#     print("%s threading is printed %s, %s"%(threading.current_thread().name, value1, value2))
# #     time.sleep(2)
#
#
# if __name__ == "__main__":
#     import numpy as np
#     from concurrent.futures import ThreadPoolExecutor
#     threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="test_")
#     items = [i for i in range(10)]
#     items_1 = [i+1 for i in range(10)]
#     threadPool.map(test, items,items_1)
#     threadPool.shutdown(wait=True)


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_1 = len(num1)
        len_2 = len(num2)

        # 补0
        if len_1 < len_2:
            for _ in range(len_2-len_1):
                num1 = '0'+ num1
        elif len_1 > len_2:
            for _ in range(len_1-len_2):
                num2 = '0'+ num2


        num_length = len(num1)
        i ,j = num_length-1, num_length-1
        res = ''
        jump = 0
        for _ in range(num_length):
            if jump:
                result = int(num1[i]) + int(num2[j]) + 1
            else:
                result = int(num1[i]) + int(num2[j])
            if result >= 10:
                jump = 1
                # 只保留各位数
                result = result - 10
            else:
                jump = 0
            res = str(result) + res
            i -= 1
            j -= 1
        return res


# from concurrent.futures import ThreadPoolExecutor
#
# # 定义一个函数，它将被线程池中的线程执行
# def process_item(item):
#     # 对item进行处理
#     return item * 2
#
#
# # 创建一个线程池
# with ThreadPoolExecutor(max_workers=5) as executor:
#     # 创建一个迭代器，其中包含你想并发处理的项
#     items = [1, 2, 3, 4, 5]
#
#     # 使用map函数将process_item函数应用到线程池中的每个项
#     results = executor.map(process_item, items)
#     print(results)
#     # 打印结果
#     for result in results:
#         print(result)

print(Solution().addStrings('1','9'))