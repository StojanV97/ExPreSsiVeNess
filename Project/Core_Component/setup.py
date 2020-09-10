from setuptools import setup, find_packages
setup(
    name="Core_Component",
    version="0.1",
    packages=find_packages(),
    install_requires=['Django>=3.0.2'],

    package_data={'Core_Component': ['Templates/*.html']},
    zip_safe=False
)
