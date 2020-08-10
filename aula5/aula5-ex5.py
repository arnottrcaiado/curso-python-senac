# aula5 - ex5 - Arnott Ramos Caiado
# Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo,
# que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaimposto ( imposto, custo ):
    valor_imposto = custo * imposto
    valor = custo + valor_imposto
    return( valor )


custo = float(input( "Entre valor do custo do produto:"))
imposto=float(input( "Entre com a taxa de imposto (decimal ):"))

valor = somaimposto( imposto, custo)

print("Custo:", custo, " perc imposto :", imposto, " valor apos imposto:", valor)
