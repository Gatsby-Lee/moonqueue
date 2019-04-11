from setuptools import setup, find_packages

requires = [
    'redis',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
]

setup(
    name='moonqueue',
    version='0.2.1',
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
    extras_require={
        'testing': tests_require,
    },
)
