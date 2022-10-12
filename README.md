# django to build a bulletin board, called "pybo" <br>

To run codes in local host (127.0.0.1) , enter the command below in CLI,   
python manage.py runserver --settings=config.settings.local   # on your local host computer  

or  
python manage.py runserver --settings=config.settings.prod  # on a cloud server such as AWS  

you may need to make a database first  
python manage.py makemigrations  
python manage.py migrate  
