import face_recognition
import os
import cv2
import shutil
import pickle
import numpy as np

'''
KNOWN_FACES_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\known_faces'
UNKNOWN_FACES_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\unknown_faces' 
WRONGS_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\wrongs' 
WRONGS_FILE = 'Relatorio_erros_foto.csv' 
MATCHES_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\matches' 
MATCHES_FILE = 'Relatorio_possiveis_fraudes.csv'
'''
KNOWN_FACES_DIR = 'G:\\fraudes\\2019\\Biometrias_SAF\\Junto'
UNKNOWN_FACES_DIR = 'G:\\teste_bio\\teste'
WRONGS_DIR = 'G:\\relatorios\\biometria\\wrongs'
WRONGS_FILE = 'Relatorio_erros_foto.csv'
MATCHES_DIR = 'G:\\relatorios\\biometria\\matches'
MATCHES_FILE = 'Relatorio_possiveis_fraudes.csv'
TOLERANCE = 0.4 #quanto menor mais refinado

FRAME_THICKNESS = 3 #pixels
FONT_THICKNESS = 2
MODEL = "hog" #or cnn, cnn pode deixar mais lento

'''
KNOWN_FACES_ENCODED_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\known_faces_encoded'
KNOWN_FACES_ENCODED_FILE = 'dataset_faces_encoded.dat'
NUMBER_SAF_ENCODED_FILE = 'dataset_number_saf_encoded.dat'
'''
KNOWN_FACES_ENCODED_DIR = 'G:\\fraudes\\2019\\Biometrias_SAF\\Biometrias_Python_Encoded'
KNOWN_FACES_ENCODED_FILE = 'dataset_faces_encoded.dat'
NUMBER_SAF_ENCODED_FILE = 'dataset_number_saf_encoded.dat'

print("Carregando imagens do SAF para comparação")
'''
known_faces = []
number_saf = []

onlydir = next(os.walk(f"{KNOWN_FACES_DIR}"))[1]
count_ano_total = len(onlydir)
count_ano = 1
for ano in os.listdir(KNOWN_FACES_DIR):
	onlyfiles = next(os.walk(f"{KNOWN_FACES_DIR}/{ano}"))[2]
	count_oco_total = len(onlyfiles)
	count_oco = 1
	for filename_known in os.listdir(f"{KNOWN_FACES_DIR}/{ano}"):
		print(f"Processando as imagens no SAF de {ano} ({count_ano}/{count_ano_total}) ocorrencia ({count_oco}/{count_oco_total})")
		image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{ano}/{filename_known}")
		encoding = face_recognition.face_encodings(image) [0] #só pega a primeira face da imagem, para imagens que tem mais de uma face
		known_faces.append(encoding)
		number_saf.append(filename_known)
		count_oco += 1
	count_ano += 1
'''

# Load face encodings
with open(f"{KNOWN_FACES_ENCODED_DIR}/{KNOWN_FACES_ENCODED_FILE}", 'rb') as f:
	known_faces = pickle.load(f)

with open(f"{KNOWN_FACES_ENCODED_DIR}/{NUMBER_SAF_ENCODED_FILE}", 'rb') as f:
	number_saf = pickle.load(f)

onlydir = next(os.walk(f"{UNKNOWN_FACES_DIR}"))[1]
count_ac_total = len(onlydir)
count_ac = 1
for nome_ac in os.listdir(UNKNOWN_FACES_DIR):
	onlyfiles = next(os.walk(f"{UNKNOWN_FACES_DIR}/{nome_ac}"))[2]
	count_arq_total = len(onlyfiles)
	count_arq = 1
	for filename_unknown in os.listdir(f"{UNKNOWN_FACES_DIR}/{nome_ac}"):
		print(f"{nome_ac} ({count_ac}/{count_ac_total}) arquivo ({count_arq}/{count_arq_total})")
		extension = {os.path.splitext(filename_unknown)[1]}
		if str(extension).lower() == str({'.jpg'}) or str(extension).lower() == str({'.jpeg'}) or str(extension).lower() == str({'.png'}):
			image = face_recognition.load_image_file(f"{UNKNOWN_FACES_DIR}/{nome_ac}/{filename_unknown}")
			locations = face_recognition.face_locations(image, model=MODEL) #encontra todas as faces na imagem
			if len(locations) != 1:			
				if not os.path.exists(f"{WRONGS_DIR}/{nome_ac}"):
					os.mkdir(f"{WRONGS_DIR}/{nome_ac}")
					arquivo = open(f"{WRONGS_DIR}/{nome_ac}/{WRONGS_FILE}", 'w')
					arquivo.write('nome_arquivo;qtd_face\n')
					arquivo.close()								
				
				arquivo = open(f"{WRONGS_DIR}/{nome_ac}/{WRONGS_FILE}", 'r') # Abra o arquivo (leitura)
				conteudo_wrong = arquivo.readlines()
				conteudo_wrong.append(f"{filename_unknown};{len(locations)}\n")   # insira seu conteúdo
				arquivo = open(f"{WRONGS_DIR}/{nome_ac}/{WRONGS_FILE}", 'w') # Abre novamente o arquivo (escrita)
				arquivo.writelines(conteudo_wrong)    # escreva o conteúdo criado anteriormente nele.
				arquivo.close()

				shutil.copy(f"{UNKNOWN_FACES_DIR}/{nome_ac}/{filename_unknown}", f"{WRONGS_DIR}/{nome_ac}")

			encodings = face_recognition.face_encodings(image, locations)
		#desenhando na imagem
		#image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) #convert a imagem de vga para bgr #kite pra saber os comandos das funções

		for face_encoding, face_location in zip(encodings, locations):			
			results = face_recognition.compare_faces(known_faces, face_encoding, TOLERANCE) #true or false
			#print(f"{filename_unknown} result = {results}")
			#match = []
			count = 0
			for x in results:				
				if x == True:					
					if not os.path.exists(f"{MATCHES_DIR}/{nome_ac}"):
						os.mkdir(f"{MATCHES_DIR}/{nome_ac}")						
						arquivo = open(f"{MATCHES_DIR}/{nome_ac}/{MATCHES_FILE}", 'w')
						arquivo.write('nome_arquivo;num_oco_SAF\n')
						arquivo.close()
					#match.append(number_saf[count])
					arquivo = open(f"{MATCHES_DIR}/{nome_ac}/{MATCHES_FILE}", 'r') # Abra o arquivo (leitura)
					conteudo_match = arquivo.readlines()
					conteudo_match.append(f"{filename_unknown};{number_saf[count]}\n")   # insira seu conteúdo
					arquivo = open(f"{MATCHES_DIR}/{nome_ac}/{MATCHES_FILE}", 'w') # Abre novamente o arquivo (escrita)
					arquivo.writelines(conteudo_match)    # escreva o conteúdo criado anteriormente nele.
					arquivo.close()
					shutil.copy(f"{UNKNOWN_FACES_DIR}/{nome_ac}/{filename_unknown}", f"{MATCHES_DIR}/{nome_ac}")														
				count += 1
		count_arq += 1
	count_ac += 1

# salvar os encoding das faces conhecidas pra não ter que processar toda hora que rodar o programa
# https://github.com/ageitgey/face_recognition/wiki/How-do-I-save-face-encodings-to-a-file%3F