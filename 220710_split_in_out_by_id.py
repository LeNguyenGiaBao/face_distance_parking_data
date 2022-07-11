import os 
import glob 
import shutil 
import tqdm

dataset_path = 'D:/ParkingAppData/20220710'

in_dataset_path = glob.glob(dataset_path + '/FACE_DETECT_CAM_MAT_VAO/*.*')
out_dataset_path = glob.glob(dataset_path + '/FACE_DETECT_CAM_MAT_RA/*.*')

print("ALL FACE IN:", len(in_dataset_path))
print("ALL FACE OUT:", len(out_dataset_path))

face_in_folder_path = dataset_path + '/FACE_IN/'
if not os.path.exists(face_in_folder_path):
    os.mkdir(face_in_folder_path)
else:
    print("Cannot create face in folder")
    exit()

face_out_folder_path = dataset_path + '/FACE_OUT/'
if not os.path.exists(face_out_folder_path):
    os.mkdir(face_out_folder_path)
else:
    print("Cannot create face out folder")
    exit()

same_face_folder_path = dataset_path + '/FACE_DIR/'
if not os.path.exists(same_face_folder_path):
    os.mkdir(same_face_folder_path)
else:
    print("Cannot create same face folder")
    exit()

abnormal_face_in_folder_path = dataset_path + '/FACE_IN_ABNORMAL/'
if not os.path.exists(abnormal_face_in_folder_path):
    os.mkdir(abnormal_face_in_folder_path)
else:
    print("Cannot create abnormal face in folder")
    exit()

abnormal_face_out_folder_path = dataset_path + '/FACE_OUT_ABNORMAL/'
if not os.path.exists(abnormal_face_out_folder_path):
    os.mkdir(abnormal_face_out_folder_path)
else:
    print("Cannot create abnormal face out folder")
    exit()

in_id_plate = []
out_id_plate = []

print("-------------------- PROCESS FACE IN --------------------------")
for path in tqdm.tqdm(in_dataset_path):
    file_name_ext = os.path.split(path)[1]
    id_plate = file_name_ext.split("_")[0]
    
    if id_plate not in in_id_plate:
        in_id_plate.append(id_plate)
        os.mkdir(face_in_folder_path + id_plate)

    new_path = os.path.join(face_in_folder_path + '/' + id_plate, "IN_"+ file_name_ext)
    shutil.copy(path, new_path)

with open(os.path.join(face_in_folder_path, 'in_id_face.txt'), 'w') as f:
    f.write('\n'.join(in_id_plate))

print("-------------------- PROCESS FACE OUT --------------------------")
for path in tqdm.tqdm(out_dataset_path):
    file_name_ext = os.path.split(path)[1]
    id_plate = file_name_ext.split("_")[0]
    
    if id_plate not in out_id_plate:
        out_id_plate.append(id_plate)
        os.mkdir(face_out_folder_path + id_plate)

    new_path = os.path.join(face_out_folder_path + '/' + id_plate, "OUT_"+ file_name_ext)
    shutil.copy(path, new_path)

with open(os.path.join(face_out_folder_path, 'out_id_face.txt'), 'w') as f:
    f.write('\n'.join(out_id_plate))
print('check')
print('29P141417')
print('29P141417' in in_id_plate)
print('29P141417' in out_id_plate)
print("-------------------- GET SAME ID ------------------------------")
for id_plate in in_id_plate:
    if id_plate in out_id_plate:  # same id 
        # create same face folder
        os.mkdir(same_face_folder_path + id_plate)

        # copy face in to same face
        old_path = glob.glob(face_in_folder_path + '/' + id_plate + '/*.*')
        for path in old_path:
            shutil.copy(path, same_face_folder_path + id_plate)

        # copy face out to same face
        old_path = glob.glob(face_out_folder_path + '/' + id_plate + '/*.*')
        for path in old_path:
            shutil.copy(path, same_face_folder_path + id_plate)

        # remove in 2 list 
        in_id_plate.remove(id_plate)
        out_id_plate.remove(id_plate)

for id_plate in out_id_plate:
    if id_plate in in_id_plate:  # same id 
        # create same face folder
        os.mkdir(same_face_folder_path + id_plate)

        # copy face in to same face
        old_path = glob.glob(face_in_folder_path + '/' + id_plate + '/*.*')
        for path in old_path:
            shutil.copy(path, same_face_folder_path + id_plate)

        # copy face out to same face
        old_path = glob.glob(face_out_folder_path + '/' + id_plate + '/*.*')
        for path in old_path:
            shutil.copy(path, same_face_folder_path + id_plate)

        # remove in 2 list 
        in_id_plate.remove(id_plate)
        out_id_plate.remove(id_plate)

print("-------------------- GET ABNORMAL IN ID ------------------------------")
for id_plate in tqdm.tqdm(in_id_plate):
    os.mkdir(abnormal_face_in_folder_path + id_plate)

    # copy face in to abnormal face in
    old_path = glob.glob(face_in_folder_path + '/' + id_plate + '/*.*')
    for path in old_path:
        shutil.copy(path, abnormal_face_in_folder_path + id_plate)

print("-------------------- GET ABNORMAL OUT ID ------------------------------")
for id_plate in tqdm.tqdm(out_id_plate):
    os.mkdir(abnormal_face_out_folder_path + id_plate)

    # copy face out to abnormal face out
    old_path = glob.glob(face_out_folder_path + '/' + id_plate + '/*.*')
    for path in old_path:
        shutil.copy(path, abnormal_face_out_folder_path + id_plate)

print("-------------------- DONE ------------------------------")