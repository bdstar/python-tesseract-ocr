from setuptools import setup, find_packages

setup(
    name='tesseract',
    version='0.1',
    description='Python bindings for Tesseract',
    long_description=open('README').read(),
    author='Aidan Lister',
    author_email='aidan@php.net',
    url='http://github.com/aidanlister/python-tesseract',
    license='MPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
