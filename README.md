# Chaos Platform gRPC Library

[![Version](https://img.shields.io/pypi/v/chaosplatform-grpc.svg)](https://img.shields.io/pypi/v/chaosplatform-grpc.svg)
[![License](https://img.shields.io/pypi/l/chaosplatform-grpc.svg)](https://img.shields.io/pypi/l/chaosplatform-grpc.svg)
[![StackOverflow](https://img.shields.io/badge/StackOverflow-ChaosPlatform-blue.svg)](https://stackoverflow.com/questions/tagged/chaosplatform+or+chaostoolkit)

[![Build Status](https://travis-ci.org/chaostoolkit/chaosplatform-grpc.svg?branch=master)](https://travis-ci.org/chaostoolkit/chaosplatform-grpc)
[![Python versions](https://img.shields.io/pypi/pyversions/chaosplatform-grpc.svg)](https://www.python.org/)

This is the authentication service of the [Chaos Platform][chaosplatform].

[chaosplatform]: https://chaosplatform.org/

## Purpose

* Provide a REST api to manage access tokens
* Provide a gRPC api to manage access tokens
* Provide a web entrypoint to register a new user using an OAuth2 provider

## Content

* [Install]

[install]: ./docs/install.md

## Contribute

Contributors to this project are welcome as this is an open-source effort that
seeks [discussions][join] and continuous improvement.

[join]: https://join.chaostoolkit.org/

From a code perspective, if you wish to contribute, you will need to run a 
Python 3.5+ environment. Then, fork this repository and submit a PR. The
project cares for code readability and checks the code style to match best
practices defined in [PEP8][pep8]. Please also make sure you provide tests
whenever you submit a PR so we keep the code reliable.

[pep8]: https://pycodestyle.readthedocs.io/en/latest/

The Chaos Platform projects require all contributors must sign a
[Developer Certificate of Origin][dco] on each commit they would like to merge
into the master branch of the repository. Please, make sure you can abide by
the rules of the DCO before submitting a PR.

[dco]: https://github.com/probot/dco#how-it-works