from setuptools import setup, find_packages


setup(name='pke',
      version='2.0.0',
      description='Python Keyphrase Extraction module',
      author='pke contributors',
      author_email='florian.boudin@univ-nantes.fr',
      license='gnu',
      packages=find_packages(),
      url="https://github.com/boudinfl/pke",
      install_requires=[
          'nltk',
          'networkx',
          'numpy>=1.20.0',
          'scipy>=1.5.0',
          'scikit-learn',
          'unidecode',
          'future',
          'joblib',
          'spacy>=3.2.3'
      ],
      package_data={'pke': ['models/*.pickle', 'models/*.gz']},
      include_package_data=True,
      python_requires='>=3.8'
      )
