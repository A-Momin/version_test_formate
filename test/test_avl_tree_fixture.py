import os
import pytest
import unittest

from utils import *
from avl_tree import *


DATA_FILE_PATH = os.path.abspath('data/shellsST.txt')


# T1, T2, kvp = None, None, None

# def setup():
#     print("***************** setup ******************")
#     global T1, T2, kvp
#     kvp = NUMBERS
#     T1 = AVLTreeST()
#     T2 = AVLTreeST()

#     load_data_from_file(DATA_FILE_PATH, T1)
#     load_data_from_collection(kvp, T2)


# def test_size():
#     assert T1.size() == 7
#     assert T2.size() == len(kvp)


# def teardown():
#     print("***************** teardown ******************")

# Usage of Fixtures to have the functionality of the code aboe


# # @pytest.fixture(scope='module') to run this once for this module
# @pytest.fixture
# def args():
#     print("***************** equivalent to setup ******************")
#     kvp = NUMBERS
#     T1 = AVLTreeST()
#     T2 = AVLTreeST()

#     load_data_from_file(DATA_FILE_PATH, T1)
#     load_data_from_collection(kvp, T2)

#     return (T1, T2, kvp)


@pytest.fixture(scope='module')
def args():
    print("***************** equivalent to setup ******************")
    kvp = NUMBERS
    T1 = AVLTreeST()
    T2 = AVLTreeST()

    load_data_from_file(DATA_FILE_PATH, T1)
    load_data_from_collection(kvp, T2)

    yield (T1, T2, kvp)

    print("***************** equivalent to teardown ******************")
    print("you can implement code for teardown here (after yield statement above).")


def test_size(args):
    assert args[0].size() == 7
    assert args[1].size() == len(args[2])

def test_is_empty(args):
    assert args[0].is_empty() == False
    assert args[1].is_empty() == False
