from setuptools import setup, find_packages

setup(
    name='wx-data-explorer',
    version='0.1',
    packages=find_packages(),
    url='http://myproject.com',
    license='MIT',
    author='Bob Seaton',
    author_email='rwseaton@ncsu.edu',
    description='A short description of your project',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'wxPython',
        'matplotlib',
        # Other dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)

