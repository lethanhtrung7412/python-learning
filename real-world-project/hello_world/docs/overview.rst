Project Overview
================

1.5.1 Description
-----------------

The problem this project addresses is how to effectively onboard new developers. A strong onboarding project helps new team members become productive quickly and introduces experienced developers to shared tools and processes.

This project guides team members through:

- Installing a core set of development tools.
- Creating a working Python module.
- Displaying the completed work as part of a sprint demo.

Each developer will build a simple application with a command-line interface (CLI) that prints a cheerful greeting. For example:

.. code-block:: bash

   % python src/hello_world.py --who "World"
   Hello, World!

This shows how running the application with the `--who` parameter outputs a greeting to the console.

1.5.2 Approach
--------------

The goal is to build a small Python application module. The module will include internal functions or possibly a class. It will consist of the following components:

- A function to **parse command-line options**, using the `argparse` module.
- A function to **print a cheerful greeting**.
- A `main()` function to coordinate the above steps.
- An `if __name__ == "__main__":` guard to allow for unit testing and script execution.

Though simple in function, this project introduces engineering complexity suitable for testing multiple units and supports best practices in Python project structure.

1.5.3 Deliverables
------------------

The following files and structure are expected as part of the project:

- `README.md`: A summary of the project and its purpose.
- `pyproject.toml`: Defines the project configuration and dependencies.
- `docs/`: Contains the Sphinx-generated documentation:
  
  - `overview.rst`: This file.
  - `api.rst`: API reference for the code.

- `src/hello_world.py`: The main application module.
- `tests/test_hw.py`: Unit tests for the module.
- `features/hello_world.feature`: Gherkin-based acceptance test scenarios.
- `steps/hw_cli.py`: Step definitions for the feature tests.
- `environment.py`: Optional setup/teardown hooks for behave.
- `tox.ini`: Test automation using `tox`.
