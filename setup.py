from setuptools import setup, find_packages


setup(
    name="quotesapi",
    version="0.1.0",
    install_requires=[
        "databases==0.2.6",
        "fastapi==0.44.0",
        "migri==0.5.0",
        "uvicorn==0.10.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.8",
)
