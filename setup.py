try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as f:
    readme = f.read()

setup(
    name='jiofi',
    include_package_data=True,
    packages=['jiofi',],
    license='MIT',
    python_requires='>=3.6.0',
    install_requires= ['requests','fire', 'rich'],
    entry_points = {"console_scripts": ['jiofi = jiofi.jiofi:main']},
    url="https://github.com/athul/jiofi-cli",
    author="Athul Cyriac Ajay",
    author_email="athul8720@gmail.com",
    description="A Command Line Interface to get stats about your Jiofi.",
    long_description=readme,
    version='0.1.3',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6'
    ],
    long_description_content_type='text/markdown',
)