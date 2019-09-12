from setuptools import setup, find_packages

setup(name='polish',
      version='0.1',
      description="Polish Floorplanner from Martin Wong;sPnR database python view",
      url='github.com/stevenmburns/polish_floorplanner.git',
      author='Steven Burns',
      author_email='steven.m.burns@intel.com',
      license='MIT',
      packages=find_packages(),
      setup_requires=["pytest-runner"],
      tests_require=["pytest"],
#      scripts=['gen_viewer_json.py'],
      zip_safe=False)
