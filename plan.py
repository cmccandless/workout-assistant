from tinydb import Query
from datetime import datetime
import helper


EXERCISE_FIELDS = {
    'name': helper.str_type,
    'type': lambda x: {'reps': 'reps', 'seconds': 'seconds'}[x],
    'value': int
}


def __edit_exercise__(exercise):
    return {
        k: helper.enter_field(k, exercise[k], type=t)
        for k, t in EXERCISE_FIELDS
    }


def __get_plan__(opts):
    plan = opts.db.table('plans').get(opts.name)
    if not plan:
        raise KeyError('unknown plan "{}"'.format(opts.name))
    return plan


def __edit_plan__(opts, **defaults):
    def keep_exercise(exercise):
        return 'yes' == helper.choice(
            prompt_text=''
        )
    updated = {'name': opts.name}
    updated['focus'] = helper.enter_field('focus', type=helper.str_type)
    exercises = [
        __edit_exercise__(ex)
        for ex in defaults.get('exercises', [])
        if keep_exercise(ex)
    ]
    while True:
        another = helper.choice()
        if another == 'no':
            break
        exercise = {
            k: helper.enter_field(k, defaults.get(k), t)
            for k, t in EXERCISE_FIELDS.items()
        }
        exercises.append(exercise)
    updated['exercises'] = exercises
    opts.db.table('plans').update(updated, Query().name == opts.name)


def __run_plan__(opts):
    plan = __get_plan__(opts)
    for exercise in plan['exercises']:
        pass


def add(opts, **kwargs):
    plans = opts.db.table('plans')
    plan = {
        'name': opts.name
    }
    plans.insert(plan)
    __edit_plan__(opts, **plan, **kwargs)


def ls(opts):
    plans = opts.db.table('plans')
    if plans:
        for plan in plans:
            plan_str = '{name} ({focus})'.format(**plan)
            print(plan_str)
            yield plan_str


def details(opts):
    try:
        plan = __get_plan__(opts)
        print('focus:', plan.focus)
        print('exercises:')
        for exercise in plan['exercises']:
            print('  {name} for {value} {type}'.format(**exercise))
    except KeyError as e:
        print(str(e))


def stats(opts):
    workouts = list(map(
        helper.conv_date,
        opts.db.table('workouts').search(Query().plan == opts.name)
    ))
    if workouts:
        print('showing stats for plan', opts.name)
    else:
        print('No workouts recorded for plan')


def edit(opts):
    try:
        plan = __get_plan__(opts)
        __edit_plan__(opts, **plan)
    except KeyError as e:
        print(str(e))


def remove(opts):
    try:
        __get_plan__(opts)
        if helper.confirm():
            plans = opts.db.table('plans')
            plans.remove(Query().name == opts.name)
    except KeyError as e:
        print(str(e))


def run(opts):
    try:
        __run_plan__(opts)
        workouts = opts.db.table('workouts')
        for buddy in opts.buddy:
            buddies = opts.db.table('buddies')
            if not buddies.search(Query().name == buddy):
                buddies.insert({'name': buddy})
            workouts.insert({
                'date': str(datetime.now()),
                'buddy': buddy,
                'plan': opts.name
            })
    except KeyError as e:
        print(str(e))
