from setuptools import setup

setup(
    name='Sokoban-AI',
    version='1.0',
    python_requires='>=3.8',
    packages=[''],
    url='https://github.com/nguyendan1337/Sokoban-AI',
    py_modules=["actionfunction", "BFS", "constants", "helper", "main", "preprocess", "Q", "Qtest", "sokoban"],
    license='',
    author='Dan Nguyen, Brooke Ryan, Jillian Ness',
    author_email='brooke.ryan@uci.edu',
    description='Sokoban solver written in Python. Uses hybrid Q-learning with BFS shortest-path finding.',
    install_requires=['pathlib', 'numpy', 'parameterized']
)
