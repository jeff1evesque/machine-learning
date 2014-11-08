
BIN := node_modules/.bin
REPORTER ?= spec
SRC = index.js
TESTS = test.js

test: node_modules
	$(BIN)/mocha \
	  --reporter $(REPORTER)

coverage: $(SRC) $(TESTS)
	$(BIN)/istanbul cover $(BIN)/_mocha -- \
	  --reporter $(REPORTER)

node_modules: package.json
	@npm install
	@touch $@

clean:
	rm -rf coverage

.PHONY: test clean
