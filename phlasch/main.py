from aiohttp.web import Application, run_app
from phlasch.core.configure import configure as configure_core


def main():
    app = Application()
    configure_core(app)
    run_app(app)


if __name__ == '__main__':
    main()
