# setup.py

from setuptools import setup, find_packages

setup(
    name="task-manager",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "task-manager = task_manager.cli:main"
        ]
    },
    install_requires=[
        "argparse"  # You can add more dependencies here
    ],
    description="Simple Task Manager CLI",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/task-manager",
)

