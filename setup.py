from setuptools import setup, find_packages

setup(
    name = "afed_donations",
    version = "1.0",
    url = 'http://github.com/steveandroulakis/afed_donations',
    license = 'BSD',
    description = "Tool for viewing donations to Australian political parties",
    author = 'Steve Androulakis',
    packages = find_packages(),
    install_requires = ['setuptools',
                        'django==1.4.3',
                        'south==0.7.6'],
)
