import numpy as np

def cosine_distance(in_emb, out_emb):
    norm_in_emb = np.linalg.norm(in_emb, axis=1)
    norm_out_emb = np.linalg.norm(out_emb, axis=1)

    mul = np.dot(in_emb, out_emb.T)
    norm_in_emb = norm_in_emb.reshape(-1, 1)
    norm_out_emb = norm_out_emb.reshape(1, -1)

    mul_norm = np.dot(norm_in_emb, norm_out_emb)
    cosine = mul / mul_norm
    cosine_distance = 1 - cosine

    return cosine_distance

def euclidean_distance(in_emb, out_emb):
    out_emb = np.expand_dims(out_emb,axis=1)
    euclidean_distance = in_emb - out_emb
    euclidean_distance = np.sum(np.multiply(euclidean_distance, euclidean_distance), axis=2)
    euclidean_distance = np.sqrt(euclidean_distance)

    return euclidean_distance