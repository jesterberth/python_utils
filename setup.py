import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_utils",
    version="0.0.1",
    author="Jesterberth",
    author_email="estermann@outlook.com",
    description="personal collection of python utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jesterberth/python_utils",
    project_urls={"Bug Tracker": "https://github.com/jesterberth/python_utils/issues"},
    license="MIT",
    packages=["python_utils"],
    install_requires=[],
)
