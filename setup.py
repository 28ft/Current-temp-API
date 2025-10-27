import setuptools

with open("README.md", "r", encoding= "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name= "current_temp_api",
    version= "0.0.1",
    author= "fatemeh taklifi",
    author_email= "fatemetaklifi@gmail.com",
    description= "a simple client api module to get current temperature from service providers",
    long_description= long_description,
    url= "https://github.com/28ft/Current-temp-API.git",
    classifiers= [
        "Programming Language :: Python :: 3.13",
        "license :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires= [
        "requests",
    ],
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where="src"),
    python_requires= ">=3.6"
)