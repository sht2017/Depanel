import os
def ifinstall():
    if os.path.isfile('./.key'):
        return bool(True)
    else:
        return bool(False)