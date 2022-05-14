# pythonRecursion

A [recursão](https://pt.wikipedia.org/wiki/Recursividade_(ci%C3%AAncia_da_computa%C3%A7%C3%A3o)) é um recurso poderoso da computação. A recursão faz parte da abordagem
"dividir para conquistar", onde um problema grande é dividido em problemas 
menores, que por sua vez são resolvidos.

Considere o seguinte exemplo. Vamos supor que tenhamos uma 
[árvore binária](https://pt.wikipedia.org/wiki/%C3%81rvore_bin%C3%A1ria) que 
gostaríamos de percorrer:

<img src = "images/balanced_binary_tree.svg" alt="árvore binária balanceada e completa com 7 nodos"/>

Esta árvore codifica a equação `y = (x-5)*(x+7)` (**y** está implícito).

Como você percorreria esta árvore? Você logo irá perceber que percorrê-la usando laços de repetição é uma tarefa difícil. 
Podemos escrever

```python
# representação em heap da árvore binária
tree = ['*', '-', '+', 'x', '5', 'x', '7']
for i in range(len(tree)):
    print(tree[i])
```

Mas isso não fará com que a árvore seja percorrida corretamente (pelo menos os itens não serão impressos na ordem correta). 
Se você tentar, verá que é muito difícil desenvolver um código-fonte **simples** que realize esta tarefa.

Com recursão, contudo, o código-fonte é

```python
# representação em heap da árvore binária
tree = ['*', '-', '+', 'x', '5', 'x', '7']
def percorre(i, graph):
    if i >= len(tree):
       return 
    
    lft = (i * 2) + 1
    rgt = (i * 2) + 2
   
    percorre(lft, graph)
    print(graph[i], end=' ')
    percorre(rgt, graph)

percorre(0, tree)
```

A saída será exatamente o que queremos: `x - 5 * x + 7`

## Referências

Para compilar os grafos da pasta [graphs](graphs), siga o passo-a-passo abaixo.

1. Instalar graphviz na máquina (assumindo que você 
   [já tenha criado um ambiente virtual](https://github.com/CTISM-Prof-Henry/pythonEssentials/blob/main/chapters/venvs.md#criando-e-usando-pela-linha-de-comando)):
    ```bash
    conda install --file requirements.txt
   ```
2. Rodar o comando

   ```bash 
   dot -Tsvg <nome do arquivo .dot> > <nome da imagem .svg>
   ```

   Por exemplo:
   
   ```bash 
   dot -Tsvg graphs/balanced_binary_tree.dot > images/balanced_binary_tree.svg
   ```


