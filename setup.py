from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
#import asciify
import sys


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


with open('README.rst') as reader:
    readme = reader.read()

setup(
    name='asciify',
    version='0.0.1',
    description='Image to ascii API',
    long_description=readme,
    author='John Curran',
    author_email='curran736@gmail.com',
    url='',
    license='MIT License',
    #packages=find_packages(exclude=('tests')) + ['asciify'],
    packages=['asciify'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    install_requires=[],
    classifiers=(
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ),
)
