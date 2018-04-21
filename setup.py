from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='awwsbase',
    version='0.0.1',
    description='Common AWS code',
    long_description=readme,
    author='Mark McClain',
    author_email='mjm461@gmail.com',
    url='https://github.com/mjm461/awsbase',
    license=license,
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires = [
        #'boto3' # AWS containers already include the latest version - add manually if you want it
    ]
)
