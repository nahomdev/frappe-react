from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')
    
setup(
    name='nah',
    version='1.0.0',
    description='next js spa generator for frappe framework',
    author='nahom balcha',
    author_email='nahomdev2021@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True
)