[![Build Status](https://travis-ci.org/jmencisom/wikastro.svg?branch=master)](https://travis-ci.org/jmencisom/wikastro)
[![astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)](http://www.astropy.org/)

# WIKASTRO
This is a project that pretend to enrich the information of the free encyclopedia Wikipedia, using the Web scraping data extraction technique on reliable websites such as the astronomical Simbad database  (http://simbad.u-strasbg.fr/simbad)/), where, by a website, is possible type the corresponding numbering to the required item and this will show a template with the data obtained, where the user will approve the modification of the information on the Wikipedia website.

## Getting Started

### Prerequisites

* Python 2.7.14
* pip
* virtualenv (optional)

### Installing

1. Optional: Create a local virtualenv 
```
$ virtualenv wikastro-ve
```
  1.1. Go to the new directory
```
$ cd wikastro-ve
```
  1.2. Load the directory
```
$ source bin/activate
```
2. Clone the repository
```
$ git clone https://github.com/jmencisom/wikastro.git
```
3. Go to directory
```
$ cd wikastro
```
4. Install requirements
```
$ pip install -r requirements.txt
```

## Versioning

We use [Github](http://github.com/) for versioning. For the versions available, see the [https://github.com/jmencisom/wikastro/](https://github.com/jmencisom/wikastro/). 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Astropy
* Travis CI
