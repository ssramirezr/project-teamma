def input_G():
    nCasos = int(input())
    for i in range(nCasos):
        m = int(input())
        G = {}
        nonterminals = 0
        while nonterminals < m:
            l = input()
            l = l.split()
            G[l[0]] = []
            for j in range(1, len(l)):
                G[l[0]].append(l[j])
            nonterminals += 1

        for nonterm in G:
            first_set = first(G, nonterm, [])
            print("First("+nonterm+") = " + "{"+str(first_set)+"}")

def first(G, nonterm, used):
    first_set = []

    if nonterm in used:   # If the nonterminal has already been used, return the first set of that nonterminal
        return first_set
    else:
        used.append(nonterm)     # If the nonterminal has not been used, add it to the list of used nonterminals

    for i in G[nonterm]:         # We iterate that has to the productions of that terminal
        if i[0].islower():       # If the first symbol is a lower case letter (terminal), we add it to the list of first
            first_set.append(i[0])
        else:                      # If the first symbol is an upper case letter (nonterminal), recursively we found the first set of that nonterminal
            first_set += first(G, i[0], used)

    return first_set

input_G()