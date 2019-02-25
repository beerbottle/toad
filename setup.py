from setuptools import setup, find_packages, Extension

NAME = 'toad'

def get_version():
    ns = {}
    with open(f'{NAME}/version.py') as f:
        exec(f.read(), ns)
    return ns['__version__']

setup(
    name = NAME,
    version = get_version(),
    description = 'python utils for detect data',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/amphibian-dev/toad',
    author = 'ESC Team',
    author_email = 'secbone@gmail.com',
    packages = find_packages(exclude = ['tests']),
    python_requires = '>=3.5',
    setup_requires = [
        'setuptools',
    ],
    install_requires = [
        'numpy >= 1.15',
        'pandas',
        'scipy',
        'sklearn',
        'statsmodels',
        'seaborn',
    ],
    tests_require=[
        'pytest'
    ],
    license = 'MIT',
    classifiers = [
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points = {
        'console_scripts': [
            'toad = toad.cli:main',
        ],
    },
)
