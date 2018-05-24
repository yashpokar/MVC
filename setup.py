from setuptools import setup, find_packages

setup(
    name='mvc',
    description='A high-level web framework.',
    version='0.0.1',
    install_requires=[
        'Werkzeug',
        'Jinja2',
    ],
    packages=find_packages(),
)
