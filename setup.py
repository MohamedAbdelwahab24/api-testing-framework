from setuptools import setup, find_packages

setup(
    name="api-testing-framework",
    version="1.0.0",
    author="Mohamed Abdelwahab",
    description="Automated API testing framework with contract testing",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.11",
)
