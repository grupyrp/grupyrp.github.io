Grupy-RP
========

Repositório do site do grupy-rp feito com pelican usando o tema 'Malt'

Para contribuir

* Clone o repositório

    ```bash
    git clone https://github.com/grupyrp/grupyrp.github.io
    git submodule update --init --recursive
    ```

* Crie e ative um virtualenv

    ```bash
    virtualenv grupyrp
    source grupyrp/bin/activate
    ```

* Inicie o servidor de desenvolvimento do pelican

    ```bash
    ./develop_server.sh start
    ```

* Coloque o output do pelican em produção em grupyrp.github.io

    ```bash
    make github
    ```
