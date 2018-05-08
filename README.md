[![Build Status](https://travis-ci.org/jmencisom/wikastro.svg?branch=master)](https://travis-ci.org/jmencisom/wikastro)
[![astropy](http://img.shields.io/badge/powered%20by-AstroPy-orange.svg?style=flat)](http://www.astropy.org/)

# WIKASTRO
Wikastro enriches the information on astronomical objects available at the free encyclopedia Wikipedia. It uses web scraping to extract data from reliable websites such as [UDS/CNRS Simbad](http://simbad.u-strasbg.fr/simbad/), [SAO/NASA ADS](http://adsabs.harvard.edu/), among others. Users add the resulting page by hand to the encyclopedia. The result uses the respective format, multimedia and supporting references.

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
