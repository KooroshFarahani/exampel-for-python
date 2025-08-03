"""یک لیست با ۱۰ عدد تصادفی بین ۱ تا ۱۰۰ بساز"""
import random

list1 = [random.randint(1, 100) for i in range(10)]
print (list1)