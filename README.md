## Instalation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required extensions.

"""bash
    pip3 install -r requirements.txt
"""

## Launch project

To launch project:
* Clone this repository
    """shell
        git clone https://github.com/pykulytsky/pragmaxBlog.git
    """
* Install all requirements 
    """bash
        pip3 install -r requirements.txt
    """
* Go to master directory
    """shell
        cd pragmaxBlog
    """
* Edit pragmaxBlog/settings.py
* Migrate db changes
    """shell
        python manage.py migrate
    """
* Set flag DEBUG=True in settings file

* Run django debug server
    """shell
        python manage.py runserver
    """