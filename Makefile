.PHONY: server
server:
	poetry run lektor server

.PHONY: generate-html
generate-html:
	poetry run lektor build --output-path public
