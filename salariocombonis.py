#coding: utf-8

def ComissaoSalario():
    nome = input("entrer le nom de vendeur:")
    saLARIOFIX= float(input("INFORME O SALARIO:"))
    vendas= float(input("INFORME O total de vendas:"))
    commissao= 0.15*vendas
    pagamentoesperado=saLARIOFIX+commissao
    return nome, commissao, pagamentoesperado

if __name__=="__salariocombonis__":
saLARIOFIX, commissao, pagamentoesperado
strg= "{0} obteve RS {1: ,2f} de comissiao e vai receber {2: ,2f}" .format(nome, commissao, pagamentoesperado)
print(strg)