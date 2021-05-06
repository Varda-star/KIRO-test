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


def in_group(idt, data):

    for k in data["trains"]:
        for i in k:
            if i["id"] == idt:
                return k


def get_train_aquai(q, data):
    for k in data["trains"]:
        if k[0]["voieAQuai"] == q:
            return k


def contraintes1(trains, data):
    L = list_trains(data)
    T = True
    for j in trains:
        trainj = get_train(int(j), L)
        solj = trains[j]
        it = solj['itineraire']
        itinj = get_itin(int(it), data)
        if (((it != "notAffected") or (qt != "notAffected")) and ((itinj["voieAQuai"] != solj["voieAQuai"]) or (itinj["voisEnligne"] != solj["voisEnLigne"]))):
            T = False
    return T


def contraintes2(trains, data):
    L = list_trains(data)
    T = True
    for j in trains:
        solj = trains[j]
        qj = solj["voieAQuai"]
        k = in_group(int(j), data)
        qg = k[0]["voieAQuai"]
        if qj != qg:
            T = False
    return T


def indicatriceq(i, s):
    if s[i]["voieAQuai"] == 'notAffected':
        return 1
    return 0


# def listelement(s):
#     elements = []
#     for k in s["trains"]:
#         for l in k:
#             elements.append(l)
#     return elements


def indicatricej(j, s):
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


def cout(s, J, cout_vide):
    somme = 0
    for i in s:
        somme += indicatriceq(i, s)*cout_vide
    for j in J:
        somme += indicatricej(j, s)*j[4]
    return somme


def solution(data, J):
    resultat = {}
    itineraire = data['itineraire']
    trains = list_trains(data)
    compatibilite = {compatibilite[train['id']] = ["notAffected"] for train in trains}
    for i in itineraire:
        for train in trains:
            if train['voiesAQuai'] == i['voiesAQuai'] and train['voiesEnLigne'] == i['voiesEnLigne'] and train['sensDepart'] == i['sensDepart']:
                compatibilite[train['id']].append(i)

    # for group in data['trains']:
    #     resultat[group]
    #     for k in group:
    #         posssibilite = set(compatibilite[k['id']])
    #         for j in J:
    #             if k['id'] in {j[0], j[2]}:
    #                 for element in posssibilite:
    #                     if element['id'] in {j[1], j[3]}:
    #                         posssibilite = posssibilite - {element}
