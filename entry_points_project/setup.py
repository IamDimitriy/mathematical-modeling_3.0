from setuptools import setup

setup(
    name="mathematical-modeling",
    version="0.1.0",
    packages=["mathematical-modeling"],
    entry_points={
        "gui_scripts": [
            "mathematical-modeling = mathematical-modeling.__main__:main"
        ]
    },
)
