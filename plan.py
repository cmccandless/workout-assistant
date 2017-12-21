# from tinydb import Query


def add(db, opts):
    print('adding plan', opts.name)


def list(db, opts):
    print('listing plans')


def details(db, opts):
    print('showing details for plan', opts.name)


def stats(db, opts):
    print('showing stats for plan', opts.name)


def edit(db, opts):
    print('editing plan', opts.name)


def remove(db, opts):
    print('removing plan', opts.name)


def run(db, opts):
    print('running plan', opts.name)
