#!/usr/bin/python3
"""
Command interpreter for AirBnB project
"""
import cmd
from models import cls_init, storage
import re
import json


class HBNBCommand(cmd.Cmd):
    """
    Command inerpreter class
    """
    prompt = '(hbnb) '
    ERR = [
        '** class name missing **',
        '** class doesn\'t exist **',
        '** instance id missing **',
        '** no instance found **',
        '** attribute name missing **',
        '** value missing **',
    ]

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def __check_error(self, line):
        """
        check for errors
        """
        if len(line) == 0:
            print(HBNBCommand.ERR[0])
            return 1
        elif line[0] not in cls_init.keys():
            print(HBNBCommand.ERR[1])
            return 1
        return 0

    def get_obj(self, line):
        """
        return the an object
        """
        line = line.split()
        if self.__check_error(line):
            return
        if len(line) < 2:
            print(HBNBCommand.ERR[2])
        else:
            storage_objs = storage.all()
            obj_name, obj_id = line[0], line[1]
            for k, v in storage_objs.items():
                cls_name, id = k.split('.')
                if obj_name == cls_name and obj_id == id:
                    return v
            print(HBNBCommand.ERR[3])
            return None

    def do_EOF(self):
        """function to handle EOF"""
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, line):
        """create: create [ARG] [PARAM 1] [PARAM 2] ...
        ARG = Class Name
        PARAM = <key name>=<value>
                value syntax: "<value>"
        SYNOPSIS: Creates a new instance of the Class from given input ARG
                and PARAMS. Key in PARAM = an instance attribute.
        EXAMPLE: create City name="Chicago"
                City.create(name="Chicago")
        """
        line = line.split()
        if self.__check_error(line):
            return
        class_obj = cls_init[line[0]]
        my_obj = class_obj()
        my_obj.save()
        print(my_obj.id)

    def do_show(self, line):
        """show: show [ARG] [ARG1]
        ARG = Class
        ARG1 = ID #
        SYNOPSIS: Prints object of given ID from given Class"""
        obj = self.get_obj(line)
        if obj:
            print(obj)

    def do_destroy(self, line):
        """destroy: destroy [ARG] [ARG1]
        ARG = Class
        ARG1 = ID #
        SYNOPSIS: destroys object of given ID from given Class
        EXAMPLE: destroy City 1234-abcd-5678-efgh
                City.destroy(1234-abcd-5678-efgh)
        """
        obj = self.get_obj(line)
        if obj:
            storage.delete(obj)

    def do_all(self, line):
        """all: all [ARG]
        ARG = Class
        SYNOPSIS: prints all objects of given class
        EXAMPLE: all City
                City.all()
        """
        obj_list = []
        line = line.split()
        if len(line) != 0 and self.__check_error(line):
            return
        for k, obj in storage.all().items():
            cls_name = obj.__class__.__name__
            if len(line) > 0:
                if line[0] == cls_name:
                    obj_list.append(obj.__repr__())
            else:
                obj_list.append(obj.__repr__())
        print(obj_list)

    def __create_dict(self, str):
        str = str.replace("'", '"')
        try:
            new_dict = json.loads(str)
        except json.JSONDecodeError:
            return None
        for k, v in new_dict.items():
            if v.replace(".", "").isnumeric():
                new_dict[k] = float(v)
            elif v.isdigit():
                new_dict[k] = int(v)
        return new_dict

    def do_update(self, line):
        """update: update [ARG] [ARG1] [ARG2] [ARG3]
        ARG = Class
        ARG1 = ID #
        ARG2 = attribute name
        ARG3 = value of new attribute
        SYNOPSIS: updates or adds a new attribute and value of given Class
        EXAMPLE: update City 1234-abcd-5678-efgh name Chicago
                 City.update(1234-abcd-5678-efgh, name, Chicago)
                 City.update(1234-abcd, {'name': 'Chicago', 'address': 'None'})
        """
        obj = self.get_obj(line)
        if obj is None:
            return
        line = line.split()
        if len(line) < 3:
            print(HBNBCommand.ERR[4])
        elif len(line) < 4:
            print(HBNBCommand.ERR[5])
        else:
            pattern = re.compile(r"^.+\s.+\s({.+})")
            match = re.search(pattern, " ".join(line))
            if match:
                update_dict = self.__create_dict(match.group(1))
            else:
                if line[3].isdigit():
                    update_dict = {line[2]: int(line[3])}
                elif line[3].replace(".", "").isnumeric():
                    update_dict = {line[2]: float(line[3])}
                else:
                    update_dict = {line[2]: line[3]}
            obj.update_bm(update_dict)

    def do_BaseModel(self, line):
        """class method with .function() syntax
        Usage: BaseModel.<command>(<id>)"""
        self.__parse_cls_methods('BaseModel', line)

    def do_User(self, line):
        """class method with .function() syntax
        Usage: User.<command>(<id>)"""
        self.__parse_cls_methods('User', line)

    def do_Place(self, line):
        """class method with .function() syntax
        Usage: Place.<command>(<id>)"""
        self.__parse_cls_methods('Place', line)

    def do_City(self, line):
        """class method with .function() syntax
        Usage: City.<command>(<id>)"""
        self.__parse_cls_methods('City', line)

    def do_Review(self, line):
        """class method with .function() syntax
        Usage: Review.<command>(<id>)"""
        self.__parse_cls_methods('Review', line)

    def do_State(self, line):
        """class method with .function() syntax
        Usage: State.<command>(<id>)"""
        self.__parse_cls_methods('State', line)

    def do_Amenity(self, line):
        """class method with .function() syntax
        Usage: Amenity.<command>(<id>)"""
        self.__parse_cls_methods('Amenity', line)

    def __count(self, line):
        """counts the number objects in File Storage"""
        line = line.split()
        storage_objs = storage.all()
        counter = 0
        for obj in storage_objs.values():
            cls_name = obj.__class__.__name__
            if line[0] == cls_name:
                counter += 1
        print(counter)

    def __parse_cls_methods(self, cls_name, method):
        """
        private: parses the input from .function() syntax, calls matched func
        """
        method_dict = {
            'create': self.do_create,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'all': self.do_all,
            'update': self.do_update,
            'count': self.__count
        }
        if '(' and ')' in method:
            method, cls_args = method.strip('.)').split('(')
            if method == 'update':
                pattern = re.compile(r'^(".+"), ({.+})')
                match = re.search(pattern, cls_args)
                if match:
                    cls_args = [match.group(1), match.group(2)]
                    cls_args[0] = cls_args[0].replace('"', "")
                    cls_args = " ".join(cls_args)
                else:
                    cls_args = cls_args.replace(',', "")
                    cls_args = cls_args.replace('"', "")
            args = "{} {}".format(cls_name, cls_args)
            for k in method_dict.keys():
                if k == method:
                    method_dict[k](args)
                    return


if __name__ == '__main__':
    """Loop entry point"""
    HBNBCommand().cmdloop()
