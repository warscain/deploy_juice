from distutils.core import setup
import sys


__version__ = 0.1

kw = dict(
    name = 'deploy_juice',
    version = __version__,
    description = 'Sync services change and deploy services',
    long_description = open('D:\pycharm_win\deploy_juice\README.md', 'r').read(),
    author = 'Zhimou Peng',
    author_email = 'warscain@gmail.com',
    url = 'https://github.com/warscain/deploy_juice',
    download_url = 'https://github.com/warscain/deploy_juice',
    # py_modules = [''],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ])

if sys.version_info[1]==5:
    kw['install_requires'] = ['simplejson']

setup(**kw)
