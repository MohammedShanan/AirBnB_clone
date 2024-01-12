# AirBnB_clone

## Description

Project is a clone of the AirBnB application and website.This repository contains the command interpreter that allows us to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## How to install and run the project

### To install the project run

```
git clone https://github.com/MohammedShanan/AirBnB_clone.git
```

## To start working with command interpreter run

```
./console
```

## Or

```
python console.py
```

## Commands table

| Commands |          Usage example           |                                  Fuction |
| -------- | :------------------------------: | ---------------------------------------: |
| help     |              `help`              |          displays all commands available |
| create   |        `create BaseModel`        |                      create a new object |
| show     |         `show User 1a2b`         |        show an object from the json file |
| update   | `update User 123abc {named:ali}` |                update objects attributes |
| all      |           `all State`            |           display all objects in a class |
| count    |          `count Place`           | display the number of objects in a class |
| destroy  |      `destroy User 123abc`       |              destroy object with it's id |
| quit     |              `quit`              |                         exit the program |

## Another way to use commands is class.command(args)

Ex

```
User.create()
```

```
User.all()
```
