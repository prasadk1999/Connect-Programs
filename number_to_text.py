import sys

result = []
first_9_number = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
ten_to_nineteen = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                   'Nineteen']
multiples_of_ten = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def position_of_thousands(self, l, position_of_digit, suffix):  # Converts thousands and positions of thousands to text
    # position_of_digit means the index at which the digit exists
    temp_number = l_result = ''
    # First we take out the digits at thousands and ten thousands place
    if l >= position_of_digit + 2:  # if there exists a digit at ten thousandth place
        temp_number = self[position_of_digit:position_of_digit + 2]
    elif l == position_of_digit + 1:  # if this is the last digit of the number
        temp_number = self[position_of_digit]
    # Convert the number to text according to the number
    if len(temp_number) == 2:  # executes if there number is in range 10000-99999, basically if ten_thousandth digit
        # exists!
        if temp_number[1] != '1':  # This function does not execute numbers from 10-19
            l_result = first_9_number[int(temp_number[0]) - 1]
            result.append(l_result + suffix if l_result is not None else '')
    else:
        l_result = first_9_number[int(temp_number[0]) - 1]
        result.append(l_result + suffix if l_result is not None else '')


def position_of_ten_thousands(self, suffix):  # Converts digits at ten thousand and positions of ten thousands to text
    if self[0] == '0':  # this if is only for numbers which are multiples of 10 i.e 10,20,30 etc
        if self[1] == '1':  # only 10 number is executed here
            return ten_to_nineteen[int(self[0])] + suffix
        else:  # 20-90 numbers executed here
            return multiples_of_ten[int(self[1]) - 2] + suffix
    else:  # numbers except 10-19 and multiples of 10 are executed here
        if self[1] == '1':
            return ten_to_nineteen[int(self[0])] + suffix
        else:
            return multiples_of_ten[int(self[1]) - 2]


def units(self, l):  # Converts unit digit to text
    if l > 1:  # if 2 digits are given as input
        if self[1] != '1':
            return first_9_number[int(self[0]) - 1]
    else:  # if only one digit is given as input
        return first_9_number[int(self[0]) - 1]


def tens(self):
    # if value at tens place is 1, then return statement will be based on value at unit's place
    if self[1] == '1':
        return ten_to_nineteen[int(self[0])]
    else:
        return multiples_of_ten[int(self[1]) - 2]


def hundreds(self):
    temp = first_9_number[int(self) - 1]
    return temp + ' Hundred' if temp is not None else ''


def display(self):
    for i in range(len(self) - 1, -1, -1):
        if i == 2:
            print(self[i], end=' and ')
        elif self[i] is not None:
            print(self[i], end=' ')


def indian_number_system(self):
    suffixes = [' Thousand', ' Lakh', ' Crore', ' Arab', ' Kharab', ' Nil', ' Padma', ' Shankh']
    counter_of_suffix = 0
    thousandth_position = 3
    ten_thousandth_position = 4
    n = self[::-1]  # Reverse the number
    l = len(n)
    for i in range(0, 3):
        if n[i] != '0' and i < l:
            # Units Place
            if i == 0:
                if l >= 2:
                    result.append(units(n[i:i + 2], l))
                else:  # if only 1 digit exists
                    result.append(units(n[i], l))
                continue
            # Tens Place
            if i == 1:
                result.append(tens(n[i - 1:i + 1]))
                continue
            # Hundreds Place
            if i == 2:
                result.append(hundreds(n[i]))
                continue
    for i in range(3, l):
        if n[i] != '0':
            if i == thousandth_position:
                position_of_thousands(n, l, i, suffixes[counter_of_suffix])
                thousandth_position = thousandth_position + 2
                continue
            if i == ten_thousandth_position:
                result.append(position_of_ten_thousands(n[i - 1:i + 1], suffixes[counter_of_suffix]))
                ten_thousandth_position = ten_thousandth_position + 2
                counter_of_suffix = counter_of_suffix + 1
                continue
        else:
            if i == thousandth_position:
                thousandth_position = thousandth_position + 2
                continue
            if i == ten_thousandth_position:
                ten_thousandth_position = ten_thousandth_position + 2
                counter_of_suffix = counter_of_suffix + 1
                continue
    display(result)


def international_number_system(self):
    suffixes = [' Thousand', ' Million', ' Billion', ' Trillion', ' Quadrillion', ' Quintillion']
    counter_of_suffix = 0
    thousandth_position = 3
    ten_thousandth_position = 4
    hundred_thousandth_position = 5
    n = self[::-1]  # Reverse the number
    l = len(n)
    for i in range(0, 3):
        if n[i] != '0' and i < l:
            # Units Place
            if i == 0:
                if l >= 2:
                    result.append(units(n[i:i + 2], l))
                else:
                    result.append(units(n[i], l))
                continue
            # Tens Place
            if i == 1:
                result.append(tens(n[i - 1:i + 1]))
                continue
            # Hundreds Place
            if i == 2:
                result.append(hundreds(n[i]))
                continue
    for i in range(3, l):
        if n[i] != '0':
            if i == thousandth_position:  # this section will only execute when the index is in position of
                # thousands, like 4th,7th,10th, etc.
                position_of_thousands(n, l, i,
                                      suffixes[counter_of_suffix])  # converts the digit passed into appropriate text
                thousandth_position = thousandth_position + 3
            if i == ten_thousandth_position:
                result.append(position_of_ten_thousands(n[i - 1:i + 1], suffixes[counter_of_suffix]))
                ten_thousandth_position = ten_thousandth_position + 3
            if i == hundred_thousandth_position:
                if n[i - 1] == '0' and n[i - 2] == '0':  # for numbers like 100000,2000000, etc
                    result.append(hundreds(n[i]) + suffixes[counter_of_suffix])
                else:
                    result.append(hundreds(n[i]) + ' and')
                hundred_thousandth_position = hundred_thousandth_position + 3
                counter_of_suffix = counter_of_suffix + 1
        else:  # if, if part does not get executed(if there are zeroes), then this part ensures that position
            # variables are properly adjusted.
            if i == thousandth_position:
                thousandth_position = thousandth_position + 3
            if i == ten_thousandth_position:
                ten_thousandth_position = ten_thousandth_position + 3
            if i == hundred_thousandth_position:
                hundred_thousandth_position = hundred_thousandth_position + 3
                counter_of_suffix = counter_of_suffix + 1

    display(result)


if __name__ == '__main__':
    result = []
    while 1:
        number = int(input('Enter a number:'))
        print('1. Indian Number system\n2.) US Number system\n3.)Quit')
        choice = int(input('Enter choice:'))
        if choice == 1:
            if number < 0:
                print('Minus', end=' ')
            indian_number_system(str(abs(number)))
        elif choice == 2:
            if number < 0:
                print('Minus', end=' ')
            international_number_system(str(abs(number)))
        elif choice == 3:
            sys.exit(1)
        else:
            print("Invalid Input!")
