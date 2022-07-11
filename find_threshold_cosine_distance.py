import glob 
import os 
import shutil
import time 
import cv2
import numpy as np 
import matplotlib.pyplot as plt 
from model import load_emb_model
from get_emb import get_emb
from metric import cosine_distance, euclidean_distance

dates = [20220623, 20220624, 20220629, 20220630]
has_padding = [20220623, 20220624, 20220629, 20220630]
padding = 50
MODEL_NAME = 'opencv'
model = load_emb_model(MODEL_NAME)

in_embs = []
out_embs = []

for date in dates:
    dataset = r'D:\\ParkingAppData\\{}\\FACE_DIR_NO_MASK_CLEANED\\'.format(date)

    folders = sorted(glob.glob(dataset + '*\\'))
    
    for folder in folders:
        in_path = glob.glob(folder + 'FACE*\IN_*.png')[0]
        out_path = glob.glob(folder + 'FACE*\OUT_*.png')[0]

        img = cv2.imread(in_path)
        if date in has_padding:
            img = img[padding:-padding, padding:-padding, :]
        emb = get_emb(MODEL_NAME, model, img)
        in_embs.append(emb)

        img = cv2.imread(out_path)
        if date in has_padding:
            img = img[padding:-padding, padding:-padding, :]
        emb = get_emb(MODEL_NAME, model, img)
        out_embs.append(emb)

in_emb_arr = np.array(in_embs)
out_emb_arr = np.array(out_embs)
cos_distance = cosine_distance(in_emb_arr, out_emb_arr)
print(cos_distance)
same_distance = np.diagonal(cos_distance)
cosine_distance_copy = cos_distance.copy()
np.fill_diagonal(cosine_distance_copy, np.NINF)
diff_distance = np.max(cosine_distance_copy, axis=1)
print(diff_distance)

plt.hist(same_distance, bins=30)
plt.hist(diff_distance, bins=30, alpha=0.7, color='r')
plt.legend(['same person', 'diff person'])
plt.xlabel("Distance")
plt.title("Cosine Distance On Parking Data With SFace")

plt.show()
