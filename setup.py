from setuptools import setup, version

setup(
    name='cli_framework',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points='''
    [console_scripts]
    super=cli_framework:cli_framework
    '''
    )
