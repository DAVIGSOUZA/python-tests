'''
CPF = 168.995.350-09

DIGITO 1
CPF[1] * 10
CPF[2] * 9
CPF[3] * 8
CPF[4] * 7
CPF[5] * 6
CPF[6] * 5
CPF[7] * 4
CPF[8] * 3
CPF[9] * 2

DIGITO 2
CPF[1] * 11
CPF[2] * 10
CPF[3] * 9
CPF[4] * 8
CPF[5] * 7
CPF[6] * 6
CPF[7] * 5
CPF[8] * 4
CPF[9] * 3
DIGITO1 * 2


DIGITO = 11 - (SOMA / 11)

IF SOMA > 9 ? DIGITO1 = 0 : DIGITO

'''


def validate_cpf():
    cpf = input('Validar CPF. Informe somente números:')
    cpf_validation = cpf[:-2]
    if len(cpf) != 11:
        print('cpf', cpf, 'não é válido')
    else:
        count = 10
        validator = 0

        for n in cpf_validation:
            validator = validator + (int(n) * count)
            count -= 1

        digit1 = 11 - (validator % 11)

        if digit1 > 9:
            digit1 = 0

        if cpf[-2] != str(digit1):
            print('cpf', cpf, 'não é válido')
        else:
            cpf_validation = cpf_validation + str(digit1)
            count = 11
            validator = 0
            for n in cpf_validation:
                validator = validator + (int(n) * count)
                count -= 1

            digit2 = 11 - (validator % 11)
            if digit2 > 9:
                digit2 = 0

            cpf_validation = cpf_validation + str(digit2)

            if cpf != cpf_validation:
                print('cpf', cpf, 'não é válido')
            else:
                print('cpf', cpf, 'é válido')


validate_cpf()
