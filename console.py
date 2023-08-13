#!/usr/bin/python3

"""For defining the AirBnB console"""
import re
from shlex import split
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

def parse(arg):
    curlyBraces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curlyBraces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
            lexer = split(arg[:curlyBraces.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(curlyBraces.group())
            return retl
    
class HBNBCommand(cmd.Cmd):
     """
     For defining the HBnB command interpreter
     Attr:
     prompt (The command prompt)
     """

     prompt = "(hbnb) "
     __classes = {
          "BaseModel",
          "User",
          "State",
          "City",
          "Place",
          "Amenity",
          "Review"
          }

     def emptyline(self):
          """Pass an empty line"""
          pass
     
     def default(self, arg):
          """
          cmd module default behaviour if input is invalid
          """
          argDict = {
               "all" : self.do_all,
               "show" : self.do_show,
               "destroy" : self.do_destroy,
               "count" : self.do_count,
               "update" : self.do_update
               }
          
          match = re.search(r"\.", arg)
          if match is not None:
               argOne = [arg[:match.span()[0]], arg[match.span()[1]:]]
               match = re.search(r"\((.*?)\)",argOne[1])
               if match is not None:
                    command = [argOne[1][:match.span()[0]],match.group()[1:-1]]
                    if command[0] in argDict.keys():
                         call = "{} {}".format(argOne[0], command[1])
                         return argDict[command[0]](call)
          print("*** Unknown syntax: {}".format(arg))
          return False
     
     def do_quit(self, arg):
          """Command to quit the program"""
          return True
     
     def do_EOF(self, arg):
          """Signal to exit the program"""
          print("")
          return True
     
     def do_create(self, arg):
          """
          create a new class instance and print its id
          """
          argOne = parse(arg)
          if len(argOne) == 0:
               print("** class name missing **")
          elif argOne[0] not in HBNBCommand.__classes:
               print("** class doesn't exist **")
          else:
               print(eval(argOne[0])().id)
               storage.save()

     def do_show(self, arg):
          """
          Display spring representation of a class instance of a given id
          """
          argOne = parse(arg)
          objDict = storage.all()
          if len(argOne) == 0:
               print("** class name missing**")
          elif argOne[0] not in HBNBCommand.__classes:
               print("** class doesn't exist **")
          elif len(argOne) == 1:
               print("** instance id missing **")
          elif "{}.{}".format(argOne[0], argOne[1]) not in objDict.keys():
               print("** no instance found **")
          else:
               print(objDict["{}.{}".format(argOne[0], argOne[1])])    


     def do_destroy(self, arg):
          """
          Delete the class instance of a given id
          """
          argOne = parse(arg)
          objDict = storage.all()
          if len(argOne) == 0:
               print("** class name missing**")
          elif argOne[0] not in HBNBCommand.__classes:
               print("** class doesn't exist **")
          elif len(argOne) == 1:
               print("** instance id missing **")
          elif "{}.{}".format(argOne[0], argOne[1]) not in objDict.keys():
               print("** no instance found **")
          else:
               del objDict["{}.{}".format(argOne[0], argOne[1])]
               storage.save()

     def do_all(self, arg):
          """
          Display the string representation of all given class instances.
          And if no  class is specified, displays all instantiated objects
          """
          argOne = parse(arg)
          if len(argOne) > 0 and argOne[0] not in HBNBCommand.__classes:
               print("** class doesn't exist **")
          else:
               objOne = []
               for o in storage.all().values():
                    if len(argOne) > 0 and argOne[0] == o.__class__.__name__:
                         objOne.append(o.__str__())
                    elif len(argOne) == 0:
                         objOne.append(o.__str__())
               print(objOne)

     def do_count(self, arg):
          """
          count the number of instances in a given class
          """
          argOne = parse(arg)
          count = 0
          for o in storage.all().values():
               if argOne[0] == o.__class__.__name__:
                    count += 1
          print(count)

     def do_update(self, arg):
          """
          update an instance of a given id by adding or updating a given key/value attribute
          """
          argOne = parse(arg)
          objDict = storage.all()

          if len(argOne) == 0:
               print("** class name missing**")
               return False
          if argOne[0] not in HBNBCommand.__classes:
               print("** class doesn't exist **")
               return False
          if len(argOne) == 1:
               print("** instance id missing **")
               return False
          if "{}.{}".format(argOne[0], argOne[1]) not in objDict.keys():
               print("** no instance found **")
               return False
          if len(argOne) == 2:
               print("** attribute name missing **")
               return False
          if len(argOne) == 3:
               try:
                    type(eval(argOne[2])) != dict
               except NameError:
                    print("** value missing **")
                    return False
          if len(argOne) == 4:
               o = objDict["{}.{}".format(argOne[0], argOne[1])]
               if argOne[2] in o.__class__.__dict__.keys():
                    vt = type(o.__class__.__dict__[argOne[2]])
                    o.__dict__[argOne[2]] = vt(argOne[3])
               else:
                    o.__dict__[argOne[2]] = argOne[3]
          elif type(eval(argOne[2])) == dict:
               o = objDict["{}.{}".format(argOne[0], argOne[1])]
               for k,v in eval(argOne[2]).items():
                    if (k in o.__class__.__dict__.keys() and 
                        type(o.__class__.__dict__[k]) in {str, int, float}):
                         vt = type(o.__class__.__dict__[k])
                         o.__dict__[k] = vt(v)
                    else:
                         o.__dict__[k] = v
          storage.save()


if __name__ == "__main__":
     HBNBCommand().cmdloop()
