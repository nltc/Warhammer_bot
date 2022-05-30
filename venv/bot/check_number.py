import phonenumbers

def number_check(message):

    '''Проверка валидности номера'''

    try:
        if phonenumbers.is_valid_number(phonenumbers.parse(message, 'RU')):
            return True

        else:
            return False
    
    except Exception as e:
        return False
    
    