# CTFd
CTFd Scripts to help save time

Script to download user CSV from CTFd Server for python 3.8.5 (Built on Windows 10)
You will need to change the variables:
    - url - specify in one of these formats:
        http://www.domain.com:8000/
        http://www.domain.com/
        https://www.domain.com/
    - uname - username with admin rights to CTFd
    - passwd - password for user with admin rights to CTFd
Then simply run the script under regular user rights.
__author__ = "James Rodewald"
__copyright__ = "Copyright 2020, Akblarb"
__credits__ = ["Wireshark for showing me headers and request info"]
__license__ = "GPL"
__version__ = "1.0.0.0"
__maintainer__ = "James Rodewald"
__email__ = "<snip>"
__status__ = "Beta PoC"
***Currently does not save CSV to disk.  Only displays on screen.
