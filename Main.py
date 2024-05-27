def input_G():
    nCasos = int(input())    # Number of cases recived for processing
    for i in range(nCasos):   # We iterate over the number of cases
        m = int(input())      # For each case we read the number of nonterminals of the grammar
        G = {}                # We create a dictionary to store the nonterminals of the grammar and their productions
        nonterminals = 0
        while nonterminals < m:
            l = input().split()  # We read the line with tge nonterminal and its productions
            G[l[0]] = []        # We add the nonterminal to the dictionary as key and an empty list as value
            for j in range(1, len(l)):    # We iterate over the productions of the nonterminal and add them to the list of productions
                G[l[0]].append(l[j])
            nonterminals += 1

        # We calculate and show the First sets
        first_sets = {}     # We create a dictionary to store the first sets of the nonterminals
        for nonterm in G:   # For ech nonterminal in the grammar
            first_sets[nonterm] = first(G, nonterm, [])   # We calculate the first set of the nonterminal and store it in the dictionary
            print("First(" + nonterm + ") = {" + ", ".join(first_sets[nonterm]) + "}")


def first(G, nonterm, used):
    first_set = set()  # we initialize the set to store the first set of the nonterminal

    if nonterm in used:   # If the nonterminal has already been used, return the first set of that nonterminal
        return first_set
    else:
        used.append(nonterm)   # If the nonterminal has not been used, add it to the list of used nonterminals

    for i in G[nonterm]:      # We iterate in the list of productions of the nonterminal in i position
        if i[0].islower():    # If the first symbol of the production is a terminal, we add it to the first set
            first_set.add(i[0])
        else:
            first_set.update(first(G, i[0], used))   # If the first symbol of the production is a nonterminal, we recursively calculate the first set of that nonterminal and add it to the first set

    return first_set     # We return de set with the first set of the nonterminal

input_G()

