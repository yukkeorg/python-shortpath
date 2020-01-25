from setuptools import setup, find_packages

setup(
    name="shortpath",
    version="0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
