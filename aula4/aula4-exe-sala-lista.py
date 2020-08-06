# aula4 - exercicios em sala

nomes2= ["ata","pinha"]
nomes = ["caja","abacate", "laranja", "maçã", "uva", "morango", "jaca"]
nomes.sort()
print( nomes )
print(nomes[1])
print(nomes[2:])

nomes.append( "mangaba")
for item in nomes :
    print( item, end='-')

print( nomes.count("abacate") )

print( nomes.index("uva"))

nomes.insert( 1 ,"umbu")
nomes.reverse()

print(nomes)
nomes.sort()
print(nomes)
nomes.extend( nomes2 )
print(nomes)
