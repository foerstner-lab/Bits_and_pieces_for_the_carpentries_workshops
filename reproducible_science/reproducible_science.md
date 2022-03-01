- Data + Code => Reproducitbility
  - BUT - dependecies - not only your code - also packages etc.

- Options
  - Python package managers: pip, poetry
  - General package managers: conda, nix
  - Containers: Docker, Singularty
  - Virtual machines

- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424 
- https://bioconda.github.io/

# Conda

- install Anaconda or miniconda

```
conda create --name my_awesome_project --channel bioconda
```

show all environments

```
conda info --envs
```

List all install packages

```
conda list
```

```
conda activate my_awesome_project
```

Let's install two important Python packages with conda

```
conda install pandas seaborn
```

Conda can also be used to install non-python programs e.g. git

```
conda install git
```

or curl

```
conda install curl
```

```
wget --version | head -n 1
GNU Wget 1.20.1 built on linux-gnu.
```

```
which curl
/home/kuf/.conda/envs/my_awesome_project/bin/curl
```

Windows 
```
gcm curl
```

```
conda remove curl
```

Install specific version

```
conda install curl=7.69.1
```

```
conda env export > environment.yml
```

https://github.com/mwaskom/seaborn-data/blob/master/fmri.csv 
https://github.com/mwaskom/Waskom_CerebCortex_2017
https://academic.oup.com/cercor/article/27/2/1270/3056315?keytype=ref&ijkey=5hjFprzQ7miiYZ4


```
import requests

url = 'http://google.com/favicon.ico'
r = requests.get(url, allow_redirects=True)
open('google.ico', 'wb').write(r.content)
```

```
channels:
  - defaults
  - bioconda
  - conda-forge
dependencies:
  - python=3.10
  - pandas=1.4.1
  - seaborn=0.11.2
```
