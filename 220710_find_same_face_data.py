import os 
import glob 
import cv2 
import shutil
import numpy as np 
import tqdm
from model import load_emb_model
from get_emb import get_emb
from metric import cosine_distance, euclidean_distance

MODEL_NAME = 'opencv'
model = load_emb_model(MODEL_NAME)

dataset_path = 'D:/ParkingAppData/final_face_data/'
out_dir = 'D:/ParkingAppData/result_sface/'
if not os.path.exists(out_dir):
    os.mkdir(out_dir)
else:
    print("Cannot create output folder")
    exit()

ids = os.listdir(dataset_path)
print("Num identity:", len(ids))

for id in tqdm.tqdm(ids):
    in_faces = glob.glob(dataset_path + id + '/IN_*.*')
    out_faces = glob.glob(dataset_path + id + '/OUT_*.*')

    if len(in_faces) == 0 or len(out_faces) == 0:
        continue

    in_embs = []
    out_embs = []

    for path in in_faces:
        img = cv2.imread(path)
        img = img[50:-50, 50:-50, :]

        emb = get_emb(MODEL_NAME, model, img)
        in_embs.append(emb)

    for path in out_faces:
        img = cv2.imread(path)
        img = img[50:-50, 50:-50, :]

        emb = get_emb(MODEL_NAME, model, img)
        out_embs.append(emb) 

    in_emb_arr = np.array(in_embs)
    out_emb_arr = np.array(out_embs)
    
    cos_distance = cosine_distance(in_emb_arr, out_emb_arr)
    min_cos = np.min(cos_distance)
    min_in, min_out = np.unravel_index(np.argmin(cos_distance, axis=None), cos_distance.shape)

    folder_min_cos_id = out_dir + '{:.4f}_{}'.format(min_cos, id)
    os.mkdir(folder_min_cos_id)

    # copy 2 face which best same
    shutil.copy(in_faces[min_in], folder_min_cos_id)
    shutil.copy(out_faces[min_out], folder_min_cos_id)