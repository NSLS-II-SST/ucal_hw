from setuptools import setup, find_packages

setup(
    author="Charles Titus",
    author_email="charles.titus@nist.gov",
    install_requires=["bluesky", "ophyd", "numpy", "scipy", "sst_base", "sst_funcs"],
    name="ucal_hw",
    use_scm_version=True,
    packages=find_packages()
)
