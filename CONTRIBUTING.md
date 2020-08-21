# Contributing Guidelines

## Environment Setup
```
git clone https://github.com/cedricconol/bertosaurus
cd bertosaurus

# it is a good idea to create and activate a virtualenv here
pip install pre-commit
pre-commit install

# another good idea is update the hooks to the latest version
pre-commit autoupdate
```
## Best Practices

## Installation

In order to set up the necessary environment:

1. clone the `bertosaurus` repo
   ```
   git clone https://github.com/cedricconol/bertosaurus.git
   ```
2. change directory to `bertosaurus`
   ```
   cd bertosaurus
   ```
3. create an environment `bertosaurus`,
   ```
   conda env create -f environment.yaml
   ```
4. activate the new environment with
   ```
   conda activate bertosaurus
   ```
5. install `bertosaurus` with:
   ```
   python setup.py install # or `develop`
   ```

Optional and needed only once after `git clone`:

6. install several [pre-commit] git hooks with:
   ```
   pre-commit install
   ```
   and checkout the configuration under `.pre-commit-config.yaml`.
   The `-n, --no-verify` flag of `git commit` can be used to deactivate pre-commit hooks temporarily.

7. install [nbstripout] git hooks to remove the output cells of committed notebooks with:
   ```
   nbstripout --install --attributes notebooks/.gitattributes
   ```
   This is useful to avoid large diffs due to plots in your notebooks.
   A simple `nbstripout --uninstall` will revert these changes.

## Dependency Management & Reproducibility

1. Always keep your abstract (unpinned) dependencies updated in `environment.yaml` and eventually
   in `setup.cfg` if you want to ship and install your package via `pip` later on.
2. Create concrete dependencies as `environment.lock.yaml` for the exact reproduction of your
   environment with:
   ```
   conda env export -n bertosaurus -f environment.lock.yaml
   ```
   For multi-OS development, consider using `--no-builds` during the export.
3. Update your current environment with respect to a new `environment.lock.yaml` using:
   ```
   conda env update -f environment.lock.yaml --prune
   ```
