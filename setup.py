from setuptools import setup

REQUIREMENTS = [
    'docutils',
    'pymongo',
    'simplejson',
    'argcomplete',
]

setup(
    name='golismero',
    long_description_content_type="text/markdown",
    packages=['golismero',],
    py_modules=['golismero'],
    entry_points = {
        'console_scripts': [
            'golismero=golismero:main']
    },
    install_requires=REQUIREMENTS,
)