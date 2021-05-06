# Ici sera écrite toutes les fnctions

def get_itin(i, data):
    for k in data["itineraire"]:
        if k["id"] == i:
            return k


def list_trains(data):
    L = []
    for i in data['trains']:
        for j in i:
            L.append(j)
    return L


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


def contrainte3(solution, data, liste_contrainte):

    list_train = [get_train(int(id), list_trains(data)) for id in solution]
    #print (list_train)
    for i in range(len(list_train)):
        if (str(list_train[i].get("id")) in solution):

            for j in range(len(liste_contrainte)):
               # print(solution[str(list_train[i]['id'])].get("voieAQuai"))
                if (solution[str(list_train[i]['id'])].get("voieAQuai") in liste_contrainte[j].get("voiesAQuaiInterdites")):

                    if(list_train[i].get("voieEnLigne") in liste_contrainte[j].get("voiesEnLigne")):
                        return False

                    if (list_train[i].get("typesMateriels") in liste_contrainte[j].get("typesMateriels")):
                        return False

                    if (list_train[i].get("typeCirculation") in liste_contrainte[j].get("typesCirculation")):
                        return False

    return True
