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
          'nltk==3.9.1',
          'networkx==3.4.2',
          'numpy==1.26.4',
          'scipy==1.14.1',
          'scikit-learn==1.5.1',
          'unidecode==1.3.8',
          'future==1.0.0',
          'joblib==1.4.2',
          'spacy==3.7.5'
      ],
      package_data={'pke': ['models/*.pickle', 'models/*.gz']},
      include_package_data=True,
      python_requires='>=3.8'
      )
