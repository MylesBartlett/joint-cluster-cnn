from setuptools import find_packages, setup

setup(
    name="jule",
    version="0.1.0",
    author="",
    packages=find_packages(),
    description="TF-based unofficial implementation of JULE",
    python_requires=">=3.6",
    package_data={"dataset": ["py.typed"]},
    install_requires=[
        "tensorflow=1.15",
        "numpy",
        "scikit-learn",
    ],
)
