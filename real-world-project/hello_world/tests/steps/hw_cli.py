from behave import when, then
import subprocess

@when(u'we run command "python src/hello_world.py"')
def step_run_hello_world(context):
    """Run the hello_world.py script using subprocess."""
    result = subprocess.run(
        ["python", "src/hello_world.py"],
        capture_output=True,
        text=True
    )
    context.cli_output = result.stdout.strip()

@then(u'output has "Hello, World!"')
def step_check_output(context):
    """Verify that the expected greeting is in the output."""
    assert "Hello, World!" in context.cli_output, \
        f'Expected "Hello, World!" in output, but got: {context.cli_output}'
