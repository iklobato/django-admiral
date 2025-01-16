from setuptools import setup, find_packages

def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='django-admiral',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    license='MIT',
    description='A comprehensive testing framework for Django Admin interfaces using Selenium',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/iklobato/django-admiral',
    author='iklobato',
    author_email='iklobato@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Django>=3.2',
        'selenium>=4.0.0',
        'webdriver_manager>=3.8.0',
    ],
    extras_require={
        'test': [
            'pytest>=7.0.0',
            'pytest-django>=4.5.0',
            'pytest-cov>=4.0.0',
            'factory-boy>=3.2.0',
            'pytest-selenium>=4.0.0',
        ],
        'dev': [
            'black>=23.0.0',
            'isort>=5.10.0',
            'flake8>=6.0.0',
            'mypy>=1.0.0',
            'pre-commit>=3.0.0',
        ],
        'docs': [
            'sphinx>=6.0.0',
            'sphinx-rtd-theme>=1.2.0',
            'myst-parser>=1.0.0',
        ],
    },
    project_urls={
        'Bug Tracker': 'https://github.com/iklobato/django-admiral/issues',
        'Documentation': 'https://django-admiral.readthedocs.io/',
        'Source Code': 'https://github.com/iklobato/django-admiral',
    },
    entry_points={
        'console_scripts': [
            'admiral=django_admiral.cli:main',
        ],
    },
    zip_safe=False,
    platforms='any',
)
