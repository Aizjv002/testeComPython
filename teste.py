def operacoes_aritmeticas(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b

    if b != 0:
        divisao = a / b
        if divisao == float("inf"):
            resultado_divisao = "infinito positivo"
        elif divisao == float("-inf"):
            resultado_divisao = "infinito negativo"
        else:
            resultado_divisao = divisao
    else:
        resultado_divisao = "indefinido"

    return [soma, subtracao, multiplicacao, resultado_divisao]

#a outra função de conceitos
def calcular_conceito(nota1, nota2, nota3):
    if nota1 < 0 or nota1 > 100 or nota2 < 0 or nota2 > 100 or nota3 < 0 or nota3 > 100:
        return "NULO"
    
    media = (nota1 + nota2 + nota3) / 3

    if media < 50:
        return "D"
    elif media < 70:
        return "C"
    elif media < 90:
        return "B"
    else:
        return "A"

def relatorio_de_erros():
  errors = [] #para armazenar os erros dos testes
  lista = operacoes_aritmeticas(2, 3)
  # replace assertions by conditions
  if not lista[0] == 5:
    errors.append("Erro: A soma não está correta")
  if not lista[1] == -1:
    errors.append("Erro: A subtração está errada")
  if not lista[2] == 6:
    errors.append("Erro: A multiplicação está errada")
  if not lista[3] == 2/3:
    errors.append("Erro: A divisão está errada - valores positivos")
  lista = operacoes_aritmeticas(2, 0)
  if not lista[3] == "infinito positivo":
    errors.append("Erro: A divisão está errada - deveria ser infinito positivo")
  lista = operacoes_aritmeticas(-2, 0)# se é infinito negativo
  if not lista[3] == "infinito negativo":
    errors.append("Erro: A divisão está errada - deveria ser infinito negativo")
  lista = operacoes_aritmeticas(0, 0)#se é indefinido
  if not lista[3] == "indefinido":
    errors.append("Erro: A divisão está errada - deveria ser indefinido")
  #para a função de conceitos das notas
  ##ver para cada uma se uma da posições é de nota negativa (3 casos)
  if not calcular_conceito(-1,60,60) == "NULO":
      errors.append("Erro: a função calcular_conceito está aceitando nota negativa.")
  ##ver quando a nota é maior q 100 (3 casos)
  if not calcular_conceito(101,60,60) == "NULO":
      errors.append("Erro: a função calcular_conceito está aceitando nota maior que 100.")
  if not calcular_conceito(60,101,60) == "NULO":
      errors.append("Erro: a função calcular_conceito está aceitando nota maior que 100.")
  if not calcular_conceito(60,60,101) == "NULO":
      errors.append("Erro: a função calcular_conceito está aceitando nota maior que 100.")
  ##testar nos limites dos conceitos (médias 0, 49.999, 50, 69.999, 70, 89.999, 90, 100)
  if not calcular_conceito(0,0,0) == "D":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito D")
  if not calcular_conceito(49.999,49.999,49.999) == "D":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito D")
  if not calcular_conceito(50,50,50) == "C":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito C",)
  if not calcular_conceito(69.999,69.999,69.999) == "C":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito B")
  if not calcular_conceito(70,70,70) == "B":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito B")
  if not calcular_conceito(89.999,89.999,89.999) == "B":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito B")
  if not calcular_conceito(90,90,90) == "A":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito A")
  if not calcular_conceito(100,100,100) == "A":
      errors.append("Erro: a função calcular_conceito deveria retornar conceito A")
 
  # assert no error message has been registered, else print messages
  assert not errors, "errors occured:\n{}".format("\n".join(errors))


relatorio_de_erros()
print("Success, test ran 100% without errors")