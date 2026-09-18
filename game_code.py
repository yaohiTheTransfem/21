import random
def user_input(prompt):
    user_nums = []
    for i in range(3):
        try:
            fetch_integer = int(input(prompt))
            while fetch_integer < 0 or fetch_integer > 19:
                fetch_integer = int(input(prompt))
            user_nums.append(fetch_integer)
        except ValueError:
            print("Error: Not an integer): ")
    return user_nums


def multiplication_gimmick(ai_integers, user_integers):
    ai_integers = list(ai_integers)
    user_integers = list(user_integers)
    for i in range(9):
        j = i % 3
        k = i//3

        if ai_integers[k] == user_integers[j]:
            ai_integers[k] = ai_integers[k] + user_integers[j]
            user_integers[j] = ai_integers[k] + user_integers[j]
        else:
            pass
    return ai_integers, user_integers


def ai():
    def fetch_integers():
        int0 = random.randint(0,19)
        int1 = random.randint(0,19)
        int2 = random.randint(0,19)
        return int0, int1, int2
    
    all_integers = fetch_integers()
    total = sum(all_integers)
    while total >= 21:
       all_integers = fetch_integers()
       total = sum(all_integers)
    return all_integers

def winner(user_output, ai_output):   
    if ai_output > user_output:
        print("The AI wins!")
    elif user_output > ai_output:
        print("The user wins!") 
    elif user_input == ai_output:
        print("It's a draw!")
    else:
        print("It's a draw!")

def main():
    
    ##fetches user's numbers and generates numbers using the state of the art AI
    user_integers = user_input("Please enter in your integers: ")
    while sum(user_integers) >= 21:
        user_integers = user_input("Please enter in valid integers: ")
    
    
    ai_output = ai()
    ai_output, user_integers = multiplication_gimmick(ai_output, user_integers)
    
    
    ai_total = sum(ai_output)
    user_total = sum(user_integers)
    winner(user_total, ai_total)


if __name__ == "__main__":
    main()