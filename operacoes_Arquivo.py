import os
arquivo_Nome = ""
ersten_Mal = True
operacoes = ["União", "Intersecção", "Diferença", "Cartesiano"]
def imprimir_Resultado(operacao:str, conjunto_1:str, conjunto_2:str, resultado:str) -> None:
    global ersten_Mal
    linhas = [operacao, ": conjunto 1 {",  conjunto_1, "}, conjunto 2 {", conjunto_2, "}. Resultado: {", resultado, "}"]
    arquivo_Novo = open("Resultado.txt", "a")
    if ersten_Mal:#Primeira vez
        arquivo_Novo.write("Nome do arquivo selecionado: " + arquivo_Nome + "\n")
        ersten_Mal = False
    operacao = operacao.replace('\n', ' ')
    conjunto_1 = conjunto_1.replace('\n', ' ')
    conjunto_2 = conjunto_2.replace('\n', ' ')
    resultado = resultado.replace('\n', ' ')
    linha_resultado = f"{operacao}: conjunto 1 {{{conjunto_1}}}, conjunto 2 {{{conjunto_2}}}. Resultado: {{{resultado}}}\n"

    arquivo_Novo.writelines(linha_resultado)

    arquivo_Novo.close()

def formatacao(conjunto:str) -> list:
    conjunto_Final = []
    if "\n" not in conjunto:
        conjunto += "\n"#Como o conjunto 2 é a última linha a ser lida ele não pega o elemento de nova linha o que causa um erro de index na hora de formatar
    item = ""
    for i, entidade in enumerate(conjunto):
        if entidade.strip() and entidade != ",":
            item += entidade
            if conjunto[i + 1] == "," or conjunto[i + 1] == "\n":
                conjunto_Final.append(item)
                item = ""

    return conjunto_Final

def uniao(conjunto_1:str, conjunto_2:str) -> None:
    conjunto_A = formatacao(conjunto_1)
    conjunto_B = formatacao(conjunto_2)

    conjunto_A = set(conjunto_A)
    conjunto_B = set(conjunto_B)
    resultado = conjunto_A.union(conjunto_B)
    resultado = ",".join(resultado)

    imprimir_Resultado(operacoes[0], conjunto_1, conjunto_2, resultado)

def interseccao(conjunto_1:str, conjunto_2:str) -> None:
    conjunto_A = formatacao(conjunto_1)
    conjunto_B = formatacao(conjunto_2)

    conjunto_A = set(conjunto_A)
    conjunto_B = set(conjunto_B)
    resultado = conjunto_A.intersection(conjunto_B)
    resultado = ",".join(resultado)
    imprimir_Resultado(operacoes[1], conjunto_1, conjunto_2, resultado)

def diferenca(conjunto_1:str, conjunto_2:str) -> None:
    conjunto_A = formatacao(conjunto_1)
    conjunto_B = formatacao(conjunto_2)

    conjunto_A = set(conjunto_A)
    conjunto_B = set(conjunto_B)
    resultado = conjunto_A - conjunto_B
    resultado = ",".join(resultado)
    imprimir_Resultado(operacoes[2], conjunto_1, conjunto_2, resultado)

def cartesiano(conjunto_1:str, conjunto_2:str) -> None:
    conjunto_A = formatacao(conjunto_1)
    conjunto_B = formatacao(conjunto_2)

    resultado = ""
    for i in range(len(conjunto_A)):
        if conjunto_A[i].strip() and conjunto_A[i] != ",":
            for j in range(len(conjunto_B)):
                if conjunto_B[j].strip() and conjunto_B[j] != ",":
                    resultado += "(" + conjunto_A[i] + "," + conjunto_B[j] + "),"
    resultado = resultado[:-1]
    imprimir_Resultado(operacoes[3], conjunto_1, conjunto_2, resultado)

def processar_Arquivo(nome:str) -> None:
    try:
        file = open(nome, 'r')
        quantidade_Operacoes = int(file.readline())
        operacoes_lidas = 0
        while True:
            modo = file.readline().strip()
            conjunto_1 = file.readline()
            conjunto_2 = file.readline()
            if modo == "":
                break
            operacoes_lidas += 1
            if modo == "U":
                uniao(conjunto_1,conjunto_2)
            elif modo == "I":
                interseccao(conjunto_1, conjunto_2)
            elif modo == "D":
                diferenca(conjunto_1, conjunto_2)
            elif modo == "C":
                cartesiano(conjunto_1,conjunto_2)
            else:
                print("Certifique-se que os indicadores de operação estejão em letra maiúsculas")
        file.close()

        if operacoes_lidas != quantidade_Operacoes:
            if os.path.exists("Resultado.txt"):
                os.remove("Resultado.txt")
        else:
            print("Os resultados estão num arquivo chamado 'Resultado.txt'")

    except FileNotFoundError:
        print(f'Arquivo {nome} não foi encontrado')


def main():
    global arquivo_Nome
    arquivo_Nome = input("Digite o nome do arquvio (com .txt): ")
    processar_Arquivo(arquivo_Nome)

if __name__ == '__main__':
    main()
