from setuptools import setup, find_packages

setup(
    name="crawler",  # Use 'crawler' as the package name
    version="0.1.0",  # Package version
    description="A Python tool for crawling and finding files based on various criteria.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Muhammad Sohaib Hassan",
    author_email="muhammadsohaibhassan3@gmail.com",
    url="https://github.com/MuhammadSohaibHassan/crawler",  # Your GitHub repo URL
    packages=find_packages(),  # Automatically find packages (optional)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Choose a license (e.g., MIT)
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "crawler=crawler:main",  # Ensure 'crawler' is the command
        ],
    },
)
