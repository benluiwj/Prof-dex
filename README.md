## Profédex
Profédex aims to help Computer Science students in NUS to get to know their Professors better. Through a gamified telegram bot which builds on the idea of the Pokédex, the Professors are now entries for the Profédex. 

First the Profédex will be empty, with all the Professors name as `?????`. As students go through their NUS journey, they will meet many different Professors. By entering `/add <prof's name>` as an instruction on the telegram bot, the user will be able to unlock the information of the Professors. Information provided are - the Professor's name, Research Area, office location and a Bio.

The `/list` and `/show` functions are available to view the entries of the Profédex that have been inputted by the user.


## Developement Setup
> The setup section and related scripts are largely inspired by those of [Acquity](https://github.com/acquity/api).

First, install Python 3.9. Use [`pyenv`](https://github.com/pyenv/pyenv) to make your life easier.

```bash
curl https://pyenv.run | bash
pyenv install 3.9.4 # >= 3.9
pyenv local 3.9.4
```

Install [Poetry](https://python-poetry.org), version 1.1.6.

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | env POETRY_VERSION=1.1.6 python -
```

Install dependencies by running this in the project root.

```bash
poetry install
```

Add environment variables from the default values.
```
cp .env.default .env
```

## Run app
```
./launch.sh
```

## Commands

`/start` : Starts the bot.

`/add` : Adds 1 prof to the Profédex. The name of the prof can be found [here](https://www.comp.nus.edu.sg/about/depts/cs/faculty/). Example : `/add Lee Wee Sun` would be valid but any other variation of the prof's name will be invalid.

`/show` : Lists all the profs that you have added into Profédex so far. If no profs have been added, an error message will appear.

`/list` : Lists all the profs in the Profédex. Profs that are yet to be seen will have a placeholder value that consists of `?`. Clicking on any entry will reveal details of the prof. If the prof has not been added, all detail fields will be placholders.


