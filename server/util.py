# import ml classifier libraries
import os
import torch
from torch.utils.data import TensorDataset
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler

BATCH_SIZE = 5
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def load_model():

    tokenizer = BertTokenizer.from_pretrained(
        'bert-base-uncased', do_lower_case=True)
    
    # Check for device CPU/GPU
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    # Initialize the model
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                            num_labels=12,
                                                            output_attentions=False,
                                                            output_hidden_states=False)
    model.to(device)

    # File with trained model state is being loaded and used here
    model.load_state_dict(torch.load(
        'finetuned_BERT_final.model', map_location=torch.device('cpu')))
    model.eval()

    return model, device, tokenizer
