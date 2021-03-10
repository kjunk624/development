# import re
# from typing import Pattern

# # for i in range(2,10):
# #     for j in range(1,10):
# #         print(f'{i}**{j}={i**j:10}')
        
# Pattern_string = r'파이썬'
# pattern = re.compile(Pattern_string)

# # re.search(pattern,'파이썬')
# re.search('파이썬', '파이썬 프로그래밍')
# if re.match:
#     print('문자열에 패턴과 일치하는 텍스트가 존재 함')
# else:
#     print('문자열에 패턴과 일치하는 텍스트가 존재하지 않음 ')
    
# match=re.search(pattern,'즐거운 파이썬 프로그앰')
# match.group()
# print(match)

# sample = '1789Python김파이fog'
# pattern = re.compile(r'[가-힣]{2,4}')
# match = re.search(pattern,sample)
# match.group()
# print(match.group())


# sample = '우리나라에 이런 번호가 있을까 010-9349-5468 do you think there is the number whitch 010-222-333?'
    
# pattern = re.compile(r'01\d-\d{4}-\d{4}')
# match = re.search(pattern, sample)
# match.group()
# print(match.group())


def forloop():
    lists = [('a','s','a'),('d','f','d'),('r','o','r')]

    global list

    for list in lists:
        list_print = ' '
        list_print += str(list[0]) + str(list[1])
        print(list_print)
        ans = input('which one?:')
        if ans == list[2]:
            print('good')
        else:
            print('bad')

        list += list


forloop()