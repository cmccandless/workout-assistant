# from tinydb import Query


def add(db, opts):
    print('adding buddy', opts.name)


def list(db, opts):
    print('listing buddies')


def stats(db, opts):
    print('printing stats for buddy', opts.name)


def remove(db, opts):
    print('removing buddy', opts.name)
