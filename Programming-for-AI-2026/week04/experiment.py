class Experiment:
    def __init__(self, experiment_id, model_name, dataset_name, accuracy): 
        if not 0 <= accuracy <= 1:            
            raise ValueError("Accuracy must be between 0 and 1.")        
        self.experiment_id = experiment_id        
        self.model_name = model_name        
        self.dataset_name = dataset_name         
        self.accuracy = accuracy      
    def to_dictionary(self):         
        return {             
                "experiment_id": self.experiment_id,             
                "model_name": self.model_name,             
                "dataset_name": self.dataset_name,             
                "accuracy": self.accuracy,         
            } 