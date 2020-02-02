import argparse
from phlasch.runners import run
from phlasch.migrators import revision, upgrade, downgrade


def main():
    # create command parser
    parser = argparse.ArgumentParser(
        'phlasch',
        description='a url shortener app/lib.',
    )

    # make command subparsers
    subparsers = parser.add_subparsers(
        title='action',
        description='the action to take.',
        dest='action',
        required=True,
    )

    # run subparser
    run_parser = subparsers.add_parser(
        'run',
        description='run app.',
        help='run app',
    )
    run_parser.add_argument(
        'app', type=str,
        help='the app to run',
    )

    # revision subparser
    revision_parser = subparsers.add_parser(
        'revision',
        description='make revision.',
        help='make revision',
    )
    revision_parser.add_argument(
        'app', type=str,
        help='the app to make the revision for',
    )
    revision_parser.add_argument(
        'message', type=str,
        help='the revision message',
    )

    # upgrade subparser
    upgrade_parser = subparsers.add_parser(
        'upgrade',
        description='upgrade to revision.',
        help='upgrade to revision',
    )
    upgrade_parser.add_argument(
        'app', type=str,
        help='the app to upgrade',
    )
    upgrade_parser.add_argument(
        'rev', type=str,
        help='the rev to upgrade to',
    )

    # downgrade subparser
    downgrade_parser = subparsers.add_parser(
        'downgrade',
        description='downgrade to revision.',
        help='downgrade to revision',
    )
    downgrade_parser.add_argument(
        'app', type=str,
        help='the app to downgrade',
    )
    downgrade_parser.add_argument(
        'rev', type=str,
        help='the rev to downgrade to',
    )

    # parse args
    args = parser.parse_args()

    if args.action == 'run':
        run(args.app)
    elif args.action == 'revision':
        revision(args.app, args.message)
    elif args.action == 'upgrade':
        upgrade(args.app, args.rev)
    elif args.action == 'downgrade':
        upgrade(args.app, args.rev)


if __name__ == '__main__':
    main()
