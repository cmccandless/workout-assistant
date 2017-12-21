from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import plan
import buddy
import shlex
from tinydb import TinyDB


def read_command():
    args = shlex.split(input('>'))
    return shell_main_parser.parse_known_args(args)


def shell(opts):
    db = opts.db
    while True:
        opts, args = read_command()
        try:
            if opts.command in ['exit', 'quit', 'q']:
                return
            elif opts.command in ['help', 'h', '?']:
                if args:
                    args += ['-h']
                    opts, args = shell_main_parser.parse_known_args(args)
                else:
                    print(shell_main_parser.format_help())
                    continue
            if opts.command in ['buddy', 'b']:
                opts = buddy_parser.parse_args(args)
                setattr(opts, 'db', db)
                opts.func(opts)
            elif opts.command in ['plan', 'p']:
                opts = plan_parser.parse_args(args)
                setattr(opts, 'db', db)
                opts.func(opts)
        except SystemExit:
            pass


class BaseParser(ArgumentParser):
    def __init__(self, **kwargs):
        ArgumentParser.__init__(
            self, formatter_class=ArgumentDefaultsHelpFormatter, **kwargs
        )


NAME_NEEDED = [BaseParser(add_help=False)]
NAME_NEEDED[0].add_argument('name')

main_parser = BaseParser()
main_commands = main_parser.add_subparsers()

# Global Arguments
main_parser.add_argument(
    '--db', default='db.json', help='database file path', type=TinyDB
)

# Commands {
# (b|buddy)
# }
# buddy {
# (a|add) name
# (ls|list)
# (s|stats) name
# (rm|remove) name
# }
buddy_parser = main_commands.add_parser('buddy', aliases=['b'])
buddy_commands = buddy_parser.add_subparsers()

buddy_add_parser = buddy_commands.add_parser(
    'add', aliases=['a'], parents=NAME_NEEDED
)
buddy_add_parser.set_defaults(func=buddy.add)

buddy_list_parser = buddy_commands.add_parser('list', aliases=['ls'])
buddy_list_parser.set_defaults(func=buddy.ls)

buddy_stats_parser = buddy_commands.add_parser(
    'stats', aliases=['st'], parents=NAME_NEEDED
)
buddy_stats_parser.set_defaults(func=buddy.stats)

buddy_remove_parser = buddy_commands.add_parser(
    'remove', aliases=['rm'], parents=NAME_NEEDED
)
buddy_remove_parser.set_defaults(func=buddy.remove)

buddy_log_parser = buddy_commands.add_parser(
    'log', aliases=['l'], parents=NAME_NEEDED
)
buddy_log_parser.set_defaults(func=buddy.log)

# plan {
# (a|add) name
# (ls|list)
# (d|details) name
# (s|stats) name
# (e|edit) name
# (rm|remove) name
# run name buddy [buddy ...]
# }
plan_parser = main_commands.add_parser('plan', aliases=['p'])
plan_commands = plan_parser.add_subparsers()

plan_add_parser = plan_commands.add_parser(
    'add', aliases=['a'], parents=NAME_NEEDED
)
plan_add_parser.set_defaults(func=plan.add)

plan_list_parser = plan_commands.add_parser('list', aliases=['ls'])
plan_list_parser.set_defaults(func=plan.ls)

plan_details_parser = plan_commands.add_parser(
    'details', aliases=['d'], parents=NAME_NEEDED
)
plan_details_parser.set_defaults(func=plan.details)

plan_stats_parser = plan_commands.add_parser(
    'stats', aliases=['st'], parents=NAME_NEEDED
)
plan_stats_parser.set_defaults(func=plan.stats)

plan_edit_parser = plan_commands.add_parser(
    'edit', aliases=['e'], parents=NAME_NEEDED
)
plan_edit_parser.set_defaults(func=plan.edit)

plan_remove_parser = plan_commands.add_parser(
    'remove', aliases=['rm'], parents=NAME_NEEDED
)
plan_remove_parser.set_defaults(func=plan.remove)

plan_run_parser = plan_commands.add_parser('run', parents=NAME_NEEDED)
plan_run_parser.set_defaults(func=plan.run)
plan_run_parser.add_argument('buddy', nargs='+')


# shell
shell_parser = main_commands.add_parser('shell', aliases=['sh'])
shell_parser.set_defaults(func=shell)

shell_main_parser = BaseParser(add_help=False)
shell_main_parser.add_argument(
    'command',
    choices=[
        'help', 'h', '?',
        'buddy', 'b',
        'plan', 'p',
        'exit', 'q', 'quit'
    ]
)
