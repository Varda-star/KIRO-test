def contraite3(solution, data, liste_contrainte):

    list_train = [get_train[id, data] for id in solution]

    for i in range(len(List_train)):
        if (list_train[i][0].get("id") in solution):

            for j in range(len(list_contraite_quai)):
                if (slolution.get("voieAQuai") in list_contraite_quai[j].get("voiesAQuaiInterdites")):

                    if((List_train[i][0].get(list_train[i][0].get("id"))).get("voieAQuai") in list_contraite_quai[j].get("voiesEnLigne")):
                        return False

                    if (List_train[i][0].get("typesMateriels")[0] in list_contraite_quai[j].get("typesMateriels")):
                        return False

                    if (List_train[i][0].get("typeCirculation") in list_contraite_quai[j].get("typesCirculation")):
                        return False

    return Bool
