def wrapper_function(num):
    def ad(func):
        def sum_of_two_num(num1):
            print(num + num1)
            return func()
        return sum_of_two_num
    return ad

@wrapper_function(1)
def send_num():
    print("Sending")


send_num(3)

