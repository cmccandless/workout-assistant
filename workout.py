#!/usr/bin/env python
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from tinydb import TinyDB
import buddy
import plan

NAME_NEEDED = [ArgumentParser(
    formatter_class=ArgumentDefaultsHelpFormatter,
    add_help=False
)]
NAME_NEEDED[0].add_argument('name')

main_parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
main_commands = main_parser.add_subparsers()

# Global Arguments
main_parser.add_argument('--db', default='db.json', help='database file path')

# Commands
# buddy {(a|add), (ls|list), (s|stats), (rm|remove)}
buddy_parser = main_commands.add_parser('buddy', aliases=['b'])
buddy_commands = buddy_parser.add_subparsers()

buddy_add_parser = buddy_commands.add_parser(
    'add', aliases=['a'], parents=NAME_NEEDED
)
buddy_add_parser.set_defaults(func=buddy.add)

buddy_list_parser = buddy_commands.add_parser('list', aliases=['ls'])
buddy_list_parser.set_defaults(func=buddy.list)

buddy_stats_parser = buddy_commands.add_parser(
    'stats', aliases=['s'], parents=NAME_NEEDED
)
buddy_stats_parser.set_defaults(func=buddy.stats)

buddy_remove_parser = buddy_commands.add_parser(
    'remove', aliases=['rm'], parents=NAME_NEEDED
)
buddy_remove_parser.set_defaults(func=buddy.remove)

# plan {(a|add), (ls|list), (d|details), (s|stats), (e|edit), (rm|remove), run}
plan_parser = main_commands.add_parser('plan', aliases=['p'])
plan_commands = plan_parser.add_subparsers()

plan_add_parser = plan_commands.add_parser(
    'add', aliases=['a'], parents=NAME_NEEDED
)
plan_add_parser.set_defaults(func=plan.add)

plan_list_parser = plan_commands.add_parser('list', aliases=['ls'])
plan_list_parser.set_defaults(func=plan.list)

plan_details_parser = plan_commands.add_parser(
    'details', aliases=['d'], parents=NAME_NEEDED
)
plan_details_parser.set_defaults(func=plan.details)

plan_stats_parser = plan_commands.add_parser(
    'stats', aliases=['s'], parents=NAME_NEEDED
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
plan_run_parser.add_argument('buddies', nargs='+')


if __name__ == '__main__':
    opts = main_parser.parse_args()
    db = TinyDB(opts.db)
    opts.func(db, opts)
