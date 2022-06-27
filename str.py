# 单引号、双引号、三引号
'''
word = '字符串'
sentence = "这是一个句子"
paragraph = """
        这是一个段落
        可以由多行组成
"""
print(word)
print(sentence)
print(paragraph)
'''

'''
# my_str = "I'm a student"
my_str = 'I\'m a student'      # \转义
print(my_str)
'''
'''
# my_str = "Json said \"I like you\""
my_str = 'Json said "I like you"'
print(my_str)
'''

str = "jiaxing"
'''
print(str)
print(str[0])
print(str[0:4])    # [起始位置：结束位置：步进值]
print(str[0:7:2])
'''
'''
print(str[5:])
print(str[:5])

print(str + "，你好")
print(str * 3)
'''
print("hello\njiaxing")         # 使用反斜杠，实现转义字符的功能
print(r"hello\njiaxing")        # 在字符串前面直接加r，表示直接显示原始字符，不进行转义