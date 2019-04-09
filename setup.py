from setuptools import setup, find_packages

requires = [
    'redis',
]


setup(
    name='moonqueue',
    version='0.1.2',
    description='Queue Implementation with Redis',
    long_description=open('README.rst').read(),
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.6',
    ],
    author='Gatsby Lee',
    url='https://github.com/Gatsby-Lee/moonqueue',
    keywords='gatsby redis queue',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
