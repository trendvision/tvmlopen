from fastai.vision import *
import requests
from io import BytesIO

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

"""
    Usage:
        path_to_model = 'folder/with/export.pkl'
        path_to_dir = 'folder/with'
        
        # load model
        learner = load_learner_from_dir(path_to_dir)
        
        # predict
        pred = predict_from_url(learner, url)
"""

def load_learner_from_dir(model_directory):
    learn = load_learner(model_directory)
    if hasattr(learn.model, 'module'):
        learn.model = learn.model.module
    return learn


def load_image_form_url(url):
    response = requests.get(url).content
    try:
        img = open_image(BytesIO(response))
    except OSError as e:
        print(e)
        return None
    return img


def predict_from_directory(learner, image_directory):
    pred_dict = {}
    for sample in get_image_files(image_directory):
        if Path(sample).suffix not in ['.jpg', '.png']: continue
        try:
            img = open_image(sample)
        except OSError:
            pred_dict[sample] = None
            continue
        pred, _, _ = learner.predict(img)
        pred_dict[str(sample)] = str(pred)
    return pred_dict


def predict_from_url(learner, img_url):
    img = load_image_form_url(img_url)
    pred, _, _ = learner.predict(img)
    return pred


def predict_from_bytes(learner, url):
    img_bytes = requests.get(url).content
    try:
        img = open_image(BytesIO(img_bytes))
    except OSError as e:
        print(e)
        return None
    pred, _, _ = learner.predict(img)
    return pred
