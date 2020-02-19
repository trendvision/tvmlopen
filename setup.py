import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='tvml',
     version='0.1',
     scripts=['tvml'],
     author="Pazlvbanke",
     author_email="pazlvbanke@yandex.ru",
     description="Uhaha",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/trendvision/tvml",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
