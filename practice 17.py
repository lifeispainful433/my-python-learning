# 列表
numbers = [1, 5, 3, 9, 2]
print(max(numbers))  # 输出：9

# 元组
tuples = (10, 8, 15, 3)
print(max(tuples))   # 输出：15

words = ["cat", "elephant", "dog"]
print(max(words))              # 按字母：输出 "elephant" (e开头)
print(max(words, key=len))     # 按长度：输出 "elephant" (8个字母最长)

scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
# key=scores.get 意思是：别看名字，看他们对应的分数！
print(max(scores, key=scores.get))  # 输出：Bob (90分最高)
