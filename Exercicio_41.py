print("FOLHA DE PAGAMENTO")
print("Funcionário: José da Silva")
valor_hora = float(input("Informe o valor da hora de trabalho em R$:"))
quant_hora = float(input("Informe a quantidade de horas trabalhadas no mês:"))
s = (valor_hora * quant_hora)
print(f"Você receberá a quantia de R$ {s + (s * 0.10)} considerando o seu bônus de 10%.")