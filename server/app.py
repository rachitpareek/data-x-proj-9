import json
import time
import pickle
from util import *
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, redirect, url_for, make_response

# start flask
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# render extension webpage


@app.route('/')
def extension():
    return render_template('extension.html')

# api route


@app.route('/api', methods=['GET', 'POST'])
def home():

    start = time.time()

    text = {}

    print("was there any data?")
    if request.data:
        print("RECEIVED DATA.")
        text = json.loads(request.data)
        print("DATA", text)

    # with open("./resources/model.pkl", 'rb') as file:
    #     model = pickle.load(file)

    # with open("./resources/vectorizer.pkl", 'rb') as file:
    #     vectorizer = pickle.load(file)

    # if "message" not in data:
    #     data["message"] = "Space lasers cause forest fires"

    # output = model.predict(vectorizer.transform([data["message"]]))

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

    import torch
    import numpy as np
    import pandas as pd
    from torch.utils.data import DataLoader, RandomSampler, SequentialSampler
    from transformers import BertTokenizer, BertForSequenceClassification
    from torch.utils.data import TensorDataset

    data = [[text["message"]]]
    validate_data = pd.DataFrame(data, columns=['content'])

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

    encoded_data_val = tokenizer.batch_encode_plus(
        validate_data.content.values,  #article text being passed to encoder
        add_special_tokens=True, 
        return_attention_mask=True, 
        pad_to_max_length=True, 
        max_length=500, 
        return_tensors='pt'
    )

    input_ids_val = encoded_data_val['input_ids']
    attention_masks_val = encoded_data_val['attention_mask']
    dataset_val = TensorDataset(input_ids_val, attention_masks_val)

    batch_size = 2

    dataloader_validation = DataLoader(dataset_val, sampler=SequentialSampler(dataset_val), batch_size=batch_size)

    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                        num_labels=12,
                                                        output_attentions=False,
                                                        output_hidden_states=False)

    model.to(device)

    #file with model state is being loaded and used here

    model.load_state_dict(torch.load('finetuned_BERT_epoch_3.model', map_location=torch.device('cpu')))

    model.eval()

    predictions = []
    for batch in dataloader_validation:

        batch = tuple(b.to(device) for b in batch)

        inputs = {'input_ids':      batch[0],'attention_mask': batch[1],}

        with torch.no_grad():        
            outputs = model(**inputs)

        logits = outputs[0]

        logits = logits.detach().cpu().numpy()
        #label_ids = inputs['labels'].cpu().numpy()
        predictions.append(logits)
    predictions = np.concatenate(predictions, axis=0)
    predictions
    a = np.argmax(predictions, axis=1).flatten()

    print(label_dict[a[0]])

    print("DATA:", data)

    print("TIME:", time.time()-start)

    return str(label_dict[a[0]])


@app.after_request
def after_request_func(response):
    response.direct_passthrough = False
    origin = request.headers.get('Origin')
    response = make_response(response)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


app.run(debug=True)
