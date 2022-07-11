import glob 
import os 
import shutil
import time 
import cv2
import numpy as np 
from model import load_emb_model
from get_emb import get_emb
from metric import cosine_distance, euclidean_distance

dates = [20220623, 20220624, 20220629, 20220630]
has_padding = [20220623, 20220624, 20220629, 20220630]
padding = 50
MODEL_NAME = 'opencv'
model = load_emb_model(MODEL_NAME)

for date in dates:
    dataset = r'D:\\ParkingAppData\\{}\\FACE_DIR_NO_MASK_CLEANED\\'.format(date)

    folders = sorted(glob.glob(dataset + '*\\'))
    
    for folder in folders:
        org_face_in_paths = sorted(glob.glob(folder + 'IN_*.png'))
        org_face_out_paths = sorted(glob.glob(folder + 'OUT_*.png'))

        in_embs = []
        out_embs = []

        for in_path in org_face_in_paths:
            img = cv2.imread(in_path)
            if date in has_padding:
                img = img[padding:-padding, padding:-padding, :]
            emb = get_emb(MODEL_NAME, model, img)
            in_embs.append(emb)

        for out_path in org_face_out_paths:
            img = cv2.imread(out_path)
            if date in has_padding:
                img = img[padding:-padding, padding:-padding, :]
            emb = get_emb(MODEL_NAME, model, img)
            out_embs.append(emb)

        in_emb_arr = np.array(in_embs)
        out_emb_arr = np.array(out_embs)
        
        cos_distance = cosine_distance(in_emb_arr, out_emb_arr)
        min_cos = np.min(cos_distance)
        min_in, min_out = np.unravel_index(np.argmin(cos_distance, axis=None), cos_distance.shape)
        
        two_face_dir = os.path.join(folder, "FACE_{}".format(min_cos))
        os.mkdir(two_face_dir)

        # copy 2 face which best same
        shutil.copy(org_face_in_paths[min_in], two_face_dir)
        shutil.copy(org_face_out_paths[min_out], two_face_dir)
        
