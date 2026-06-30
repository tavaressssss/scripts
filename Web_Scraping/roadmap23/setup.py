from setuptools import setup

setup(
    name='extrator',
    version='1.0',
    py_modules=['scraper'], # O nome do ficheiro sem o .py
    entry_points={
        'console_scripts': [
            # nome-do-comando = ficheiro:funcao_principal
            'extrator=scraper:main',
        ],
    },
)