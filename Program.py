weights=[6,5,7,2,3,4,5,6,7]
def validate_nip(nip):
    if len(nip) !=10:
        return False
    if nip.isdigit():
        return False
    suma = 0
    for i in range(9):
        suma += int(nip[i])*weights[i]
    if suma%11 == 10 and suma %11 != nip[9]:
        return False
    return True
nip = '123456789'
t=validate_nip(nip)
print(t)