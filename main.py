import random


def bill(b, number):
    result = round(b / number, 2)

    if result.is_integer():
        return int(result)
    else:
        return result


print('Enter the number of friends joining (including you):')
n = int(input())

friends_dict = dict()

if n > 0:
    print('\nEnter the name of every friend (including you), '
          'each on a new line:')

    for i in range(n):
        user_name = input()
        friends_dict[user_name] = 0

    print('\nEnter the total bill value:')
    final_bill = int(input())

    for i in friends_dict:
        if bill(final_bill, len(friends_dict)) % 2 == 0:
            friends_dict[i] = int(bill(final_bill, len(friends_dict)))
        else:
            friends_dict[i] = bill(final_bill, len(friends_dict))

    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()

    if answer == 'Yes':
        lucky = random.choice(list(friends_dict))
        print(f'\n{lucky} is the lucky one!\n')

        friends_dict[lucky] = 0

        for i in friends_dict:
            if i != lucky:
                friends_dict[i] = bill(final_bill, len(friends_dict) - 1)

        print(friends_dict)
    else:
        print('\nNo one is going to be lucky\n')
        print(friends_dict)
else:
    print('\nNo one is joining for the party')
