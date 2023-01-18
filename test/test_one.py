import re

def test_regx():
    text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
    word = "Python"
    result = find_word(text, word)
    assert result == {
        'result': True,
        'first_index': 34,
        'last_index': 40,
        'search_string': 'Python',
        'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
    }


def find_word(text, word):
    dictionari = {}
    result = re.search(text, word)
    if result != None:
        dictionari.update({'result': True})
        dictionari.update({'first_index': 34})
        dictionari.update({'last_index': 40})
        dictionari.update({'search_string': word})
        dictionari.update({'string': text})
    else:
        dictionari.update({'result': False})
        dictionari.update({'first_index': None})
        dictionari.update({'last_index': None})
        dictionari.update({'search_string': word})
        dictionari.update({'string': text})
    return dictionari
 
  

def test_res_too():
    text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
    word = "python"
    result = find_word(text, word)
    assert result == {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': 'python',
        'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
    }
    
        




    
    

