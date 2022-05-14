def main():
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


if __name__ == '__main__':
    main()
