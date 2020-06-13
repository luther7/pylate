# {{ cookiecutter.name }}

{%- if cookiecutter.github_actions %}
![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/tests/badge.svg)
{%- endif %}

---

## Getting Started

```sh
$ pip install --user poetry
$ poetry install
$ poetry run pre-commit install
```
