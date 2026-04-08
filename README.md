# narrativa_neuromat

## Introdução

Este projeto é resultado da bolsa Fundação de Amparo à Pesquisa do Estado de São Paulo (FAPESP) de Jornalismo Científico de André M. Rodeguero Stefanuto (Processo nº 2025/01835-6), vinculado ao CEPID-Neuromat (Processo nº 2013/07699-0).
Ele tem o objetivo de apresentar, em uma construção narrativa baseada em dados, o histórico de iniciativas do NeuroMat e o amplo diálogo e transversalidade presente na organização delas e do próprio Centro.

A publicação é organizada em 5 abas, contendo uma apresentação e outras quatro abas, apresentando diferentes aspectos da história do NeuroMat.

__Licença__: o projeto final está licenciado via Creative Commons CC-BY 4.0 (Attribution 4.0 International);

## Requisitos:
Ele foi desenvolvido utilizando Python + Django na interface do VSCode. Foram utilizadas as versões:
- Python: 3.14.0;
- Django 5.2.1; (Versões mais recentes tiveram problemas com os arquivos estáticos, provavelmente devido ao uso de barras / e barras invertidas \ no Windows)
- VSCode: 1.113;

Para instalar a versão de Django, use uma das possibilidades abaixo
```
pip install django==5.2.1
```
```
python -m pip install django==5.2.1
```
  
Para acessar a lista completa de requisitos, acesse "requirements.txt.".
Para instalar a lista de requisitos, use:
```
pip install -r requirements.txt
```
```
python -m pip install -r requirements.txt
```


## Recomendações para desenvolvimento

No VSCode, foram instaladas as extensões:
- Django (Baptiste Darthnay);
- Pylance (Microsoft)
- Python (Microsoft)
- Python Debugger (Microsoft)
- Python Environment (Microsoft)

## Descrição

A pasta "narrativa_neuromat" contém as subpastas "narrativa_neuromat" (de mesmo nome) e "site_narrativa", assim como os arquivos "db.sqlite3" e "manage.py". Entre os arquivos contido nas subpastas, estão:

### Arquivos de configuração:

* "./" se refere a um diretório anterior, não especificado

- ".site_narrativa/urls.py" --> define as URLs internas que serão acessadas pelo servidor;
- "./site_narrativa/views.py --> define como serão visualizadas, na página, as URL definidas no arquivo anterior;
-  "./site_narrativa/settings.py --> define as configurações gerais da página;

### Arquivos de estilo:

- "./site_narrativa/static/css/style.css" --> define as características estilísticas da página. __É neste arquivo que devem ser feitas alterações para mudanças estilísticas na página final.__
- "./site_narrativa/templates/" --> pasta contém os templates HTML de exibição, que seguirão as definições estilísticas definidas por "style.css". __É neste arquivo que deve mexer caso tenha interesse em customizar a configuração visual da página, não apenas o estilo dos elementos__;
- "./site_narrativa/static/images/" -- > a pasta contém as imagens que são exibidas no HTML final

## Execução

1. Para execução do servidor, é preciso baixar a pasta completa "narrativa_neuromat" e todos seus componentes.

2. No VSCode (ou em outro editor ou terminal), você deve ser capaz de acessar essa pasta:
- O caminho: File > Open Folder > (Selecionar a pasta baixada). 
- Você pode preferir utilizar outras vias para fazer isso, então utilizar o código "cd" no terminal permite acessar a pasta, como em "cd ./narrativa_neuromat".

3. Uma vez que os arquivos estão baixados localmente, você deve acessar a localização de "manage.py". Originalmente, ele está em "./narrativa_neuromat/manage.py", no diretório base do projeto.  É este arquivo que será capaz de reproduzir o servidor.

4. Criar o ambiente virtual
Antes de rodar o servidor, é recomendável criar um ambiente virtual para isolar os pacotes do projeto.
No terminal, execute:
```
bashpython -m venv venv
```
 5. Ativar o ambiente virtual
- Windows:
```
bashvenv\Scripts\activate
```
- Mac/Linux:
```
bashsource venv/bin/activate
```
Quando ativado, você verá (venv) no início da linha do terminal, indicando que o ambiente está ativo.

6. Instalar os pacotes necessários
Com o ambiente virtual ativo, instale as dependências do projeto:
bashpython -m pip install -r requirements.txt

7. Em seguida, deve executar um dos três códigos, dependendo da versão de Python que está utilizando:
```
python manage.py runserver (utilizado na construção do projeto);
```
```
py manage.py runserver (caso esteja rodando diretamente em ambiente windows)
```
``` 
python3 manage.py runserver
```

8. Com isso, você terá acesso local à interface do projeto como foi publicada na URL "http://127.0.0.1:8000/". Você acessará a página por meio da aba "homepage", conforme imagem abaixo, mas poderá navegar ao longo das demais abas utilizando a barra lateral ou os botões ao final de cada página.

9. Para explorar o conteúdo da página, seu visual e seu estilo, acesse os arquivos HTML, localizados na pasta "templates" e o arquivo "style.css".

<img width="2527" height="831" alt="image" src="https://github.com/user-attachments/assets/e5330c96-aa23-4314-8467-9e2e7f76a9bf" />

 

