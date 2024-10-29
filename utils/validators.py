from datetime import datetime

def validate_due_date(due_date):
    # Verifica se a data inserida não é menor que a atual
    return due_date > datetime.now()
