from distutils.core import setup
setup(
    name = 'icalevents',
    packages = ['icalevents'],
    version = '0.0.1',
    description = 'iCal downloader and parser',
    author = 'Thomas Irgang',
    author_email = 'thomas@irgang-la.de',
    url = 'https://github.com/irgangla/icalevents',
    download_url = 'https://github.com/irgangla/icalevents/archive/v0.0.1.tar.gz',
    keywords = ['iCal'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    long_description = """\
iCal download, parse and query tool
-------------------------------------

Supports downloading of iCal URL or loading of iCal files, parsing the content and finding events occurring in a given
time range.

See: icalevents.icalevents.events(url=None, file=None, start=None, end=None, fix_apple=False)

This version requires Python 3 or later.
"""
)