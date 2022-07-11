import glob 
import os 
import shutil
import time 


dates = [20220706, 20220707]
has_padding = []
padding = 50

for date in dates:
    dataset = r'D:\\ParkingAppData\\{}'.format(date)

    org_face_in_paths = sorted(glob.glob(dataset + '\\FACE_DETECT_CAM_MAT_VAO\\*.png'))
    org_face_out_paths = sorted(glob.glob(dataset + '\\NO_MASK_FACE_DETECT_CAM_MAT_RA\\*.png'))

    dir_face = os.path.join(dataset, "FACE_DIR_NO_MASK")
    if not os.path.exists(dir_face):
        print(dir_face)
        os.mkdir(dir_face)
        time.sleep(1)
    else:
        shutil.rmtree(dir_face)
    
    face_ids = []

    for out_path in org_face_out_paths:
        file_name = os.path.split(out_path)[1]
        face_id = file_name.split('_')[0]

        if face_id not in face_ids:
            face_ids.append(face_id)

            face_id_path = os.path.join(dir_face, face_id)
            os.mkdir(face_id_path)

        new_path = os.path.join(face_id_path, "OUT_"+file_name)
        shutil.copy(out_path, new_path)

    for in_path in org_face_in_paths:
        file_name = os.path.split(in_path)[1]
        face_id = file_name.split('_')[0]

        if face_id in face_ids:
            face_id_path = os.path.join(dir_face, face_id)

            new_path = os.path.join(face_id_path, "IN_"+file_name)
            shutil.copy(in_path, new_path)