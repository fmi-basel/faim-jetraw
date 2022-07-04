FAIM-Jetraw Workflows
---
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

[comment]: <> ([![tests]&#40;https://github.com/fmi-basel/faim-jetraw/workflows/tests/badge.svg&#41;]&#40;https://github.com/fmi-basel/faim-jetraw/actions&#41;)

[comment]: <> ([![codecov]&#40;https://codecov.io/gh/fmi-basel/faim-jetraw/branch/main/graph/badge.svg&#41;]&#40;https://app.codecov.io/gh/fmi-basel/faim-jetraw&#41;)

Jetraw compression workflows used in the facility for advanced mircoscopy and
imaging (FAIM) at the Friedrich Miescher Institute for biomedial research.

# Installation

We recommend creating a new conda environment with

```shell
conda create --name jrc python=3.8
```

Then install [pyJetRaw](https://github.com/Jetraw/pyJetraw)
and [DpCore](https://github.com/Jetraw/pyDpcore)
into the freshly create conda env.

__Note:__ Linux users `export
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/path_to_jetraw_folder/lib/`

Finally install this package with

```shell
pip install git+https://github.com/fmi-faim/faim-jetraw
```

# Usage

`TODO`

# Development

Install test requirements with

```shell
pip install -r requirements.txt
```

To run pre-commit hooks install

```shell
pip install pre-commit
pre-commit install
```

# License

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this software except in compliance with the License. You may obtain a copy of
the License at http://www.apache.org/licenses/LICENSE-2.0.

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
