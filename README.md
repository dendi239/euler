# euler
[![pytest](https://github.com/dendi239/euler/actions/workflows/main.yml/badge.svg)](https://github.com/dendi239/euler/actions/workflows/main.yml)

My model solutions for project-euler tasks.

## Structure

This repo contains of files `xxx-yyy-yyy-yyy.py` where `xxx` is id of the task, `yyy-yyy-yyy` is human-readable comment to its name.
Every such file has main function to solve problem itself and `test_zzz` function that checks correctness of algorithm itself for smaller input (typically, given within problem statement).

## Testing

Since all tests are done in `test_zzz` functions, one can use `pytest` for testing all the problems.
Given strange discover process of `pytest` (you need to have `test` in filename to scan your file), you can pass files to it directly, e.g.:
```shell
pytest 001-multiples-3-and-5.py
```

However, it's quite strange, so one can use wildcard here:
```shell
pytest -v *.py
```
