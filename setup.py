from setuptools import setup, find_packages


with open('README.md', 'r', encoding='utf8') as readme_file:
    readme = readme_file.read()

requirements = ['flask==1.1.4']

setup(
    name='flask_fixture',
    version='0.0.1',
    author='Evgeniy Blinov',
    author_email='zheni-b@yandex.ru',
    description='Start and stop the flask server for your tests',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/pomponchik/flask_fixture',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements,
    entry_points={
        "pytest11": ["flask_fixture = flask_fixture"],
    },
    classifiers=[
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',
        'Framework :: Pytest',
    ],
)
