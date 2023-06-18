""" 11. Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs custando R
$1,37 cada uma, mas caso ele compra a partir de uma dúzia pagará com desconto de 10%, portanto o valor da unidade
ficará por R$ 1,24. O programa deverá receber o número de maçãs desejadas pelo cliente, e retornar o valor total da
compra. """

quantidade = float(input("Digite a quantidade de maçã comprada: "))
valor = 1.37
total = quantidade * valor

if quantidade < 12:
    total = total
    print('O valor total da compra é R$: %.2f' %total)
else:
    total = total * 0.9
    print('O valor total da compra é R$: %.2f' %total)

