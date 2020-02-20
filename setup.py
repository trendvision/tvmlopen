import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='tvml',
     version='0.1.6',
     packages=['tvml'],
     author="Pazlvbanke",
     author_email="pazlvbanke@yandex.ru",
     description="Package for everything",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/trendvision/tvmlopen",
     # packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
