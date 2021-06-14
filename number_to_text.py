units_place = None
tens_place = None
hundred_place = None
thousand_place = None
ten_thousand_place = None
lakh_place = None
ten_lakh_place = None
crore_place = None
ten_crore_place = None
result = []


def first_9_numbers_to_word(self):
    first_9_number = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    for i in range(1, 10):
        if self == str(i): return first_9_number[i - 1]


def ten_to_nineteen_to_word(self):
    ten_to_nineteen = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                       'Nineteen']
    for i in range(0, 10):
        if self == str(i): return ten_to_nineteen[i]


def multiples_of_ten_to_word(self):
    multiples_of_ten = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    for i in range(2, 10):
        if self == str(i): return multiples_of_ten[i - 2]


def units(self, l):
    if l > 1:  # if 2 digits are given as input
        if self[1] == '1':
            pass
        else:
            return first_9_numbers_to_word(self[0])
    else:  # if only one digit is given as input
        return first_9_numbers_to_word(self[0])


def tens(self):
    # if value at tens place is 1, then return statement will be based on value at unit's place
    if self[1] == '1':
        return ten_to_nineteen_to_word(self[0])
    else:
        return multiples_of_ten_to_word(self[1])


def hundreds(self):
    return first_9_numbers_to_word(self) + ' Hundred'


def thousands(self):
    if len(self) == 2:
        if self[1] != '1':
            return first_9_numbers_to_word(self[0]) + ' Thousand'
    else:
        return first_9_numbers_to_word(self[0]) + ' Thousand'


def ten_thousands(self):
    if self[0] == '0':
        if self[1] == '1':
            return ten_to_nineteen_to_word(self[0]) + ' Thousand'
        else:
            return multiples_of_ten_to_word(self[1]) + ' Thousand'
    else:
        if self[1] == '1':
            return ten_to_nineteen_to_word(self[0]) + ' Thousand'
        else:
            return multiples_of_ten_to_word(self[1])


def lakhs(self):
    if len(self) == 2:
        if self[1] != '1':
            return first_9_numbers_to_word(self[0]) + ' Lakh'
    else:
        return first_9_numbers_to_word(self[0]) + ' Lakh'


def ten_lakhs(self):
    if self[0] == '0':
        if self[1] == '1':
            return ten_to_nineteen_to_word(self[0]) + ' Lakh'
        else:
            return multiples_of_ten_to_word(self[1]) + ' Lakh'
    else:
        if self[1] == '1':
            return ten_to_nineteen_to_word(self[0]) + ' Lakh'
        else:
            return multiples_of_ten_to_word(self[1])


def crores(self):
    if len(self) == 2:
        if self[1] != '1':
            return first_9_numbers_to_word(self[0]) + ' Crore'
    else:
        return first_9_numbers_to_word(self[0]) + ' Crore'


def ten_crores(self):
    if self[0] == '0':
        if self[1] == '1':
            return ten_to_nineteen_to_word(self[0]) + ' Crore'
        else:
            return multiples_of_ten_to_word(self[1]) + ' Crore'
    else:
        if self[1] == '1':
            return ten_to_nineteen_to_word(self[0]) + ' Crore'
        else:
            return multiples_of_ten_to_word(self[1])


def display(self):
    for i in range(len(self) - 1, -1, -1):
        if i == 2:
            print(self[i], end=' and ')
        elif self[i] is not None:
            print(self[i], end=' ')


def indian_number_system(self):
    global hundred_place, tens_place, units_place, thousand_place, ten_thousand_place, lakh_place, ten_lakh_place, crore_place, ten_crore_place, result
    n = self[::-1]  # Reverse the number
    l = len(n)
    for i in range(0, l):
        if n[i]!='0':
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

            # Thousands Place
            if i == 3:
                if l >= 5:  # l>=5 because to know if there is a digit after thousands place
                    result.append(thousands(n[i:i + 2]))
                elif l == 4:
                    result.append(thousands(n[i]))
                continue
            # Ten Thousands Place
            if i == 4:
                result.append(ten_thousands(n[i - 1:i + 1]))
                continue
            # Lakhs Place
            if i == 5:
                if l >= 7:
                    result.append(lakhs(n[i:i + 2]))
                elif l == 6:
                    result.append(lakhs(n[i]))
                continue
            # Ten Lakhs Place
            if i == 6:
                result.append(ten_lakhs(n[i - 1:i + 1]))
                continue
            # Crore Place
            if i == 7:
                if l >= 9:
                    result.append(crores(n[i:i + 2]))
                elif l == 8:
                    result.append(crores(n[i]))
                continue
            if i == 8:
                result.append(ten_crores(n[i - 1:i + 1]))
                continue
    display(result)


def millions(self):
    if len(self) == 2:
        if self[1] != '1':
            return first_9_numbers_to_word(self[0]) + ' Million'
    else:
        return first_9_numbers_to_word(self[0]) + ' Million'


def international_number_system(self):
    n = self[::-1]  # Reverse the number
    l = len(n)
    for i in range(0, l):
        if n[i]!='0':
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
            # Thousands Place
            if i == 3:
                if l >= 5:  # l>=5 because to know if there is a digit after thousands place
                    result.append(thousands(n[i:i + 2]))
                elif l == 4:
                    result.append(thousands(n[i]))
            # Ten Thousands Place
            if i == 4:
                result.append(ten_thousands(n[i - 1:i + 1]))
            # Hundred Thousands Place
            if i == 5:
                if n[i - 1] != '0' and n[i - 2] != '0':
                    result.append(hundreds(n[i]))
                else:
                    result.append(hundreds(n[i]) + ' Thousand')
            # million place
            if i == 6:
                if l >= 5:  # l>=5 because to know if there is a digit after thousands place
                    result.append(millions(n[i:i + 2]))
                elif l == 4:
                    result.append(millions(n[i]))
            #ten million place
            if i==7:
                result.append(ten_thousands(n[i - 1:i + 1]))
    display(result)


if __name__ == '__main__':
    result = []
    number = input('Enter a number:')
    print('1. Indian Number system\n2.) US Number system\n')
    choice = int(input('Enter choice:'))
    if choice == 1:
        indian_number_system(number)
    elif choice == 2:
        international_number_system(number)
    else:
        print('Invalid Input!!')
