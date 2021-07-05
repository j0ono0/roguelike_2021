import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roguelike_2021_J0ono0",
    version="0.0.1",
    author="John Newall",
    author_email="john@johnnewall.com",
    description="A roguelike game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/j0ono0/roguelike_2021",

    package_dir={"": "roguelike_2021"},
    packages=setuptools.find_packages(where="roguelike_2021"),
    python_requires=">=3.6",
)
