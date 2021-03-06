""" Setup configuration for is_cropped command. """

from setuptools import setup

DESC = "Determine if one image is a cropped version of another."

setup(
    name='is_cropped',
    version='0.1',
    description=DESC,
    url='http://github.com/shinsons/waldo-shinsons',
    author='Nathen Hinson',
    author_email='nathen.hinson@gmail.com',
    test_suite='tests',
    packages=['main'],
    scripts=['bin/is_cropped'],
    zip_safe=False
)

