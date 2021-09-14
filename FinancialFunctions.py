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


cfList = [20, 50, 90, 100, 2, 3, 400, -100, -50]
r = 0.05

def npv_calc(cfList, r):
    npv = 0
    for i in range(len(cfList)):
        npv += cfList[i] / ((1 + r) ** (i+1))
    return f"The Present Value is ${npv:,.2f}"
print(npv_calc(cfList,r))


# Ideally we want


def pv_calc_1(CF1, r):
    pv1 = CF1/ ((1 + (r/100))**1)
    return pv1
def pv_calc_2(CF2, r):
    pv1 = CF2/ ((1 + (r/100))**2)
    return pv2
def pv_calc_3(CF3, r):
    pv1 = CF3/ ((1 + (r/100))**3)
    return pv3

def pv_calc_0(pv1, pv2, pv3):
    npv = sum(pv1, pv2, pv3)
    return npv
present_value = dict()

for i in range(numPeriods):

    dict[i] = PV(i, r, )

present_value[0] = 20

    {
    "Year Zero / NPV": pv_calc_0,
    "Year One": pv_calc_1,
    "Year Two": pv_calc_2,
    "Year Three": pv_calc_3

}

print(present_value)



