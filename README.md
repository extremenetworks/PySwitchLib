# pySwitchLib


Install
::
sudo pip install pySwitchLib
sudo pip install pybind


In a python program do this:
::
import pySwitchLib
import pybind


## 0.1.15:
* Added persistent sessions for REST requests. Authentication Token renewed after 160 seconds between REST requests and in case of failed REST responses.
* Timeout kwarg added to asset and API's. Default asset timeout is 1800 seconds. API timeouts override asset timeout.
* Added get_os_type() and get_os_version() methods to asset object. 
* Request from BFO team
* RestInterfaceError expection raised when asset can connect to IP, but web server is not available. Request from BFO team.

## 0.1.16:
* Rename README.md to README.rst
