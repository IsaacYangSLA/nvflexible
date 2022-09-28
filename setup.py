import os
import shutil
from datetime import datetime

from setuptools import find_packages, setup

import versioneer
# read the contents of your README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

package_name = "nvflexible"

setup(
    name=package_name,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Next Version of the Free-style machine-Learning Environment by eXchanging Intermediate Blobs from Large number of Entities",
    url="https://github.com/IsaacYangSLA/nvflexible",
    package_dir={"nvflexible": "nvflexible"},
    packages=find_packages(
        where=".",
        include=[
            "*",
        ],
        exclude=[
            "test",
        ],
    ),
    package_data={"": ["*.yaml", "*.html"]},
    zip_safe=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.9",
)
