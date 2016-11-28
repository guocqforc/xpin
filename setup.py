from setuptools import setup, find_packages

setup(
    name="xpin",
    version='0.1.5',
    zip_safe=False,
    platforms='any',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    scripts=['xpin/bin/xpin'],
    install_requires=['requests', 'flask', 'flask_sqlalchemy', 'flask_admin', 'passlib'],
    url="https://github.com/dantezhu/xpin",
    license="BSD",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="pin create/verify",
)
