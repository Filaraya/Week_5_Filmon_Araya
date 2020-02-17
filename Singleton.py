"""
Week_5;
Filmon Araya
"""

#does not use for my system so I am just using this as a test for the assignment.
class Singleton(object):
    """
    Makes sure class only has one instance. 
    """
    newInstance = None

    def __new__(cls):
        if cls.newInstance == None:
            cls.newInstance = "New Connection"
        return cls.newInstance


def main():
    s1 = Singleton()
    s2 = Singleton()
    print(s1 == s2)
    print (s1)

main()