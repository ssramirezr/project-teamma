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

        # We calculate and show the Follow sets
        follow_sets = {}    # We create a dictionary to store the follow sets of the nonterminals
        for nonterm in G:    # For each nonterminal in the grammar
            follow_sets[nonterm] = follow(G, nonterm, first_sets, [])    # We calculate the follow set of the nonterminal and store it in the dictionary
            print("Follow(" + nonterm + ") = {" + ", ".join(follow_sets[nonterm]) + "}")


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


def follow(G, nonterm, first_sets, used):
    follow_set = set()   # we initialize the set to store the follow set of the nonterminal

    if nonterm in used:  # If the nonterminal is mark as used, we return the follow set of that nonterminal
        return follow_set
    else:
        used.append(nonterm)  # If the nonterminal is not mark as used, we add it to the list of used nonterminals

    if nonterm == 'S':  # S is the initial symbol of the grammar, and because of that, we add the $ symbol to its follow set
        follow_set.add('$')

    for nt in G:  # We iterate over the nonterminals of the grammar
        for production in G[nt]:  # We iterate over the productions of the nonterminal
            if nonterm in production:   # If the nonterminal that enters as a parameter or the nonterminal that we are calculating the follow set is in the production
                idx = production.index(nonterm)   # We get the index of the nonterminal in the production
                if idx + 1 < len(production):    # If the nonterminal have a symbol after it in the production
                    next_symbol = production[idx + 1]  # We get the next symbol after the nonterminal
                    if next_symbol.islower():     # If the next symbol is a terminal, we add it to the follow set
                        follow_set.add(next_symbol)
                    else:
                        follow_set.update(first_sets[next_symbol] - {'e'})  # If the next symbol is a nonterminal, we add the first set of that nonterminal to the follow set, except the epsilon 'e'
                        if 'e' in first_sets[next_symbol]:
                            follow_set.update(follow(G, nt, first_sets, used))  # If e is in the first set of the nonterminal, we compute the follow of that nonterminal and add it to the follow set
                else:
                    if nt != nonterm:
                        follow_set.update(follow(G, nt, first_sets, used))  # In case that there are not other letter after the nonterminal, and the current nt is different from the nonterminal that we are calculating the follow set, we compute the follow of that current nt and add it to the follow set

    return follow_set

input_G()