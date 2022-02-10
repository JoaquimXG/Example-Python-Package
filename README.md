# Example Package

Testing package layouts and import structure due to issues with circular imports in other packages. 

# Structure

## Layout

- Package underneath src directory
    - This avoids issues with accidentally running local code instaed of installed package when using python -m 
- Primary package code in `__main__.py`
    - No requirement for if `__name__` == `__main__` as `__name__` will always be `__main__` when this module is run

## Function calls

1. `__main__:main` calls `one` imported from `one.py` and `three` imported from `sub_package.three.py` 
2. `one` calls `two` imported from `two.py`
3. Both `one` and `two` call `module_and_function_name_match` imported from `module_and_function_name_match.py`
4. Both `one`, `two` and `three` call `test` imported from `module_and_function_name_match.py`

## Useful Details

- Modules import functions and modules using absolute explicit imports, using the name of the package then name of the module, then name of the function if required
    - e.g.: from package_name.module_name import function_name
        - Then function is called with `function_name()`
    - or: from package_name import module_name
        - Then function is called with `module_name.function_name()`
        
# Usage

## Installed as a CLI tool

1. Setup python venv: `python -m venv .env`
2. Activate venv: `source .env/bin/activate`
3. Install as editable package: `pip install -e .`
4. Run on cli with `sample_package`

This works due to entry_points option within `setup.py`. `sample_package` has been added as an executable to the path within this environment. 

## Installed as a package

1. Setup python venv: `python -m venv .env`
2. Activate venv: `source .env/bin/activate`
3. Install as editable package: `pip install -e .`
4. Run as package: `python -m sample_package`

## Installed and imported 

1. Setup python venv: `python -m venv .env`
2. Activate venv: `source .env/bin/activate`
3. Install as editable package: `pip install -e .`
4. Import into other python projects with `import sample_package`

## Run as standalone package without installation

1. Navigate to `src/`
2. Run as package: `python -m sample_package`


# Packaging to PyPi
