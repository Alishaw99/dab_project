from setuptools import setup, find_packages

setup(
    name="dab-project",
    version="0.1",
    description="This contain  the code in the ./src directory",
    author="Tariq Shah",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
    entry_points={
        "packages": [
            "main=dab_project.main:main",
        ]
    },
)
