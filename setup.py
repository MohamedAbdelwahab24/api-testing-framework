from setuptools import setup

setup(
    name="api-testing-framework",
    version="1.0.0",
    author="Mohamed Abdelwahab",
    description="Automated API testing framework with contract testing",
    py_modules=["api_tester"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.11",
    install_requires=["requests>=2.31.0"],
)
