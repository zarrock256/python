import math

def shorter(result):                #sprowadza ułamek do prostszej postaci
    if result[0]%result[1] == 0:
        return result[0]/result[1]
    temp = result[0]
    result[0] /= math.gcd(result[0],result[1])
    result[1] /= math.gcd(temp,result[1])
    return result

def add_frac(frac1, frac2):         # frac1 + frac2
    result = [frac1[0] * frac2[1] + frac1[1] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def sub_frac(frac1, frac2):       # frac1 - frac2
    result = [frac1[0] * frac2[1] - frac1[1] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def mul_frac(frac1, frac2):      # frac1 * frac2
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def div_frac(frac1, frac2):        # frac1 / frac2
    temp = frac1[0]
    frac1[0] = frac1[1]
    frac1[1] = temp
    result = [frac1[0] * frac2[0], frac1[1] * frac2[1]]
    return shorter(result)

def is_positive(frac):              # bool, czy dodatni
    if frac[0] > 0:
        return True
    return False

def is_zero(frac):               # bool, typu [0, x]
    if frac[0] == 0:
        return True
    return False

def cmp_frac(frac1, frac2):        #porównuje ułamki: -1 | 0 | +1
    if frac1 == frac2:
        return 0
    temp = frac1[1]
    frac1[0] *= frac2[1]
    frac1[1] *= frac2[1]
    frac2[0] *= temp
    if frac1[0] < frac2[0]:
        return -1
    if frac1[0] == frac2[0]:
        return 0
    return 1

def frac2float(frac):               # konwersja do float
    return float(frac[0]/frac[1])