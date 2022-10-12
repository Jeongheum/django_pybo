# django to build a bulletin board, called "pybo" <br>

To run codes in local host (127.0.0.1) , enter the command below in CLI,   
<b> python manage.py runserver --settings=config.settings.local </b>   # on your local host computer  

or  
<b> python manage.py runserver --settings=config.settings.prod </b> # on a cloud server such as AWS  

you may need to make a database first  
<b> python manage.py makemigrations </b>  
<b> python manage.py migrate </b>
