def calc_imc(peso, altura):
    return peso / (altura ** 2)
p = float(input("Qual seu peso?: "));
a = float(input("Qual sua altura?: "));
imc = calc_imc(p,a)

print(imc)