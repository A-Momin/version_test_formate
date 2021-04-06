from typing import Sequence, List

NUMBERS = {"ZERO": 0, "TEN": 10, "TWENTY": 20, "THIRTY": 30, "FORTY": 40, "FIFTY": 50}

COLORS = sorted(["RED", "GREEN", "BLACK", "BLUE", "WHITE", "PINK", "YELLOW",
                 "CYAN", "MAGENTA", "GRAY", "BISQUE", "AZURE", "AQUA", "BEIGE"])


def swap(array: List[Sequence], i: int, j: int) -> None:
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp


def is_sorted(array):
    ''' Return True if the given list is sorted. '''
    for i in range(len(array)-1, 0, -1):
        if array[i] < array[i-1]:
            return False
    return True



def load_data_from_file(file_path, container):
    with open(file_path, encoding="utf-8") as f:         # Open the file

        value = 0
        while True:
            line = f.readline()
            if not line:
                break                      # line is empty so exit
            for word in line.split():
                container.put(word, value)
                value += 1


def load_data_from_collection(collection, container):

    if type(collection) is dict:
        for key in collection.keys():
            container.put(key, collection[key])

    elif type(collection) is list:
        for item in collection:
            container.append(collection[item])


def display_st(ST):
    print(f"""\t{"keys(): "} \t{ST.keys()}""")
    print(f"""\t{"root.key: "} \t{ST.root.key}""")
    print(f"""\t{"size(): "} \t{ST.size()}""")
    print(f"""\t{"height(): "} \t{ST.height()}""")
    print(f"""\t{"is_empty(): "} \t{ST.is_empty()}""")
    print(f"""\t{"contains('FORTY'): "} \t{ST.contains('FORTY')}""")
    print(f"""\t{"get('THIRTY'): "} \t{ST.get('THIRTY')}""")
    print(f"""\t{"select(3): "} \t{ST.select(3)}""")
    # print(f"""\t{"rank('THIRTY'): "} \t{ST.rank(ST.select(3))}""")
    print("\trank({}): \t{}".format(ST.select(3), ST.rank(ST.select(3))))
    print(f"""\t{"floor('TEEN'): "} \t{ST.floor('TEEN')}""")
    print(f"""\t{"ceiling('NINTYY'): "} \t{ST.ceiling('NINTYY')}""")

    print('\tkey-value pairs (IN-ORDER): ')
    for key in ST.keys():
        print(f"\t \t{key} \t{ST[key]}")


# FIXTURE_DIR = os.path.abspath(os.path.join(os.pardir, 'data'))


# @pytest.mark.datafiles(
#     os.path.join(FIXTURE_DIR, 'img1.jpg'),
#     os.path.join(FIXTURE_DIR, 'img2.jpg'),
#     os.path.join(FIXTURE_DIR, 'img3.jpg'),
# )
# def test_find_borders(datafiles):
#     for img in datafiles.listdir():
#         print(img)
        #assert process(img) == some_expected_value


# def simple_test_AVLTreeST(data):
#     ST = AVLTreeST()
#     load_data_from_collection(data, ST)

#     print('*'*25, 'Before Mutation: ', '*'*25)
#     display_st(ST)

#     del ST["ZERO"]
#     del ST["FIFTY"]
#     ST.put("NINTY", 90)
#     ST['SIXTY'] = 60
#     del ST['TWENTY']

#     print('*'*25, 'After Mutation: ', '*'*25)
#     display_st(ST)


# @pytest.mark.skip(reason='Not complete yet !')
# def test_main():

#     if len(sys.argv) > 1:
#         simple_test_AVLTreeST(sys.argv[1])
#     else:
#         simple_test_AVLTreeST(NUMBERS)
