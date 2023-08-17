def collatz(number):
    if number% 2==0:
        result=number//2
    else:
        result=3*number+1
    print(result)
    return result
def main():
    user_input=int(input("enter an integer"))
    while user_input!=1:
        user_input=collatz(user_input)
main()
        