import os

def deco(f):
        def deco_wrapper(*args, **kwargs):
            print('wrapper :' + str(*args))
            return os.system(f(*args, **kwargs))
        return deco_wrapper

@deco
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

@deco
def md(args):
    return 'mkdir {args}'.format(args=args)

def tree():
    os.sysmte('tree')
