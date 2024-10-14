from setuptools import setup, find_packages

setup(
    name="python-hsl-player",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "aiohttp==3.8.4",
        "PyQt6==6.5.0",
        "av==10.0.0", 
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-asyncio",
        ],
    },
    entry_points={
        "console_scripts": [
            "hsl-player=main:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="An open-source HSL (HTTP Live Streaming) media player built with Python and PyQt6",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-hsl-player",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)