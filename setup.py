from setuptools import setup

setup(
    name="JumboMana-Chess-Game",
    version="1.0",
    description="Something different",
    author="Florian",
    install_requires=[
        "fastapi",
        "chess",
        "setuptools",
        "uvicorn",
        "jinja2",
        "pytest",
    ],  # external packages acting as dependencies
)
