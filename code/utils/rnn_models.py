import torch
import torch.nn as nn

class SMILESModel(nn.Module):
    def __init__(self, vocab_size, emb_dim, \
            hidden_dim, n_layers, dropout=0.3, bidirectional=True):
        super(SMILESModel, self).__init__()
        self.embedding = nn.Embedding(vocab_size, emb_dim)
        self.lstm = nn.LSTM(emb_dim, hidden_dim, n_layers, \
            dropout=dropout, batch_first=True, bidirectional=bidirectional)
        self.dropout = nn.Dropout(dropout)
        if bidirectional:
            self.fc = nn.Linear(2*hidden_dim, 1)
        else:
            self.fc = nn.Linear(hidden_dim, 1)
    
    def forward(self, token_batch):
        out = token_batch.long()
        out = self.embedding(out)
        out, hidden = self.lstm(out)
        out = out[:, -1, :]
        out = self.dropout(out)
        out = self.fc(out)
        return out


class Tokenizer():
    def __init__(self):
        self.vocab = ["PAD", "UNK", "Br", "Cl", "H", \
            "N", "O", "S", "P", "F", "I", \
            "b", "c", "n", "o", "s", "p", "[", "]", \
            "(", ")", ".", " ", "=", "#", \
            "+", "-", ":", "~", "@", "*", "%", \
            "/", "\\", "0", "1", "2", "3", "4", \
            "5", "6", "7", "8", "9"]
        self.i2v = {i: v for i, v in enumerate(self.vocab)}
        self.v2i = {v:i for i, v in enumerate(self.vocab)}
        
    def token2idx(self, v):
        if v in self.vocab:
            return self.v2i[v]
        else:
            return self.v2i["UNK"]
    
    def encode(self, smi):
        lst = []
        for v in smi:
            lst.append(self.token2idx(v))
        return lst
