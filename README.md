# django-save-override
## Why is this here?
To provide a minimal reproducible example of bug described in https://github.com/typeddjango/django-stubs/issues/2041

It seems that mypy cannot infer the overridden `save()` method from the base Django Model class if you decorate it with an
`@override` decorator.

## Why would you want that?
The `@override` suppresses the Ruff errors that appear when there are boolean arguments in a method or function, such as the `save()`
method of the Django base Model. Since we cannot (and should not) create a different method signature in our inherited class, we can
signal to Ruff and other style checkers that we're not adding boolean arguments because we like it, but we have to follow conventions.
The `@override` decorator is understood by Ruff, but not by Mypy.

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
