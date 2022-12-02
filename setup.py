from setuptools import setup, find_packages


setup(
    name="gameflip-api",
    version="0.0.1",
    author="gustavopedrosob",
    author_email="thevicio27@gmail.com",
    description="A Python Rocket League Gameflip API",
    url="https://github.com/gustavopedrosob/Gameflip-Api",
    project_urls={
        "Bug Tracker": "https://github.com/gustavopedrosob/Gameflip-Api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6"
)
