class Register_Options:
    def __init__(self, username_github: str, pass_github: str, username_mail: str, pass_mail: str, first_name: str,
                 last_name: str):
        self.username_github = username_github
        self.pass_github = pass_github
        self.username_mail = username_mail
        self.pass_mail = pass_mail
        self.last_name = last_name
        self.first_name = first_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name
