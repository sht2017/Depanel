import os
def installed():
    if os.path.isfile('./.key'):
        return bool(True)
    else:
        return bool(False)