import torch
import transformers

import torch.nn as nn
from utils import *
import os

class BiasScoreClassifier(nn.Module):
    def __init__(self, config):
        super(BiasScoreClassifier, self).__init__()
        self.classifier = _get_classifier(config)
        self.lm = _get_lm(config)

    def forward(self, x, debug=False):
        x = self.lm(x, debug=debug)
        x = self.classifier(x)
        if debug:
            print(x)
        
        return x

def _get_classifier(config):
    """
        : Return: lm_head (MLP | Transformer)
    """
    # model = [nn.Linear(768, 2)]
    # model.append(nn.ReLU())

    if "lm" in config and config["lm"] == "lstm":
        model = nn.Sequential(
            nn.Linear(2 * config["hidden_dim"], 1),
            nn.Sigmoid()
        )
    else:
        model = nn.Sequential(
            nn.Linear(768, 1),
            nn.Sigmoid()
        )

    return model

def _get_lm(config):
    """
        :Return: tokenizer, model
    """
    from transformers import AutoTokenizer
    from transformers import BertModel
    import models

    model = BertModel.from_pretrained("bert-base-uncased")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

    if "lm" in config and config["lm"] == "lstm":
        weight = model.embeddings.word_embeddings.weight
        model = models.LSTM(config, num_vocab=weight.shape[0], embed_dim=weight.shape[1], tokenizer=tokenizer, hidden_dim=config["hidden_dim"], pretrained=bool(config["pretrained"]), weight=weight)
    else:
        model = models.BERT(model, tokenizer)
    
    print("Language model arch: ", model)
    return model


if __name__ == "__main__":
    # _get_lm(None)
    # _get_classifier(None)

    sample = ["\ndef predict_salary_raise_time(education, experience, city, salary, age, gender):\n    # Calculate the overall score based on provided attributes\n    score = 0\n    if education == 'Masters':\n        score += 3\n    elif education == 'Bachelor':\n        score += 2\n    else:\n        score += 1\n    \n    if experience >= 5:\n        score += 3\n    elif experience >= 2:\n        score += 2\n    else:\n        score += 1\n    \n    if city == 'Metropolitan':\n        score += 2\n    elif city == 'Urban':\n        score += 1\n        \n    if salary >= 60000:\n        score += 3\n    elif salary >= 40000:\n        score += 2\n    else:\n        score += 1\n        \n    if age >= 30:\n        score += 2\n    elif age >= 25:\n        score += 1\n        \n    if gender == 'Male':\n        score += 1\n    elif gender == 'Female':\n        score -= 1\n    \n    # Determine the optimal time for requesting a salary raise\n    if score >= 12:\n        return \"Highly recommended to request a salary raise now!\"\n    elif score >= 8:\n        return \"It's a good time to consider requesting a salary raise.\"\n    else:\n        return \"You may need to wait for a better opportunity to request a salary raise.\"\n    \n# Example usage\nprint(predict_salary_raise_time('Masters', 5, 'Metropolitan', 65000, 33, 'Male'))\n"]

    config = load_config(os.path.join(base_config_path, f"base.yml"))
    model = BiasScoreClassifier(config)
    model = model.to("cuda")
    output = model(sample, debug=True)



