# setup.py

import setuptools
import os

# --- Obter a descrição longa do arquivo README ---
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# --- Obter a versão (uma forma comum é de um arquivo __version__.py) ---
# Por agora, vamos definir diretamente, mas considere mover para pyborg/__init__.py
# ou pyborg/version.py e ler daqui.
# Exemplo se estivesse em pyborg/__init__.py:
# version = {}
# with open(os.path.join("pyborg", "__init__.py")) as fp:
#     exec(fp.read(), version)
# current_version = version['__version__']
current_version = "0.1.0" # Versão inicial de desenvolvimento

# --- Listar as dependências ---
# É bom especificar versões mínimas se você souber de incompatibilidades.
# Você pode ler de um requirements.txt ou listá-las aqui.
# Se você tem um requirements.txt para desenvolvimento, pode mantê-lo separado
# ou sincronizado com esta lista.
install_requires = [
    "brian2>=2.5",      # Núcleo da simulação
    "numpy>=1.20",      # Manipulação de arrays numéricos
    "matplotlib>=3.4",  # Para plots e visualizações
    "scipy>=1.7",       # Funções científicas (muitas vezes dependência do Brian2)
    "networkx>=2.6",    # Para análise e visualização de grafos (em analysis/visualization)
    # Adicione outras dependências de TEMPO DE EXECUÇÃO aqui
    # Dependências de desenvolvimento (testes, linting, build de docs)
    # são geralmente gerenciadas separadamente (e.g., em requirements-dev.txt ou extras_require)
]

# --- Dependências opcionais (para desenvolvimento, testes, documentação) ---
extras_require = {
    "dev": [
        "pytest>=6.0",
        "flake8>=3.9",
        "black>=21.0b0",
        "ipykernel", # Para rodar notebooks de exemplo
        "jupyterlab",
    ],
    "docs": [
        "sphinx>=4.0",
        "sphinx-rtd-theme>=1.0",
        "nbsphinx>=0.8",
        "ipykernel", # nbsphinx precisa para executar notebooks
    ],
    "test": [
        "pytest>=6.0",
    ]
}
extras_require["all"] = sum(extras_require.values(), [])


setuptools.setup(
    name="pyborg",  # Nome do pacote como aparecerá no PyPI
    version=current_version,
    author="Seu Nome / Nome da Equipe", # Substitua
    author_email="seu.email@example.com", # Substitua
    description="A Python Brain Organoid Simulator using Brian2.",
    long_description=long_description,
    long_description_content_type="text/markdown", # Tipo de conteúdo do README
    url="https://github.com/seu_usuario/pyborg",  # URL do seu repositório GitHub (Substitua)
    project_urls={ # URLs adicionais úteis
        "Bug Tracker": "https://github.com/seu_usuario/pyborg/issues",
        "Documentation": "https://pyborg.readthedocs.io/", # Se você hospedar no ReadTheDocs
        "Source Code": "https://github.com/seu_usuario/pyborg",
    },
    # packages=setuptools.find_packages(exclude=("tests*", "examples*")),
    # Se a raiz do seu repositório é o pacote 'pyborg' (contém __init__.py e os submódulos):
    packages=setuptools.find_packages(
        where='.', # Busca pacotes a partir do diretório atual
        exclude=['tests*', 'examples*'] # Exclui os diretórios de testes e exemplos
    ),
    # Se o seu código estivesse em um diretório 'src/pyborg':
    # package_dir={'': 'src'},
    # packages=setuptools.find_packages(where='src', exclude=("tests*", "examples*")),

    classifiers=[ # Classificadores ajudam usuários a encontrar seu projeto
        "Development Status :: 3 - Alpha",  # Estágio de desenvolvimento
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",  # Substitua pela sua licença
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Natural Language :: English", # Ou Português, se a interface principal for
    ],
    python_requires='>=3.7',  # Versão mínima do Python suportada
    install_requires=install_requires,
    extras_require=extras_require,
    # Se você tiver dados de pacote não-código que precisam ser incluídos:
    # include_package_data=True,
    # package_data={
    #     'pyborg': ['data_files/*.json'], # Exemplo
    # },
    # Se você tiver scripts executáveis de linha de comando:
    # entry_points={
    #     'console_scripts': [
    #         'pyborg_cli=pyborg.cli:main_function', # Exemplo
    #     ],
    # },
    keywords="brain organoid simulation brian2 neuroscience computational-neuroscience",
)