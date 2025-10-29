class MetricCalculator:
    def __init__(self):
        self.results = []
    
    def calculate_mean(self, data):

        if not data: 
            raise ValueError("Cannot calculate mean of empty list")
        return sum(data) / len(data)
    
    def calculate_accuracy(self, y_true, y_pred):
        if not y_true or not y_pred:
            raise ValueError("Input lists cannot be empty")
        
        if len(y_true) != len(y_pred):
            raise ValueError("Input lists must have the same length")
            
        correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
        return correct / len(y_true)
    
    
    def add_metric(self, name, value):
        self.results.append((name, value))
    
    def get_results(self):
        return self.results
