# Basics

# text = 'Hello Python!'
# path = text[6] + 'a' + text[8:10]
# print(path)

# letter = 'zzzzzzz'
# print(letter.upper())

# float_rey = 1000/7
# req = 'gdfgshsfdhs {0:1.4f}'.format(float_rey)
# print(req)

# tab = '''
# {0:15.4f} {1:15.4f} {2:15.4f} {3:15.4f}'
# {4:15.4f} {5:15.4f} {6:15.4f} {7:15.4f}
#       '''.format(12.23456, 65.65789 , 123.123454 , 543.6457878, 43.546789 , 2.435698, 568.12347, 98.234256)
# print(tab)

# letter =[123 , 23.2345 , 'a' , ' dog', 6547.234]
# ret = letter[1:4]
# gat = [65756 , 5647.1235 , 'key']
# final = gat + ret
# print(final)
# # print(letter)

# dictionary = {
#     'CPU': 'r7 1700',
#     'GPU': 'GTX 1160TI',
#     'motherboard': 'a320',
#     'RAM': 16,
#     'Power': '500W'
# }
# print(dictionary)

# tuple = ('r7 1700' , 'gtx 1660ti' , '500w', '16 RAM')
# CPU , GPU , Power , RAM = tuple
# print(CPU , GPU , Power, RAM)

# list_sets_text = {'ade' , 'error' , 'name' , 'sets'}
# list_text = set(list_sets_text)
# print(type(list_text))
# print(list_text )

# x = 12
# y = 10
# print(x>y)
# print(x<y)
# print(x >= y)
# print(x<=y)
# print(x == y)
# print( x!=y)

# print('X' > 'x')
# print(ord('X'))
# print(ord('x'))

# number = input('Enter any number')
# if number == '7':
#     print('7 is lucky number! Today is your lucky day')
# else:
#     print('Thank you! Have a nice day')

# number = input('Enter an integer number')
# if int(number) % 2 == 0 :
#     print('The number is event')
# else:
#     print('The number is odd')

# n = [1 , 2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
# for nam in n:
#     if nam % 2 == 0:
#         print(nam)

# tuple_list = [('a', 'b' , 1) , ('c' , 'h' , 3) , ('r' , 'o', 6)]
# # for item in tuple_list:
# #     print(item)
# for letter_1 , letter_2 , letter_3 in tuple_list:
#     print(letter_1 )
#     print(letter_2)
#     print(letter_3)


# dictionary = {'key': 'val', 'key1': 'val2'}
# for n in dictionary.items():
#     print(n)
#     for n in dictionary.keys():
#         print(n)
#         for n in dictionary.values():
#             print(n)

# te = input('number')
# for _ in range(int(te)):
#     print('Hello!')

# letter = 'asddfghjkl'
# for index , letter1 in enumerate(letter):
#     print(index , letter1)
# dick = {1 :'d' , 2: 'e' , 5: 'r'}
# print('q' in dick.values())

# dfg = 'asdfghkj'
# for x in dfg:
#     print(ord(x))

# greeting = 'Hello!'
# letter_list = []
# for letter in greeting:
#     letter_list.append(letter)
# print(letter_list)
# letter_list = [ letter for letter in greeting]
# print(letter_list)
# number_list = [number for number in '1034562']
# print(number_list)
# number_list1 = [number1 **2 for number1 in range(5,10)]
# print(number_list1)
# number_list3 = [((num**3)-2) for num in range(0,11)]
# print(number_list3)

# number_list = [6,234,45,-32 , -12, 67, 343]
#  new_list = [number for number in number_list if number>0]
# #print(new_list)
# new_list = ['+' if number >0 else '-' for number in number_list]
# print(new_list)


# string = "This is amazing world"
# for word in list(string.split()):
#     fdg = (" ".join(word[1]))
#     print(fdg)


# greetings = ['hello', 'hi', 'hey', 'hola']
# for letter in greetings:
#     letter2 = ((list(letter[1])))
#     print(end = letter2)

# dick = [1 ,  3 , 8]
# list = {key : value**2 for key , value in dick.items()}
# print(list)

# list = { number : number **2 for number in dick}
# print(list)

# for number in range(10):
#     count = 0
#     emoticons = ''
#     while count <= number:
#         emoticons += '\U0001f600'
#         count += 1
#     print(emoticons)

# for number in range(1,11):
#     print('\U0001f600'* number)

# count = 0
# while count < 11:
#     print('\U0001f600'* count)
#     count+=1

# Function

# def print_greeting():
#     '''
#     print 'Hello!' text
#     :return:None
#     '''
#     print('Hello!')
# print_greeting()
# help(print_greeting)

# def print_greeting_name(name = 'dfgh'):
#     print('Hello ' + name + '!')
# print_greeting_name('jack')
#
# print_greeting_name()

# def sum_of_two_numbers(a=0 ,b=0 ):
#     '''
#
#     :param a:
#     :param b:
#     :return:
#     '''
#     return a + b
# x = sum_of_two_numbers()
# print(x)

# def is_helli_in_text(text):
#     if 'hello' in text:
#         return True
#     else:
#         return False
# print(is_helli_in_text('sey  everyone'))

# def in_hello_in_text(text):
#     return 'hello' in text.lower()
# print(in_hello_in_text('sey  everyone'))

# def greetng_of_depends_on_gender(name , gender):
#
#     if gender =='male':
#         print('Hello ' + name)
#     elif gender == 'female':
#         print('hello ' + ' You are so nice')
#         return gender
#     else:
#         print('hello ' + name + ' dfgdsdfsh')
#         return gender
#
#
# return_value = greetng_of_depends_on_gender('Jack' , 'male')
# return_value = greetng_of_depends_on_gender('Jack' , 'female')
# return_value = greetng_of_depends_on_gender('Jacka' , 'bfale')

# def cat_voice(text = 'Meow!'):
#     print(text)
# cat_voice('Meow!')
#
# cat_voice()
#
# def dog_voice(text1 ='Woof!'):
#     print(text1)
# dog_voice('Woof!')
#
# dog_voice()

# def get_voice(text = 'Hello Python!'):
#     print(text)
# get_voice()

# def percent_product(percant , *args):
#     product = 1
#     for number in args:
#         product = product * number
#     return product / 100 * percant
#
# print(percent_product(20 ,4342))

# def new_kwei(**kwargs):
#     print(kwargs)
# new_kwei(firct=1 , second=2 , third=3)

# def hello_whis_kwargs(**kwargs):
#     if 'name' in kwargs:
#         print('Hello! Nice to meet you,{}'.format(kwargs['name']))
#     else:
#         print('Hello! What is yuor name?')
# hello_whis_kwargs(gender = 'male' , age= 23 , name = 'kirill')
# hello_whis_kwargs(gender = 'male' , age= 23 )

# def hello_whis_greeting_and_kwargs(greeting,**kwargs):
#     if 'name' in kwargs:
#         print('{}! Hello! Nice to meet you,{}'.format(greeting,kwargs['name']))
#     else:
#         print('{}! Hello! What is yuor name?'.format(greeting))
# hello_whis_greeting_and_kwargs('Hi' ,gender = 'male' , age= 23 , name = 'kirill')
# hello_whis_greeting_and_kwargs('god',gender = 'male' , age= 23 )

# def func_with_args_and_kwargs(*args , **kwargs):
#     print('I would like {} {}'.format(args[0] , kwargs['food']))
# func_with_args_and_kwargs('one' , 'two' , drink='coffee' , food='sandwich')

# def is_cat_here(*args):
#     if 'cat' in args():
#         return True
#     else:
#         return False
# print(is_cat_here( 'cat' , 'hello' , 'hi' , 'dog'))

# def is_item_here(item, *args):
#     item_in_args = ('one' , 'two')

# def your_favorite_color(**kwargs):
#     if 'color' in kwargs:
#         print('My favorite color is {}'.format(kwargs['color']))
#     else:
#         print('What your favorite color?')
#     if 'my_color' in kwargs:
#         print('favorite color is{}'.format(kwargs['my_color']))
#     else:
#         print('but {} is also pretty good!'.format(kwargs['color']))
# your_favorite_color(color='red' , my_color='blue')
