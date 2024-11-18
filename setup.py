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
          'networkx==3.1',
          'numpy==1.26.4',
          'scipy==1.11.1',
          'scikit-learn==1.3.0',
          'unidecode==1.3.8',
          'future==0.18.3',
          'joblib==1.2.0',
          'spacy==3.7.2'
      ],
      package_data={'pke': ['models/*.pickle', 'models/*.gz']},
      include_package_data=True,
      python_requires='>=3.8'
      )
