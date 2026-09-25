class AIModel:
    def __init__(self, model_name):
        self.model_name = model_name
        self.is_trained = False

    def train(self):
        self.is_trained = True

    def describe(self):
        return f"Model: {self.model_name}"


class ClassificationModel(AIModel):
    def __init__(self, model_name, classes):
        super().__init__(model_name)
        self.classes = classes

    def describe(self):
        return f"{super().describe()} | Classes: {self.classes}"


class RegressionModel(AIModel):
    def __init__(self, model_name, target_name):
        super().__init__(model_name)
        self.target_name = target_name

    def describe(self):
        return f"{super().describe()} | Target: {self.target_name}"


# ClassificationModel and RegressionModel are both AIModel types.
def main():
    classification = ClassificationModel("Image Classifier", ["Cat", "Dog", "Bird"])

    regression = RegressionModel("House Price Predictor", "House Price")

    classification.train()
    regression.train()

    print(classification.describe())
    print("Training state:", classification.is_trained)

    print()

    print(regression.describe())
    print("Training state:", regression.is_trained)


if __name__ == "__main__":
    main()
