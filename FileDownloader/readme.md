# how and why to use pipenv
To save python requirements and dependencies and create virtual environemnt (venv)

1. Use `pip freeze` to see your system level python config
1. We use `pip freeze > requirements.txt` to save requirements(dependencies) in a text file
1. This `requirements.txt` file can be used to install all the requirements using
`pip install -r requirements.txt`

## However this adds so many unnecessary packages 
the packages not required by our program and will be packed in exe when converting using `pyinstaller main.py`


## `pipenv` is used to create temperary virtual environment

in this env. we install only required dependencies

1. Install pipenv using `pip install pipenv`
2. Go to project folder and create virtual env using `pipenv install`, this will create a `Pipfile` and `Pipfile.lock`
3. Try to execute your program using `pipenv run <command>` or `pipenv run python main.py` and is it says missing dependencies or import failed
4. Install those modules in venv using `pipenv install <module>`
5. After install retry to execute using `pipenv run python main.py`
6. Repete steps untill program is executed successfully and test all functions.
7. Lock dependencies using `pipenv lock`
8. Export requirements using `pipenv freeze > requirements.txt`

> Now you can share your `program files` together with three more files in the same directory
> 1. `Pipfile`
> 2. `Pipfile.lock`
> 3. `requirements.txt`


# Now that you have understand process do the following in venv.
1. Install pyinstaller in venv using `pipenv install pyinstaller`
2. Compile program in to executale using `pipenv run pyinstaller main.py`
3. You may compare filesize of final executable



