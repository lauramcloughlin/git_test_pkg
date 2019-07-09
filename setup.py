from distutils.core import setup

setup(
  name = 'git_test_pkg',
  version = '0.0.1',
  description = 'A text misclassification analysis package.',
  author = 'lauramcloughlin',
  author_email = 'b00092153@student.itb.ie',
  url = 'https://github.com/lauramcloughlin/py_git_test',
  download_url = 'https://github.com/lauramcloughlin/py_git_test/archive/1.4.12.tar.gz',
  keywords = ['git_test_pkg', 'misclassification', 'classification', 'text'],
  packages = ['git_test_pkg'],
  classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
  install_requires=[]
)
