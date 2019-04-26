import os

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

this = os.path.dirname(os.path.realpath(__file__))

def read(name):
    with open(os.path.join(this, name)) as f:
        return f.read()
setup(
    name='pyydl',
    version='1.0',
    description='description',
    long_description=readme,
    author='Gabriel Alves',
    author_email='gabrieltots@gmail.com',
    url='https://github.com/gsevla/pyYDL',
    packages=['my_src'],
    install_requires=read('requirements.txt'),
    include_package_data=True,
    zip_safe=True,
    license='MIT',
    keywords='example app snap linux ubuntu',
    classifiers=[
        'Development Status :: 5 - Production/devel',
        'Intended Audience :: Developers',
        'Natural Language :: English'
    ],
    scripts=['bin/pyydl']
)