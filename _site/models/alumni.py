class Alumni:
    def __init__(self, name, batch):
        self.name = name
        self.batch = batch

    def __str__(self):
        return f"{self.name} ({self.batch})"
    