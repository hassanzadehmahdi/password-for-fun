class Password:
    def __init__(self):
        self.password = ""

    def update_password(self, addition):
        self.password += addition

    def __str__(self):
        return self.password
