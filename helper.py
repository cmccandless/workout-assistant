from datetime import datetime


def conv_date(dict_obj):
    dict_obj = dict(dict_obj)
    if 'date' in dict_obj:
        dict_obj['date'] = datetime.strptime(
            dict_obj['date'], '%Y-%m-%d %H:%M:%S.%f'
        )
    return dict_obj


def confirm(prompt='Are you sure?'):
    return input(prompt + ' [yes/no]>').lower().startswith('y')


def str_type(x):
    return x.format()


def enter_field(name, default='', indent=2, type=None):
    while True:
        value = input('{}{} [{}]: '.format(''.ljust(indent), name, default))
        if not value:
            raise EOFError()
        if type is not None:
            try:
                type(value)
            except Exception as e:
                print(str(e))
                continue
        return value


def choice(choices=['yes', 'no'], prompt_text=None):
    if any(ch is None for ch in choices):
        raise ValueError('choice cannot be None')
    prompt = '[{}]>'.format('/'.join(choices))
    if prompt_text is not None:
        prompt = prompt_text + ' ' + prompt
    value = None
    while True:
        value = input(prompt)
        if value in choices:
            return value
        print('invalid option')
