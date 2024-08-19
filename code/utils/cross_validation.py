from sklearn.model_selection import KFold
from copy import deepcopy

default_config = {
    "loss": "mse", 
    "optimizer": "Adam",
    "lr": 1e-2,
    "epochs": 20, 
    "batch_size": 256,
}

class CrossValidation:
    def __init__(self, num_fold=5, seed=42) -> None:
        self.num_fold = num_fold
        self.kf = KFold(n_splits=num_fold, shuffle=True, random_state=seed)
        self.executed = False
        self.training = []
        self.evaluation = []
        self.history = []
        
    def run_one_fold(self, model, train_set, test_set, **config):

        
        raise NotImplemented
    
    def run(self, model, dataset, **config):
        all_config = deepcopy(default_config)
        all_config.update(config)
        
        self.executed = True
        raise NotImplemented