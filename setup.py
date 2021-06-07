from setuptools import setup, find_packages

REQUIREMENTS = [
    'docutils',
    'pymongo',
    'simplejson',
    'argcomplete',
]

setup(
    name='golismero',
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=['golismero'],
    entry_points = {
        'console_scripts': [
            'golismero=golismero:main']
    },
    install_requires=REQUIREMENTS,
)