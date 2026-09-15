# Vos import ici
import csv
import doctest
from collections import defaultdict

# le path du fichier de données
FILENAME = "population.csv"


def read_file(filename):
    """retourne les données sous la forme d'une liste de dictionnaires

    Args:
        filename (str): le nom du fichier de données (n lignes)

    Returns:
        list: n-1 dictionnaires dont les clés sont les champs de la première ligne du fichier
    
    >>> data = read_file(FILENAME)
    >>> type(data)
    <class 'list'>
    >>> len(data)
    140827
    >>> type(data[0])
    <class 'dict'>
    >>> len(data[0])
    15
    >>> data[1000]["Nom Officiel Région"]
    'Grand Est'
    >>> data[5000]["Code Officiel Département"]
    '02'
    >>> data[10000]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25000]["Nom Officiel Commune / Arrondissement Municipal"]
    'Baneuil'
    >>> data[50000]["Population totale"]
    '1898.0'
    >>> data[75000]["Année de recensement"]
    '2018'
    >>> data[100000]["Nom Officiel EPCI"]
    'CC de la Région de Bar-sur-Aube'
    >>> data[125000]["Nom Officiel Département"]
    'Charente-Maritime'
    >>> data[1500]["Nom Officiel Région"]
    'Occitanie'
    >>> data[5500]["Code Officiel Département"]
    '25'
    >>> data[10500]["Code Officiel Arrondissement Départemental"]
    '001'
    >>> data[25500]["Nom Officiel Commune / Arrondissement Municipal"]
    'Fontenoy'
    >>> data[50500]["Population totale"]
    '52.0'
    >>> data[75500]["Année de recensement"]
    '2015'
    >>> data[100500]["Nom Officiel EPCI"]
    'CC de Yenne'
    >>> data[125500]["Nom Officiel Département"]
    'Aube'
    """
    with open(filename, 'r', encoding='utf8') as f:
        reader = csv.DictReader(f, delimiter=';')
        data = list(reader)
    return data


def build_list_departements(data):
    """retourne la liste ordonnée des départements contenus dans les données

    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        list: la liste ordonnée des tuples (code dpt, nom dpt)
    
    >>> data = read_file(FILENAME)
    >>> ld = build_list_departements(data)
    >>> type(ld)
    <class 'list'>
    >>> len(ld)
    99
    >>> '15' in ld
    False
    >>> 15 in ld
    False
    >>> 'Cantal' in ld
    False
    >>> ('15', 'Cantal') in ld
    True
    >>> ld[::20]
    [('01', 'Ain'), ('22', "Côtes-d'Armor"), ('40', 'Landes'), ('60', 'Oise'), ('80', 'Somme')]
    >>> ld[5::20]
    [('06', 'Alpes-Maritimes'), ('27', 'Eure'), ('45', 'Loiret'), ('65', 'Hautes-Pyrénées'), ('85', 'Vendée')]
    >>> ld[10::20]
    [('11', 'Aude'), ('30', 'Gard'), ('50', 'Manche'), ('70', 'Haute-Saône'), ('90', 'Territoire de Belfort')]
    >>> ld[15::20]
    [('16', 'Charente'), ('35', 'Ille-et-Vilaine'), ('55', 'Meuse'), ('75', 'Paris'), ('95', "Val-d'Oise")]
    >>> ld[20::20]
    [('22', "Côtes-d'Armor"), ('40', 'Landes'), ('60', 'Oise'), ('80', 'Somme')]
    >>> ld[5]
    ('06', 'Alpes-Maritimes')
    >>> ld[15]
    ('16', 'Charente')
    >>> ld[25]
    ('27', 'Eure')
    >>> ld[35]
    ('35', 'Ille-et-Vilaine')
    >>> ld[45]
    ('45', 'Loiret')
    >>> ld[55]
    ('55', 'Meuse')
    >>> ld[65]
    ('65', 'Hautes-Pyrénées')
    """
    dpts = set()
    
    for row in data:
        code = row['Code Officiel Département']
        nom = row['Nom Officiel Département']
        
        # Filtrer les lignes sans code département
        if code:
            dpts.add((code, nom))
    
    # Convertir en list et trier par code (premier élément du tuple)
    return sorted(list(dpts))


def build_list_communes(data):
    """retourne la liste des tuples (code, commune)

    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        list: la liste ordonnée des tuples (code commune, nom commune)
    
    >>> data = read_file(FILENAME)
    >>> lc = build_list_communes(data)
    >>> type(lc)
    <class 'list'>
    >>> len(lc)
    35836
    >>> type(lc[999])
    <class 'tuple'>
    >>> len(lc[999])
    2
    >>> lc[999]
    ('02598', 'Pernant')
    >>> type(lc[999][0])
    <class 'str'>
    >>> type(lc[999][1])
    <class 'str'>
    >>> lc[100:103]
    [('01105', 'Civrieux'), ('01106', 'Cize'), ('01107', 'Cleyzieu')]
    >>> lc[900:903]
    [('02499', 'Montbavin'), ('02500', 'Montbrehain'), ('02501', 'Montchâlons')]
    >>> lc[2000:2003]
    [('06089', 'Opio'), ('06090', 'Pégomas'), ('06091', 'Peille')]
    >>> lc[5000:5003]
    [('14712', 'Troarn'), ('14713', 'Montillières-sur-Orne'), ('14713', 'Trois-Monts')]
    >>> lc[10000:10003]
    [('27522', 'Saint-Christophe-sur-Condé'), ('27523', "Saint-Clair-d'Arcey"), ('27524', 'Sainte-Colombe-la-Commanderie')]
    >>> lc[15000:15003]
    [('39138', 'Chemin'), ('39139', 'Chêne-Bernard'), ('39140', 'Chêne-Sec')]
    >>> lc[20000:20003]
    [('54062', 'Benney'), ('54063', 'Bernécourt'), ('54064', 'Bertrambois')]
    >>> lc[25000:25003]
    [('63001', 'Aigueperse'), ('63002', 'Aix-la-Fayette'), ('63003', 'Ambert')]
    >>> lc[30000:30003]
    [('76002', 'Alvimare'), ('76004', 'Ambrumesnil'), ('76005', 'Amfreville-la-Mi-Voie')]
    >>> lc[-3:]
    [('97502', 'Saint-Pierre'), ('97701', 'Saint-Barthélemy'), ('97801', 'Saint-Martin')]
    """
    communes = set()
    
    for row in data:
        code = row['Code Officiel Commune / Arrondissement Municipal']
        nom = row['Nom Officiel Commune / Arrondissement Municipal']
        
        if code:
            communes.add((code, nom))
    
    return sorted(communes)


def get_pop_commune(data, code):
    """retourne la population totale d'une commune pour l'année de recensement la plus récente

    Args:
        data (list): la liste de dictionnaires retournée par read_file()
        code (str) : code de la commune considérée

    Returns:
        (int, str, str): (nom de la commune, population totale, année de recensement concernée)

    >>> data = read_file(FILENAME)
    >>> get_pop_commune(data, '39124')
    ('Chaumergy', 492, '2018')
    >>> get_pop_commune(data, '63001')
    ('Aigueperse', 2790, '2018')
    >>> get_pop_commune(data, '76005')
    ('Amfreville-la-Mi-Voie', 3354, '2018')
    >>> get_pop_commune(data, '74275')
    ('Talloires-Montmin', 2039, '2018')
    >>> get_pop_commune(data, '94022')
    ('Choisy-le-Roi', 46366, '2018')
    >>> get_pop_commune(data, '11151')
    ("Fontiès-d'Aude", 509, '2018')
    >>> get_pop_commune(data, '53210')
    ("Saint-Denis-d'Anjou", 1581, '2018')
    >>> get_pop_commune(data, '30266')
    ('Saint-Jean-de-Maruéjols-et-Avéjan', 897, '2018')
    >>> get_pop_commune(data, '07222')
    ('Saint-Cierge-sous-le-Cheylard', 211, '2018')
    >>> get_pop_commune(data, '00000')
    
    """
    result = None
    max_year = None
    
    for row in data:
        if row['Code Officiel Commune / Arrondissement Municipal'] == code:
            year = row['Année de recensement']
            
            if max_year is None or year > max_year:
                max_year = year
                name = row['Nom Officiel Commune / Arrondissement Municipal']
                pop = int(float(row['Population totale']))  # ← CHANGE CETTE LIGNE
                result = (name, pop, year)
    
    return result

def multi_dict(K, type):
    if K == 1:
        return defaultdict(type)
    else:
        return defaultdict(lambda: multi_dict(K-1, type))

def build_dict_departements(data):
    """Retourne un dictionnaire dont la clé est le département, et la valeur une liste [nombre de communes, population totale]
    
    Args:
        data (list): la liste de dictionnaires retournée par read_file()

    Returns:
        dict : un dictionnaire dont la clé est le code du dpt (str) et la valeur un tuple (int, int) nombre de communes, population totale
    
    >>> data = read_file(FILENAME)
    >>> dd = build_dict_departements(data)
    >>> type(dd)
    <class 'dict'>
    >>> len(dd)
    103
    >>> dd['18']
    (290, 310910)
    >>> dd['21']
    (713, 553151)
    >>> dd['27']
    (614, 627971)
    >>> dd['53']
    (264, 346208)
    """
    md = multi_dict(3, int)
    
    # Remplir la structure avec toutes les données
    for row in data:
        dpt = row['Code Officiel Département']
        commune = row['Code Officiel Commune / Arrondissement Municipal']
        annee = row['Année de recensement']
        pop = int(float(row['Population totale']))
        
        if dpt and commune:  # Filtrer les vides
            md[dpt][commune][annee] = pop
    
    # Construire le résultat final
    result = dict()
    
    for dpt in md:
        # Trouver l'année la plus récente pour ce département
        max_annee = None
        for commune in md[dpt]:
            for annee in md[dpt][commune]:
                if max_annee is None or annee > max_annee:
                    max_annee = annee
        
        # Compter les communes et la population pour cette année
        if max_annee:
            nb_communes = 0
            total_pop = 0
            for commune in md[dpt]:
                if max_annee in md[dpt][commune]:
                    nb_communes += 1
                    total_pop += md[dpt][commune][max_annee]
            
            result[dpt] = (nb_communes, total_pop)
    
    return result
    
    
def stat_by_dpt(dd, dpt):
    """Retourne un tuple (nombre de communes, population totale)

    Args :
        dd (dict) : le dictionnaire retourné par build_dict_departements()
        dpt (str) : le département concerné

    Returns :
        tuple : (nombre de communes, population totale)
    
    >>> data = read_file(FILENAME)
    >>> dd = build_dict_departements(data)
    >>> s = stat_by_dpt(dd, '87')
    >>> type(s)
    <class 'tuple'>
    >>> len(s)
    2
    >>> s
    (202, 383163)
    >>> stat_by_dpt(dd, '77')
    (514, 1433625)
    >>> stat_by_dpt(dd, '13')
    (134, 2058818)
    >>> stat_by_dpt(dd, '08')
    (452, 278875)
    >>> stat_by_dpt(dd, '21')
    (713, 553151)
    >>> stat_by_dpt(dd, '2A')
    (124, 160294)
    >>> stat_by_dpt(dd, '34')
    (344, 1179337)
    >>> stat_by_dpt(dd, '53')
    (264, 346208)
    >>> stat_by_dpt(dd, '64')
    (546, 698710)
    >>> stat_by_dpt(dd, '75')
    (20, 2192485)
    >>> stat_by_dpt(dd, '18')
    (290, 310910)
    >>> sbd = stat_by_dpt(dd, 'Corse')

    """
    if dpt in dd:
        return dd[dpt]
    else:
        return None

def main():
    # votre code de test ici
    # le code ci dessous est exécuté avec la commande :
    #   python population.py
    pass
    # Exemples d'appels
    # data = read_file(FILENAME)
    # l = build_list_departements(data)
    # c = build_list_communes(data)
    # p = get_pop_commune(data, '39124')
    # d = build_dict_departements(data)
    # s = stat_by_dpt(d, '77')

    
# Ne pas modifier le code ci-dessous
if __name__ == '__main__':
    dt = True
    # dt = False # Décommenter pour exécuter "main()"
    if dt:
        # la ligne suivante teste la fonction "read_file"
        # doctest.run_docstring_examples(read_file, globals(), verbose=True)
        #doctest.run_docstring_examples(build_list_departements, globals(), verbose=True)  
        #doctest.run_docstring_examples(build_list_communes, globals(), verbose=True)
        #doctest.run_docstring_examples(get_pop_commune, globals(), verbose=True)
        #doctest.run_docstring_examples(build_dict_departements, globals(), verbose=True)
        doctest.run_docstring_examples(stat_by_dpt, globals(), verbose=True)
    else:
        main()
