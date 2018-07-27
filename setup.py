from setuptools import setup, find_packages

setup(
    name='baby_cry_api',
    version='0.0.1',
    description='',
    # url="https://github.com/giulbia/baby_cry_api.git",
    author='Giulia Bianchi',
    author_email="gbianchi@xebia.fr",
    license='new BSD',
    packages=find_packages(),
    install_requires=['flask'],
    tests_require=['pytest'],
    scripts=[],
    py_modules=["baby_cry_api"],
    # include_package_data=True,
    # zip_safe=False
)
