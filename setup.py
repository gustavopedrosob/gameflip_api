from setuptools import setup


setup(
    name="rocket-league-gameflip-api",
    version="0.0.3",
    author="gustavopedrosob",
    author_email="thevicio27@gmail.com",
    description="A Python Rocket League Gameflip API",
    url="https://github.com/gustavopedrosob/gameflip_api",
    project_urls={
        "Bug Tracker": "https://github.com/gustavopedrosob/gameflip_api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=["rocket_league_gameflip_api"],
    install_requires=["requests", "unidecode", "git+https://github.com/gustavopedrosob/rocket_league_utils"],
    python_requires=">=3.6"
)
