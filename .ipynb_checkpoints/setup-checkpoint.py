from setuptools import setup, find_packages

setup(
    name='acolite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'argparse',
        'matplotlib',
        'osgeo',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'acolite-launch=acolite_wrapper:launch_acolite',
        ],
    },
)