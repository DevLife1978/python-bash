import os

def bash(f):
        def bash_wrapper(*args, **kwargs):
            print('wrapper :' + str(*args))
            return os.system(f(*args, **kwargs))
        return bash_wrapper

@bash
def ls(args=None):
    print('ls ' + str(args))
    if args is not None:
        return 'ls {args}'.format(args=args)
    else:
        return 'ls'

def lsdetail():
    ls('-lah')

def cd(path):
    os.chdir(path)
    print('$'+str(os.getcwd()))

@bash
def md(args):
    return 'mkdir {args}'.format(args=args)

