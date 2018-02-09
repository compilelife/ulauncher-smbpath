import sys

def is_linux_path(path):
    return path.startswith('smb://')


def to_linux_path(path):
    path = 'smb://'+path[2:]
    return path.replace('\\', '/')


def is_windows_path(path):
    return path.startswith('\\\\')


def to_windows_path(path):
    path = '\\\\'+path[6:]
    return path.replace('/', '\\')


def convert_path(path):
    if is_linux_path(path):
        return to_windows_path(path)
    elif is_windows_path(path):
        return to_linux_path(path)
    else:
        return 'not a valid samba path'
