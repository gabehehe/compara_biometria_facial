import face_recognition
import os
import pickle
'''
KNOWN_FACES_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\known_faces'
KNOWN_FACES_ENCODED_DIR = 'C:\\Users\\ITI\\Documents\\Projetos\\Reconhecimento_facial\\known_faces_encoded'
'''

KNOWN_FACES_DIR = 'G:\\fraudes\\2019\\Biometrias_SAF\\Junto'
KNOWN_FACES_ENCODED_DIR = 'G:\\fraudes\\2019\\Biometrias_SAF\\Biometrias_Python_Encoded'

KNOWN_FACES_ENCODED_FILE = 'dataset_faces_encoded.dat'
NUMBER_SAF_ENCODED_FILE = 'dataset_number_saf_encoded.dat'

MODEL = "hog"

print("Carregando imagens do SAF para comparação")

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
		extension = {os.path.splitext(filename_known)[1]}
		if str(extension).lower() == str({'.jpg'}) or str(extension).lower() == str({'.jpeg'}) or str(extension).lower() == str({'.png'}):
			image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{ano}/{filename_known}")
			locations = face_recognition.face_locations(image, model=MODEL) #encontra todas as faces na imagem
			if len(locations) == 1:
				encoding = face_recognition.face_encodings(image) [0] #só pega a primeira face da imagem, para imagens que tem mais de uma face
				known_faces.append(encoding)
				number_saf.append(filename_known)
		count_oco += 1
	count_ano += 1

with open(f"{KNOWN_FACES_ENCODED_DIR}/{KNOWN_FACES_ENCODED_FILE}", 'wb') as f:
    pickle.dump(known_faces, f)
    
with open(f"{KNOWN_FACES_ENCODED_DIR}/{NUMBER_SAF_ENCODED_FILE}", 'wb') as f:
    pickle.dump(number_saf, f)