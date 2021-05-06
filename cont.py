def contrainte3(solution, data, liste_contrainte):

    list_train = [get_train(int(id), data) for id in solution]

    for i in range(len(List_train)):

        for j in range(len(list_contraite_quai)):
            if (slolution[list_train[i]['id']].get("voieAQuai") in list_contraite_quai[j].get("voiesAQuaiInterdites")):

                if((List_train[i].get(list_train[i][0].get("id"))).get("voieAQuai") in list_contraite_quai[j].get("voiesEnLigne")):
                    return False

                if (List_train[i].get("typesMateriels")[0] in list_contraite_quai[j].get("typesMateriels")):
                    return False

                if (List_train[i].get("typeCirculation") in list_contraite_quai[j].get("typesCirculation")):
                    return False

    return True
s
