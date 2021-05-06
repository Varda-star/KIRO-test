def contraite3 (List_train, list_contraite_quai):
    Bool=True
    for i in range (len(List_train)):
        
        for j in range(len (list_contraite_quai)):
                if (List_train[i][0].get("voieAQuai") in list_contraite_quai[j].get("voiesAQuaiInterdites")) :

                    if( List_train[i][0].get("voieEnLigne") in list_contraite_quai[j].get("voiesEnLigne")):
                            return False

                    
                    if (List_train[i][0].get("typesMateriels")[0] in list_contraite_quai[j].get("typesMateriels")):
                            return False
                        
                    
                    if (List_train[i][0].get("typeCirculation") in list_contraite_quai[j].get("typesCirculation")):
                            return False

    return Bool
