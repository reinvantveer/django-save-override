# django-save-override
Minimal reproducible example of bug described in https://github.com/typeddjango/django-stubs/issues/2041

## Instructions
```shell
git clone git@github.com:reinvantveer/django-save-override
cd django-save-override
poetry install
poetry run mypy .
```
This should result in:
```
src/myapp/myapp/models.py:14: error: Method "save" is marked as an override, but no base method was found with this name  [misc]
Found 1 error in 1 file (checked 7 source files)
```
