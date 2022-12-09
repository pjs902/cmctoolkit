from setuptools import find_packages, setup  # pragma: no cover

setup(  # pragma: no cover
    name="cmctoolkit",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    version="0.1.0",
    include_package_data=True,
    # package_data={"cmctoolkit": ["resources/*.dat"]},
)
