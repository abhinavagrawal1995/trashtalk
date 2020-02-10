from fastai.vision import *
import requests
import cv2

# Input Azure Object Detection API key here
subscription_key = ''

model_training_relative = ""
trained_model_path = model_training_relative + "data"
learn = load_learner(trained_model_path)

classes = learn.data.classes

threshold = 0.5

def getConfidenceForTrashPrediction(output, labels):
    confidenceForLabels = output[2]

    sumConfidence = 0
    for label in labels:
        index = classes.index(label)
        confidence = confidenceForLabels[index]
        sumConfidence += confidence
    return float(sumConfidence)


def magic(image_path):
    img = cv2.imread(image_path)
    output = getAzureCVData(image_path)

    if output is not None:
        r = output['rectangle']
        crop_img = img[r['y']:r['y'] + r['h'], r['x']:r['x'] + r['w']] #img[y:y+h, x:x+w]
        cv2.imwrite(image_path, crop_img)

    output = learn.predict(open_image(image_path))

    recyclables = ['cardboard', 'plastic', 'glass', 'paper']
    landfill = ['metal', 'trash']
    compost = ['food']


    labels = {'recycle': recyclables,
           'landfill': landfill,
           'compost': compost}


    maxConfidence = float(max(output[2]))
    nnMaterialType = str(output[0])

    nnTrashType = None
    for label in labels:
        materials = labels[label]
        if nnMaterialType in materials:
            nnTrashType = label

    if maxConfidence < threshold:
        # print('calling azure')
        data = getAzureCVData(image_path)
        if data is not None:
            azureTrashType = data['trashType']
            azureConfidence = data['confidence']
            # print('azure confidence=', azureConfidence)
            # print('azureTrashType=', azureTrashType)
            return azureTrashType

    return nnTrashType


def getAzureCVData(image_path):
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}

    url = 'https://eastus.api.cognitive.microsoft.com/vision/v2.0/detect'

    recyclable = ['paper', 'newspaper', 'magazine', 'catalog', 'map', 'phonebook', 'mail', 'paperboard', 'tissue',
                  'box', 'card', 'folder', 'can', 'straw', 'carton', 'book', 'cup', 'envelope', 'cardboard', 'vase',
                  'plastic', 'boxboard', 'box', 'metal', 'tin', 'aluminum', 'dish', 'plate', 'tray', 'cookware',
                  'copper', 'jewelry', 'key', 'steel', 'pot', 'bucket', 'pan', 'tin', 'pyrex', 'utensil', 'glass',
                  'bottle', 'jar', 'cup', 'jug', 'metal', 'spoon', 'fork', 'office paper', 'blind', 'curtain']

    landfill = ['battery', 'computer', 'electronics', 'bulb', 'microfilm', 'cell phone', 'phone', 'mobile phone',
                'equipment', 'inkjet', 'cartridge', 'inkjet cardridge', 'cd', 'disk', 'tire', 'ink cartridge', 'tv',
                'power cord', 'personal computer', 'laptop', 'portable computer']

    compost = ['food', 'fruit', 'vegetable', 'apple', 'pear', 'banana', 'cucumber', 'strawberry', 'apricots', 'avocado',
               'blackberry', 'cherry', 'coconut', 'date', 'durian', 'dragonfruit', 'grape', 'grapefruit', 'kiwi',
               'lime', 'lemon', 'lychee', 'mango', 'melon', 'nectarine', 'olive', 'orange', 'peach', 'pineapple',
               'plum', 'pomegranate', 'pomelo', 'raspberries', 'watermelon', 'broccoflower', 'broccoli', 'cabbage',
               'celery', 'corn', 'basil', 'rosemary', 'sage', 'thyme', 'kale', 'lettuce', 'mushroom', 'onion', 'pepper',
               'ginger', 'wasabi', 'squash', 'tomato', 'potato', 'hair', 'wood', 'popcorn', 'leaves', 'egg', 'pasta',
               'fish', 'beef', 'chicken', 'pork', 'meat', 'soy', 'pumpkin', 'nut', 'cheese', 'toothpicks', 'pickles',
               'feather', 'fur', 'bone']

    trashTypes = {}
    trashTypes['recycle'] = recyclable
    trashTypes['landfill'] = landfill
    trashTypes['compost'] = compost

    image_data = open(image_path, "rb").read()
    r = requests.post(url, data=image_data, headers=headers)
    data = r.json()

    indiciesToRemove = []
    if 'objects' in data:
        objects = data['objects']
        for i in range(len(objects)):
            object = objects[i]
            objectName = object['object']
            if objectName in ['person', 'human', 'woman', 'man', 'hand']:
                indiciesToRemove.append(i)

        indiciesToRemove.reverse()

        for index in indiciesToRemove:
            objects.pop(index)

        if len(objects) > 0:
            object = objects[0]
            objectName = object['object'].lower()
            confidence = object['confidence']
            rectangle = object['rectangle']
            for label in trashTypes.keys():
                items = trashTypes[label]
                if objectName in items:
                    ret = {'object': objectName, 'trashType': label, 'confidence': confidence, 'rectangle': rectangle}
                    return ret
    return None

