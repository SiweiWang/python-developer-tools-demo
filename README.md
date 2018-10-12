
# Python developer tools

## Setup tools
An sample project to show how to package a python project as module :shipit:

### Package the project to module
    python setup.py sdist

There will be a new package created under `dist` directory.

### Distribute the package
The package can be distributed via Python Packaging Authority(PyPA).

    python setup.py register
    python setup.py upload

### Install the package locally
This project is just a sample and will Not meet the requirement for publish. We can install the package locally using:

    pip install dist/pets-0.1.tar.gz