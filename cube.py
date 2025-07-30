def cube(num):
    return num * num * num

def by_3(num):
    if num%3==0:
        return cube(num)
    else:
        return False
    
num = int(input("enter the number:"))

print(f"the {num} is {by_3(num)}")