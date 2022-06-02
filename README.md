# Compara Biometria Facial

Projeto para fazer batimento biométrico das fotos recebidas semanalmente com as fotos do Sistema.

## Pre-requisitos
1. Python >= 3.4
2. C++ -> baixar o visual studio 2019 (C++)
3. Windows >= 7/x64

## Instruções

Na pasta face_rec:

pip install -r requirements.txt 

ctrl+B roda o programa

## Checklist

1. Carregar as fotos conhecidas - OK
2. Salvar os ecoding das fotos conhecidas pra não ter que processar toda hora
3. Adicionar fotos a esse ecoding salvo
comparar com as novas - OK
4. pegar quantos rostos foram detectados OK
5. Se tiver diferente de 1:
	-cria uma pasta com o nome da AC dentro da pasta wrongs OK
	-copia a imagem pra pasta criada OK
	-cria um arquivo csv dentro da pasta OK
	-salva o relatório quantidade de faces detectadas no csv OK
6. Se der match - OK
	-criar uma pasta com o nome da AC dentro da pasta matches OK
	-copiar a imagem pra pasta criada OK
	-criar um arquivo csv dentro da pasta OK
	-salvar os nomes dos matchs no arquivo csv OK
