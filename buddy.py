from tinydb import Query
import helper


def add(opts):
    buddies = opts.db.table('buddies')
    buddies.insert(dict(name=opts.name))


def ls(opts):
    buddies = opts.db.table('buddies')
    if buddies:
        for buddy in buddies:
            print(buddy['name'])
            yield buddy['name']
    else:
        print('No workout buddies')


def __workouts__(opts):
    if opts.db.table('buddies').search(Query().name == opts.name):
        return opts.db.table('workouts').search(Query().buddy == opts.name)
    else:
        raise KeyError('unknown workout buddy: ' + opts.name)


def log(opts):
    try:
        workouts = __workouts__(opts)
        if workouts:
            for workout in workouts:
                workout_str = '{date}: {plan}'.format(**workout)
                print(workout_str)
                yield workout_str
        else:
            print('No workouts for', opts.name)
    except KeyError as e:
        print(str(e))


def stats(opts):
    try:
        workouts = list(map(helper.conv_date, __workouts__(opts)))
        if workouts:
            print('TODO: calculate stats for buddy', opts.name)
        else:
            print('No workouts for', opts.name)
    except KeyError as e:
        print(str(e))


def remove(opts):
    prompt = (
        'Are you sure you want to permanently ' +
        'delete workout buddy "{}"?'.format(opts.name)
    )
    if helper.confirm(prompt):
        buddies = opts.db.table('buddies')
        buddies.remove(Query().name == opts.name)
        workouts = opts.db.table('workouts')
        workouts.remove(Query().buddy == opts.name)
