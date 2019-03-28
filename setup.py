# coding=utf-8

from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='vasptools',
        version="0.2.1",
        description=(
            'tool collection for parsing vasp inputs & outputs'
        ),
        long_description=open('README.md').read(),
        author='Sky Zhang',
        author_email='sky.atomse@gmail.com',
        maintainer='Sky Zhang',
        maintainer_email='sky.atomse@gmail.com',
        license='MIT License',
        packages=find_packages(),
        platforms=["Linux", "Darwin"],
        url='https://github.com/atomse/vasptools',
        python_requires='>=3',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Operating System :: Linux/OSX',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
        install_requires=[
            'sh>=1.10.0',
        ],
        entry_points={
            "console_scripts": [
                "vasptools=vasptools.cli:run_vasptools_cli",
            ],
        },
        extras_require={
            'docs': [
                'sphinx',
                'sphinxcontrib-programoutput',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest>=4.0',
                'pytest-cov'
            ],
            'curate': [
                'graphviz'
            ],
        },
        zip_safe=True,
    )
