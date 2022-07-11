def get_emb(model_name, model, img):
    if model_name == "opencv":
        # TODO here: apply alignCrop function (hard)
        emb = model.feature(img)[0]

        return emb
    
    elif model_name == "arcface":
        # TODO: add arcface emb
        pass