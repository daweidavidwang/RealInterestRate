from sympy import *


if __name__ == '__main__':
    print("please enter the month of repay");
    month = input();
    print("Please enter the mount of monthly repay")
    repay = input();
    print("Please enter the total mount of loan")
    loan = input();

    beta = symbols('beta');
    solution = solveset(Eq(repay*(1+beta)**month - repay,loan*beta*(1+beta)**month),beta,domain = S.Reals);
    for a in solution:
        if a >0 : print(12*a);

