from setuptools import setup, find_packages

setup(
    name='dunefetch',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['windows-curses; platform_system == "Windows"','psutil'],
    entry_points={
        'console_scripts': [
            'dunefetch = dunefetch.main:run'
        ]
    },
    author='datavorous',
    description='neofetch + falling sand engine for your terminal.',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    url='https://github.com/datavorous/dunefetch',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
