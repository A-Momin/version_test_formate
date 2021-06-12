from setuptools import setup, find_packages

setup(
    name='py-proj-config-test',
    version='0.0.1',
    packages=find_packages(exclude=('tests*', 'testing', 'data')),
    description="Implementation of fundamental data structures",
    author="SHah",
    author_email="shah_pakistan@gmail.com",
    license="MIT",
    # url="https://github.com/algorithms_and_data_structures",
    # download_url='https://github.com/...../..../',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[]
)
