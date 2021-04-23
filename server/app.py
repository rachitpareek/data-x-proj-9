import time

start = time.time()

import json
import pickle
import numpy as np
from util import *
import pandas as pd
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, redirect, url_for, make_response

# Initialize the Flask server
app = Flask(__name__)

# Load model into memory
label_dict = {0: 'rumor',
                1: 'hate',
                2: 'unreliable',
                3: 'conspiracy',
                4: 'clickbait',
                5: 'satire',
                6: 'fake',
                7: 'reliable',
                8: 'bias',
                9: 'political',
                10: 'junksci',
                11: 'unknown'}

model, device, tokenizer = load_model()

print("TIME TO START SERVER:", time.time() - start)

# Route for full service webpage
@app.route('/')
def home():
    return render_template('home.html')

# Route for informational page webpage
@app.route('/info')
def info():
    return render_template('info.html')

# API route
@app.route('/api', methods=['GET', 'POST'])
def apii():

    global model, device, tokenizer, BATCH_SIZE

    start = time.time()

    data = json.loads(request.data)["message"]

    # Remove extra spaces from parsing HTML
    data = " ".join(data.split())

    if len(data) == 0 or len(data.strip()) == 0 or data is None:
        return "The server did not receive any text to classify."

    print("DATA:", data)

    validate_data = pd.DataFrame([[data]], columns=['content'])

    encoded_data_val = tokenizer.batch_encode_plus(
        validate_data.content.values, 
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=500,
        return_tensors='pt'
    )

    input_ids_val = encoded_data_val['input_ids']
    attention_masks_val = encoded_data_val['attention_mask']
    dataset_val = TensorDataset(input_ids_val, attention_masks_val)

    dataloader_validation = DataLoader(
        dataset_val, sampler=SequentialSampler(dataset_val), batch_size=BATCH_SIZE)

    predictions = []
    for batch in dataloader_validation:
        batch = tuple(b.to(device) for b in batch)
        inputs = {'input_ids': batch[0], 'attention_mask': batch[1]}
        with torch.no_grad():
            outputs = model(**inputs)
        logits = outputs[0]
        logits = logits.detach().cpu().numpy()
        predictions.append(logits)

    preds = np.concatenate(predictions, axis=0)
    a = np.argmax(preds, axis=1).flatten()

    std = [i[1] for i in sorted(list(zip(preds[0], label_dict.values())),key=lambda x:x[0])[::-1]]
    print("SORTED CLASSES:", std)

    print("TIME:", time.time() - start)

    return " ".join([f"{str(i[0]+1)}: {i[1]};" for i in list(enumerate(std))][:3])


@app.after_request
def after_request_func(response):
    response.direct_passthrough = False
    origin = request.headers.get('Origin')
    response = make_response(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run()
