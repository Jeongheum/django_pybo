<h2> Bulletin board, called "pybo", using Python Django </h2> <br>

<h4> Option #1 </h4>  
After git cloning done, enter the command below in CLI to run codes in local host (127.0.0.1).     
<b> set DJANGO_SETTINGS_MODULE=config.settings.local </b>

Then, the following to create database files  
<b> python manage.py makemigrations </b>  
<b> python manage.py migrate </b>

Then, run server
<b> python manage.py runserver </b> 

<br>

<h4> Option #2 </h4>  
To run this code on your cloud server, use the following  
<b> python manage.py runserver --settings=config.settings.prod </b> # on a cloud server such as AWS  

<br>
<img src="./sample.png"> </img>
