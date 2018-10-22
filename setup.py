""" Setup script
"""

from setuptools import setup

setup(
    name='urdf_parser',
    version='0.1',
    author='Andrew Berger',
    author_email='andrew@dexai.com',
    description='Standalone Python URDF parser as native Python package',
    url='https://github.com/DexaiRobotics/urdf_parser',
    packages=['urdf_parser'],
    python_requires='>=2.7',  # TODO: not sure if this is true
    install_requires=[
        'pyyaml',
        'lxml'
    ],
)
