# Generator
#Generator Function, Generator Expression
########################## Simple example #########
#Normal Function(return)
"""def normal_hello():
    return "Hello World"


#Generator Function
def gen_hello():
    yield "Hello World"

#normal
normal = normal_hello()
print("Normal func:", normal)

#generator
gen = gen_hello()
print("Generator", gen)"""

########### workin with generator function ################

"""#Generator Function
def gen_hello():
    yield "Hello World"

#generator
gen = gen_hello()
print("Generator", gen)
print(next(gen))
"""
############################################
#Generator with "next"
########################
"""def gen_hello():
    yield "Hello World"
    yield "Hello second World"
    yield "Hello third world"

gen = gen_hello()
print(next(gen))
print(next(gen))
print(next(gen))"""

############################################
#Generator with "next" with increasing value one by one
########################
"""def gen_hello():
    n = 1
    print("First world:", n)
    yield "Hello World"

    n += 1
    print("second World:", n)
    yield "Hello second World"

    n += 1
    print("second World:", n)
    yield "Hello third world"

    n += 1
    print("second World:", n)
    yield "Hello fourth world"

gen = gen_hello()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))"""
#################################################
"""def gen_power_two():
    number = 1
    while number < 20:
        yield number ** 2
        number += 1
num_power = gen_power_two()

print(next(num_power))
print(next(num_power))
print(next(num_power))
print(next(num_power))
print(next(num_power))
print(next(num_power))"""
##########################################
######By for condition #########
"""def gen_power_two():
    number = 1
    while number < 20:
        yield number ** 2
        number += 1
num_power = gen_power_two()

for i in num_power:
    print(i)"""
#########################################
#for list num
"""nums = [1, 2, 4, 5]
nums = [ num for num in range(1, 6)]
print(nums)
"""
#for generator nums
nums = [1, 2, 4, 5]
gen_nums = (num for num in range(1, 6))
print(gen_nums)
print(next(gen_nums))
print(next(gen_nums))
print(next(gen_nums))

for num in gen_nums:
    print("Number", num)



