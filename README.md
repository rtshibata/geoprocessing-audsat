# Desafio de Programação em Python - **Audsat**

![N|Solid](http://www.audsat.com.br/images/logo_audsat_20170502.png) 

### Sistemas de Informações Geográficas (SIG) & Sensoriamento Remoto
-----------------

### 1. Requisitos:
 - Ubuntu 16.04
 - [Miniconda](https://conda.io/miniconda.html) - Python 3.7 - Linux 64-bit (Bash installer)
 - Dependências em `audsat-renato.yml`
 
### 2. Preparando o ambiente:
Depois de ter instalado Miniconda/Anaconda crie o ambiente:
```sh
$ conda env create -f audsat-renato.yml
```
Então ative o novo ambiente:
```sh
$ source activate audsat-renato
```
Extraia tudo do `DESAFIO_PYTHON.zip` e crie a pasta *ndvi_imgs*:
```sh
$ mkdir ./DESAFIO_PYTHON/IMAGENS_PLANET/ndvi_imgs
```
**Checar se:**
- Arquivo *.shp* na pasta *mygeodata*
- Pasta *ndvi_imgs* criada dentro da pasta *IMAGENS_PLANET*
### 3. Executando o código

*	Alguns exemplos das imagens geradas pelo meu código estão na pasta *imgs_examples*

| Arquivo a ser rodado  | Exercício | Descrição |
| ---------------------- | ------ | ----- |
| driver_ndvi.py | 1 | Gera os NDVI na pasta *ndvi_imgs*, são identificados pelo nome do arquivo *tif* origem terminados com **_ndvi.tif** 
| driver_ndvi.py | 2 | Gera os recortes e a imagem recortada na pasta *ndvi_imgs*, são identificados por terem **__ CLIP __** e **__ CLIPPED __** nos nomes dos arquivos, respectivamente
| driver_ndvi.py  | 3 | Imprime na tela o valor float médio dos pixels das imagens recortadas geradas no exercício 2
| script_csv_ndvi.py | 4 | Cria arquivo csv **ndvi.csv** com os valores médios dos pixels e suas respectivas imagens recortadas





