# NPV Formula

#CF1 = input("What is your Cash Flow in Year One? ")
def perp_npv(CF1,rate):
    npv = CF1/(rate/100)
    return f"The Present Value of the Perpetuity is ${npv:,.2f}"

def grow_perp_npv(CF1, r, g):
    npv = CF1 / ((r/100)-(g/100))
    return f"The Present Value of the Growing Perpetuity is ${npv:,.2f}"

print(perp_npv(1000,5))
print(grow_perp_npv(1000,5,2))


cfList = [20, 50, 90]
r = 0.05

def npv_calc(cfList, r):
    npv = 0
    for i in range(len(cfList)):
        npv += cfList[i] / ((1 + r) ** (i+1))
    return f"The Present Value is ${npv:,.2f}"
print(npv_calc(cfList,r))





