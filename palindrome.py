def check_palindrome(number):
    flag = 0
    for i, j in zip(range(len(number)), range(len(number) - 1, -1, -1)):
        if i != j:
            if number[i] != number[j]:
                flag = 1
                break
    if flag == 1:
        print('Not a Palindrome Number')
    else:
        print("Palindrome Number")


if __name__ == '__main__':
    num = input('Enter a string:')
    if num.isnumeric():
        if int(num) < 0:
            check_palindrome(str(abs(int(num))))
    elif len(str(num)) < 2 or num == 0:
        print('Cannot check for palindrome')
    else:
        check_palindrome(str(num))