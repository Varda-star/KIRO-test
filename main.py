# Ici sera écrite toutes les fnctions

def get_itin(i, data):
    for k in data["itineraire"]:
        if k["id"] == i:
            return k


def get_train(i, L):
    for k in L:
        if k["id"] == i:
            return k


def contraintes1(trains, data):
    L = list_trains(data)
    T = True
    for j in trains:
        trainj = get_train(int(j), L)
        solj = trains[j]
        it = solj["itineraire"]
        itinj = itin(int(it), data)
        if (((it != "notAffected") or (qt != "notAffected")) and ((itinj["voiesAQuai"] != solj["voiesAQuai"]) or (itinj["voisEnligne"] != solj["voisEnLigne"]))):
            T = False
    return T


def indicatriceq(s):
    if q == 'notAffected':
        return 1
    return 0


# def listelement(s):
#     elements = []
#     for k in s["trains"]:
#         for l in k:
#             elements.append(l)
#     return elements


def indicatricej(J, s):
    for j in J:
        for k, l in enumerate(s):
            if {int(k), int(l)} == {j[0], j[2]}:
                if int(s[k]['itineraire']) == j[1] and int(s[l]['itineraire']) == j[3]:
                    return 1
    return 0


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

    return True
