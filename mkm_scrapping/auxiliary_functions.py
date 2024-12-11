def empty_df(save_path, titles = []):
    """
    Create a new, empty dataframe with columns whose name are the content of titles.
    Save it as a csv at a given path
    """
    import pandas as pd
    data = pd.DataFrame({})
    for title in titles:
        data[title] = []
    data.to_csv(save_path, index=False)

def swap_columns(data, new_columns_names: list):
    return data[new_columns_names]



def remove_zero_start(code):
    #enlève tous les "0" dans une chaine de caractère qui apparaissent avant un autre chiffre.
    #Par exemple: "ABC001234" renvoie "ABC1234"
    i = True
    new_str = ""
    chiffres = [str(j) for j in range(1, 10)]
    for a in code:
        if a in chiffres:
            i = False
        if not(a == "0" and i):
            new_str += a
    return new_str

def add_column(dataframe, column_name:str, value = "None"):
    dataframe[column_name] = value

def intersect_list(l1,l2):
    return [i for i in l1 if i in l2]

def complement_list(l1: list,l2: list):
    """
    Renvoie les éléments de l1 qui ne sont pas dans l2
    """
    return [i for i in l1 if i not in l2]

def split_list(l: list, step = 10):
    """
    Take a list and a step (optional) as an argument. Return a list containing lists with step elements of l
    """
    L = []
    l1 = []
    for i in l:
        l1.append(i)
        if len(l1) == step:
            L.append(l1)
            l1 = []
    if l1 != []:
        L.append(l1)
    return L
