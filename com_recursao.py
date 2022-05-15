def percorre(i, graph):
    if i >= len(tree):
       return 
    
    lft = (i * 2) + 1
    rgt = (i * 2) + 2
   
    percorre(lft, graph)
    print(graph[i], end=' ')
    percorre(rgt, graph)

# representação em heap da árvore binária
tree = ['*', '-', '+', 'x', '5', 'x', '7']
percorre(0, tree)
print() # imprime uma linha em branco