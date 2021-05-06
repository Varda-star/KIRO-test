# Ici sera écrite toutes les fnctions

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
