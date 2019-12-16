#                Pass Locker

An application that allows users to store passwords for various accounts.


## Created by [wamakimaN](https://github.com/wamakimaN)

## Description

An application that allows us to store passwords for site accounts.
Pass Locker stores a user's password for their site accounts. This ensures that a user's password is stored safely for easy retrieval.

## User Specifications

* In order to create an account with a user's details,log in and input password
* Store user's login credentials
* store user's login credentials for a new accounts

## B.D.D

|  Behaviour 	|  Input 	|  Output 	|
|---	|---	|---	|
| Create account  	|  ca:enter create credentials mode<br>user name:Moses<br>password:12345	|  user is able to create account<br>Congratulations Moses you may now log in 	|
|   User login 	|  ln:enter ligin mode<br>user name:Moses<br>password:12345 	|  User is able to log in<br>Welcome Moses. What would you like to do? 	|
|  Add site credentials 	|  as:enter credentials writting mode<br>name:twitter<br>user name:wama<br>password:qwerty 	|  User is able to store site credentials<br>new created account:<br>Account:twitter<br>user name:Moses<br>password:qwerty 	|
|  Display site credentials 	|  cd:short code for displaying all credentials saved 	|  show site credentials saved<br>if nothing is saved:You do not seem to have anything saved yet 	|
|  Search site credentials by name 	|  site name:twitter 	|  Account:twitter<br>user name:Moses<br>password:qwerty 	|
|  Delete credentials 	|  dc:enter credentials delete mode<br>site name:twitter 	|  twitter credentials have been deleted 	|
|  Exit application 	|  ex:short code to exit app 	|  you have successfully exited Pass Locker 	|

## Installation

Clone this using the command below:

git clone  https://github.com/wamakimaN/password-store.git

Run the ./run.py script on the terminal to open.

## Technologies Used

* Python 3.6

## License

MIT (C) **[wamakimaN](https://github.com/wamakimaN)**