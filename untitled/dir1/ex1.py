print("Hello World!")
print("Hello Again")
print("I like typing this.")
print("This is fun.")
print('Yay! Printing.')
# print ("I'd much rather you 'not'.")
# print ('I "said" do not touch this.')
print("Roosters", '100 - 25 * 3 % 4', "Roosters", 100.01 - 25 * 3 % 4)
my_name = 'billa'
print("my name is %s", my_name)


def fun1(arg1):
    k = 4
    x = "arma"
    print((arg1 + x) * k)


def fun2(*arg1):
    arg1 = arg1 + 1


k = 1
fun2(k)
print(k)
