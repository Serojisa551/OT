def cutting(mail):
    mail_copy = ""
    for elm in mail:
        if elm == "@":
            return mail_copy
        else:
            mail_copy += elm