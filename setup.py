#!/usr/bin/env python3

"""Setuptools setup file."""

import setuptools

console_scripts = [
    "gif-to-video = gif_to_video.gif_to_video:main"]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GifToVideo",
    version="0.1.0",
    author="Drakovek",
    author_email="DrakovekMail@gmail.com",
    description="An application that converts animated .GIF files into videos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Drakovek/GifToVideo",
    packages=setuptools.find_packages(),
    install_requires=["python-ffmpeg", "pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.0',
    entry_points={"console_scripts": console_scripts}
)
