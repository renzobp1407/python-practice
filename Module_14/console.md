# Glossary

you can run python directly on the console

on windows:

Path = is a global variable that our O.S uses to specify where to find programs
E.G when you type python, that's a program

if the program is in a folder which is in the PATH, ir will work

E.G C:Python/python3.7

yoy can see what's in yopur path by typing this on MAC OS X or Linux: ```echo $Path```

the PAth is an example of an environment variable, these are just global variables avaible to al programs that run in the environment

yoy can see what's in envorinment variables by typing this on MAC OS X or Linux: ```export```

for more information: [env variables windows](https://www.computerhope.com/issues/ch000549.htm)


python3 or python in Windows

which python3.7 for mac OS


# Virualenv

work for an aislated dependencies projects

pip is for installing packages
command: ``` pip install request  ```
command: ``` pip3.7 install request  ```
command: ``` pip install ```

pip install virtualenv
virtual env vend --python=python3.7

para entrar al entorno virtual:

En macOS y Linux:
source nombre_del_entorno/bin/activate

en windows
.\html\Scripts\activate

inside the venv ww have to install all the dependencies and we can use a personalized python version

# navigating the terminal

pwd = folder actually on site (linux)
'dir' or 'cd' = folder actually on site  (windows)

chdir 

turn back on folder
cd ..
cd -

all files:
ls

run proyect:
python project.py
python3.7 project.py

all libraries:
pip freeze

pip list

on a requierements file
pip freeze > requirements.txt

show al dependencies
cat requirements.txt

# using pipenv

pipenv is a new standart for managing project dependencies on python

remove the venv
rm -rf venv

pip install pipenv

pipenv install

To activate this project's virtualenv, run pipenv shell


pipfile = libraries it needs
pipfile.lock = is for locking the versions of the used dependencies libraries

# pipenv and virtualenv

pipenv run python

pipenv run python menu.py

pipenv = says is for your code and project is not for your python installation

if you move the project, we have to recreate the virutalenv again













