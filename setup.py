from setuptools import setup, find_packages

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
    
setup(
    name = 'cli-tool',
    description = 'cli tool',
    packages = find_packages(),
    py_modules=['cli_tool'],
    author = 'Sandra',
    entry_points="""
                [console_scripts]
                cli-tool=cli_tool:main
                """,


    install_requires = [requirements],
    version = '0.0.1',  
)