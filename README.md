Projeto para fazer batimento biométrico das fotos recebidas semanalmente com as fotos do SAF.

Python 
Tem que ter C++ -> baixa o visual studio 2019 free e só instala no C++
Deve ser windows 64

pip install -r requirements.txt (dentro da pasta face_rec)

ctrl+B roda o programa

carregar as fotos conhecidas OK
Salvar os ecoding das fotos conhecidas pra não ter que processar toda hora
Adicionar fotos a esse ecoding salvo
comparar com as novas OK
pegar quantos rostos foram detectados OK
se tiver diferente de 1 OK
	cria uma pasta com o nome da AC dentro da pasta wrongs OK
	copia a imagem pra pasta criada OK
	cria um arquivo csv dentro da pasta OK
	salva o relatório quantidade de faces detectadas no csv OK
se der match OK
	Criar uma pasta com o nome da AC dentro da pasta matches OK
	copiar a imagem pra pasta criada OK
	Criar um arquivo csv dentro da pasta OK
	salvar os nomes dos matchs no arquivo csv OK
