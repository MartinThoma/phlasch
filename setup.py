import setuptools
from os import getenv


with open('./.github/README.md', 'r') as fh:
    long_description = fh.read()


install_requires = [
    'aiohttp[speedups]',
    'aiohttp-swagger[performance]',
    'aiopg[sa]',
    'alembic',
    'gunicorn',
]


setuptools.setup(
    name='phlasch-server',
    version=getenv('TRAVIS_TAG', '0.0.0'),
    description='a url shortener app/lib.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bbmokhtari/phlasch-server',
    author='Behzad B. Mokhtari',
    author_email='behzad.public@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet',
    ],
    keywords=' '.join(['url-shortener', 'url-shortener-microservice']),
    project_urls={
        'Documentation': 'https://github.com/bbmokhtari/phlasch-server',
        'Source': 'https://github.com/bbmokhtari/phlasch-server',
        'Tracker': 'https://github.com/bbmokhtari/phlasch-server/issues',
    },
    packages=setuptools.find_packages(
        exclude=[
            'tests',
        ],
    ),
    package_data={
        "phlasch": [
            "alembic.ini",
            "*/migrations/*",
            "*/migrations/versions/*",
            "*/swagger/*",
        ],
    },
    install_requires=install_requires,
    python_requires='>=3.7, <4',
)
