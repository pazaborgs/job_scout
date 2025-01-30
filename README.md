# Job Scout

O Job Scout é o Projeto Integrador II do curso de Ciência de Dados da Univesp. Trata-se de uma aplicação web desenvolvida para facilitar o acompanhamento de vagas de emprego e processos seletivos. O sistema permite que os usuários cadastrem e gerenciem suas candidaturas em um único ambiente, eliminando a necessidade de consultar múltiplos sites.

A plataforma foi desenvolvida utilizando Django e Python e conhecimentos em Banco de Dados.

    $ virtualenv project-env
    $ source project-env/bin/activate
    $ pip install -r https://raw.githubusercontent.com/juanifioren/django-project-template/master/requirements.txt

    # You may want to change the name `projectname`.
    $ django-admin startproject --template https://github.com/juanifioren/django-project-template/archive/master.zip projectname

    $ cd projectname/
    $ cp settings_custom.py.edit settings_custom.py
    $ python manage.py migrate
    $ python manage.py runserver