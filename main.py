import re

while True:
    statement = input()
    statement = re.sub(r'(人类|人)','你', statement)
    statement = re.sub(r'(进化|变|变的)','生', statement)
    statement = re.sub(r'(猴子|猩猩)','你妈', statement)
    print(statement)

