# pesa-serv
Simple web framework that implements dynamic roouting and SSL with the help of Gunicorn WSGI Web Server

# Getting Started

* Git clone the repo:
    ```git@github.com:gkarumbi/pesa-serv.git```

* cd to the clone repo folder

    ``cd <Directory Name> ``

* Create a virtual environment 
  
    ```virtualenv <virtual-env-name>```

* Activate the virtual environment 

    ```. <virtual-env-name>/bin/activate```

* Install all the dependencies 
  
    ```pip install -r requirements.txt```

* Generate SSL certificates and store them in a folder names 'certs'
    ``` openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365 ```

* Run the Server
    ```gunicorn --certfile=certs/cert.pem --keyfile=certs/key.pem --bind 127.0.0.1:8000 app:app```

* View The static path @:
    [home](http://localhost:8000/home)
    [about](http://localhost:8000/about)

* Create a Dynamic path @:
    http://localhost:8000/hello/yourname

# Current Limitations

The HTML has to be hard coded

# Future Extensions

-To implment a django-like templating system
-To implement an ORM similar to Django ORM or SQL Alchemy