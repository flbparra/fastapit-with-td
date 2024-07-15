def troco(valor):
    moedas_cinquenta = valor // 50
    moedas_vinte_e_cinco = (valor % 50) // 25
    moedas_dez = (valor % 50 % 25) // 10
    moedas_cinco = (valor % 50 % 25 % 10) // 5
    moedas_um = (valor % 50 % 25 % 10 % 5) // 1

    print(
        f"{moedas_cinquenta} moedas de 50 centavos\n"
        f"{moedas_vinte_e_cinco} moedas de 25 centavos\n"
        f"{moedas_dez} moedas de 10 centavos\n"
        f"{moedas_cinco} moedas de 5 centavos\n"
        f"{moedas_um} moedas de 1 centavo"
    )


troco(567)
