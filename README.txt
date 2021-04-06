



🔥 Pytest:

    - https://docs.pytest.org/en/stable/usage.html
    - https://docs.pytest.org/en/stable/example/index.html
    - pytest-datafiles: https://github.com/omarkohl/pytest-datafiles/blob/master/README.rst

For running all tests write down:

    $ pytest [-q | -v]

For running some specific tests (Ex: sorting):

    $ python3 -m pytest ads/tests/sortings.py
    $ pytest -k sorting.py
    $ pytest ads/test/sortings.py
    $ pytest -k -s test_avl_tree   -->> Use -s flag to allow to execute print statement in your test functions.



🔥 Black:

    - https://black.readthedocs.io/en/stable/compatible_configs.html
    - 

For formatting the whole package
    $ python -m black {source_file_or_directory}

For formatting a module from it's diractory
    $ black {source_file_or_directory}