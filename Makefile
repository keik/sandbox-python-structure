TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
SELF="sandbox-python-structure"
DEV_DEPS="requirements-dev.txt"

test: init
	@echo $(TAG)$@$(END)
	flake8
	py.test tests --cov sandbox_python_structure --verbose

init: uninstall
	@echo $(TAG)$@$(END)
	pip install --upgrade -r $(DEV_DEPS)
	pip install --upgrade --editable .

uninstall:
	@echo $(TAG)$@$(END)
	- pip uninstall --yes -r $(DEV_DEPS) 2>/dev/null
