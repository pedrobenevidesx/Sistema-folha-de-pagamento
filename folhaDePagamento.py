## funcao para calcular inss
## funcao para calcular ir
## funcao para vale transporte
## funcao para a folha de pagamento
## resultados


def calcularInss(salarioBruto):
    if salarioBruto <= 1621:
        return salarioBruto * 0.075
    
    elif salarioBruto <= 2902.84:
        return salarioBruto * 0.09
    
    elif salarioBruto <= 4354.27:
        return salarioBruto * 0.12
    
    elif salarioBruto <= 8475.55:
        return salarioBruto * 0.14
    
    else: 
        return 1186.57
    


def calcularIr(baseIr):
    if baseIr <= 2428:
        return 0
    
    elif baseIr <= 2826.65:
        return baseIr * 0.075 - 182.16
    
    elif baseIr <= 3751.05:
        return baseIr * 0.15 - 394.16
    
    elif baseIr <= 4664.68:
        return baseIr * 0.225 - 675.49
    
    else:
        return baseIr * 0.275 - 908.73
    
    

def valeTransporte(salarioBruto):
    return salarioBruto * 0.06



def folhaDePagamento(nome, salario):

    inss = calcularInss(salario)

    baseIr = salario - inss

    ir = calcularIr(baseIr)

    vt = valeTransporte(salario)

    salarioLiquido = salario - inss - ir - vt

    print(f"\nFuncionario: {nome}")
    print(f"Salario Bruto: {salario:.2f}")
    print(f"INSS: {inss:.2f}")
    print(f"IRPF: {ir:.2f}")
    print(f"Vale Transporte: {vt:.2f}")
    print(f"Salario liquido: {salarioLiquido:.2f}\n")



for i in range(5):
    nome = input("Funcionario: ")
    salario = float(input("Salario: "))

    folhaDePagamento(nome, salario)

