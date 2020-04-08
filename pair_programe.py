def MPF(income):
    if income/12 < 7100:
        MPF = 0

    elif income/12 >= 7100 and income/12 <=30000:
        MPF = income * 0.05

    elif income/12 > 30000:
        MPF = 1500 * 12

    return MPF

def Separate(income):
    net_income = income - MPF(income)
    net_chargeable_income = net_income - 132000
    if net_chargeable_income < 0:
        net_chargeable_income = 0

    return net_chargeable_income

def joint(husband_income,wife_income):
    net_chargeable_income = husband_income + wife_income - MPF(husband_income) - MPF(wife_income) - 264000
    if net_chargeable_income < 0:
        net_chargeable_income = 0

    return net_chargeable_income
    

def tax(net_chargeable_income):
    tax = 0
    if net_chargeable_income >= 50000:
        tax += 1000
        if net_chargeable_income >= 100000:
            tax += 3000
            if net_chargeable_income >= 150000:
                tax += 5000
                if net_chargeable_income >= 200000:
                    tax +=7000
                    if net_chargeable_income > 200000:
                        tax += (net_chargeable_income -200000)*0.17
                else: 
                    tax += (net_chargeable_income-150000)*0.14
            else:
                tax += (net_chargeable_income-100000) *0.1
        else:
            tax += (net_chargeable_income-50000) *0.06
    else:
        tax += net_chargeable_income *0.02

    return(tax)

def main():

    try:
        husband_income = float(input('Enter husband income :'))
        wife_income = float(input('Enter wife income :'))

        if husband_income < 0:
            raise ValueError("Please enter a number greater than zero")

        if wife_income < 0:
            raise ValueError("Please enter a number greater than zero")       

        print("husband's MPF is:",MPF(husband_income))
        print("wife's MPF is:",MPF(wife_income))


        print("The Separate tax of husband is:",tax(Separate(husband_income)))
        print("The Separate tax of wife is:",tax(Separate(wife_income)))
        print("The joint Tax is:",tax(joint(husband_income,wife_income)))

        if tax(Separate(husband_income)) + tax(Separate(wife_income)) < tax(joint(husband_income,wife_income)):
            print("Recommend to use spearate tax")
        else:
            print("Recommend to use joint tax")

    except ValueError:
        print("income must be positive")
    except:
        print("input error")

if __name__ == '__main__':
    main()









     
