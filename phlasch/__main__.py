import argparse
from phlasch.runners import run
from phlasch.migrators import makemigrations, migrate


def main():
    # create command parser
    parser = argparse.ArgumentParser(
        'phlasch',
        description='a url shortener app/lib.',
    )

    # make command subparsers
    subparsers = parser.add_subparsers(
        title='actions',
        description='the actions that can be taken.',
        dest='action',
        required=True,
    )

    # run subparser
    subparsers.add_parser(
        'run',
        description='run all apps.',
        help='run all apps',
    )

    # makemigrations subparser
    makemigrations_parser = subparsers.add_parser(
        'makemigrations',
        description='make migrations.',
        help='make migrations',
    )
    makemigrations_parser.add_argument(
        'app', type=str,
        help='the app to make the migrations for',
    )
    makemigrations_parser.add_argument(
        'message', type=str,
        help='the migration message',
    )

    # migrate subparser
    migrate_parser = subparsers.add_parser(
        'migrate',
        description='migrate.',
        help='migrate',
    )
    migrate_parser.add_argument(
        'app', type=str,
        help='the app to migrate',
    )

    # parse args
    args = parser.parse_args()

    if args.action == 'run':
        run()
    elif args.action == 'makemigrations':
        makemigrations(args.app, args.message)
    elif args.action == 'migrate':
        migrate(args.app)


if __name__ == '__main__':
    main()
