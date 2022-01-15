import setuptools

with open("README.md", "r") as fh:
long_description = fh.read()

setuptools.setup(
   name="diceroller",
   version="1",
   author="Nicolas Concha",
   author_email="niccy266@hotmail.com",
   description="A simple, interactive dice roller",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="google.com",
   packages=setuptools.find_packages(),
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
)
