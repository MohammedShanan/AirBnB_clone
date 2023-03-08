import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def preloop(self):
        """
        handles intro to command interpreter
        """
        print('.----------------------------.')
        print('|    Welcome to hbnb CLI!    |')
        print('|   for help, input \'help\'   |')
        print('|   for quit, input \'quit\'   |')
        print('.----------------------------.')

    def postloop(self):
        """
        handles exit to command interpreter
        """
        print('.----------------------------.')
        print('|  Well, that sure was fun!  |')
        print('.----------------------------.')

    def do_quit(self, line):
        """
        Quit command to exit the program
        """

        return True


    def do_EOF(self, line):
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
