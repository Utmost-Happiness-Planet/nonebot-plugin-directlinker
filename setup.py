from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nonebot-plugin-directlinker",
    version="2.3.1",
    author="uhpteam",
    description="A plugin based on NoneBot2 to extract direct links of files in qq group.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Utmost-Happiness-Planet/nonebot-plugin-directlinker",
    project_urls={
        "Bug Tracker": "https://github.com/Utmost-Happiness-Planet/nonebot-plugin-directlinker/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    packages=["nonebot_plugin_directlinker"],
    python_requires=">=3.7",
    install_requires=[
        "nonebot2 >= 2.0.0b2",
        "nonebot-adapter-onebot >= 2.0.0b1"
    ],
)
