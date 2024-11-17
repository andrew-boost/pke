from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(name='pke',
      version='2.0.0',
      description='Python Keyphrase Extraction module',
      author='pke contributors',
      author_email='florian.boudin@univ-nantes.fr',
      license='gnu',
      packages=find_packages(),
      url="https://github.com/boudinfl/pke",
      install_requires=requirements,
      package_data={'pke': ['models/*.pickle', 'models/*.gz']},
      include_package_data=True,
      python_requires='>=3.8'
      )
