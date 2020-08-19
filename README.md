## Instalation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required extensions.

```bash
    pip3 install -r requirements.txt
```

## Launch project

To launch project:
* Clone this repository
    ```bash
    git clone https://github.com/pykulytsky/pragmaxBlog.git
    ```
* Install all requirements 
    ```bash
    pip3 install -r requirements.txt
    ```
* Go to master directory
    ```bash
        cd pragmaxBlog
    ```
* Edit pragmaxBlog/settings.py
* Migrate db changes
    ```bash
    python manage.py migrate
    ```
* Set flag DEBUG=True in settings file

* Run django debug server
    ```bash
    python manage.py runserver
    ```