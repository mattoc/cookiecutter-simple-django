cookiecutter-simple-django
==========================

A cookiecutter_ template for Django.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

Description
-----------

Lighter version of the Daniel Greenfeld's cookiecutter-django.

It uses the latest stable versions and it only defines a skeleton which can be extended as needed.

Usage
------

Let's pretend you want to create a Django project called "redditclone". Rather than using `startproject`
and then editing the results to include your name, email, and various configuration issues that always get forgotten until the worst possible moment, get cookiecutter_ to do all the work.

First, get cookiecutter. Trust me, it's awesome::

Set up your virtualenv::

    $ cd ~/Projects
    $ mkvirtualenv myproject -a myproject
    $ pip install cookiecutter

Now run it against this repo::

    $ git clone https://github.com/mattoc/cookiecutter-simple-django.git
    $ cookiecutter cookiecutter-simple-django

You'll be prompted for some questions, answer them, then it will create a Django project for you.


It prompts you for questions. Answer them::

    Cloning into 'cookiecutter-django'...
    remote: Counting objects: 443, done.
    remote: Compressing objects: 100% (242/242), done.
    remote: Total 443 (delta 196), reused 419 (delta 176)
    Receiving objects: 100% (443/443), 119.91 KiB | 0 bytes/s, done.
    Resolving deltas: 100% (196/196), done.
    project_name (default is "project_name")? myproject
    repo_name (default is "repo_name")? myapp
    author_name (default is "Your Name")? Your Name
    email (default is "Your email")? <your-email>
    description (default is "A short description of the project.")? My app
    year (default is "Current year")? 2014


Create the database ``myapp`` and then set up your project::

    $ cd myapp/
    $ pip install -r requirements/local.txt
    $ python ./manage.py syncdb
    $ python ./manage.py migrate
    $ python ./manage.py runserver

and load localhost:8000/admin

A git repo will be created for you by a post-setup hook.


Structure
---------

The structure used should look quite familiar:

**Requirements**

The ``requirements`` folder contains a requirements file for each environment.

If you need to add a dependency please choose the right file.

**Settings**

The ``settings`` folder contains a settings file for each environment and the ``local`` settings should be gitignored.

If you take a look at ``base.py``, you'll see that it includes the optional module ``local.py``
in the same folder. There you can override the local values and gitignore will
exclude it from your commits.

The ``testing.py`` module is loaded automatically after ``base.py`` and ``local.py`` every time you
run ``python ./manage.py test``.

**Apps**

The ``apps`` folder should contain all your local django apps, this is to keep
the structure of the project clean.

When it's time to ``python ./manage.py startapp <name>``, just move the generated
module to ``apps``. If you want to know why this works, just take a look at the line::

    sys.path.insert(0, root('apps'))

in ``settings/base.py``.


Done!
-----

Now, it's time to write the code!!!


Not Exactly What You Want?
---------------------------

This is what I want. *It might not be what you want.* Don't worry, you have options:

Fork This
~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this to create your own version.
Once you have your fork working, let me know and I'll add it to a '*Similar Cookiecutter Templates*' list here.
It's up to you whether or not to rename your fork.

If you do rename your fork, I encourage you to submit it to the following places:

* cookiecutter_ so it gets listed in the README as a template.
* The cookiecutter grid_ on Django Packages.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _grid: https://www.djangopackages.com/grids/g/cookiecutter/

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they make my own project development
experience better.
