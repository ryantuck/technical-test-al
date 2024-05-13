# AngelList Take-home project

.PHONY : setup
setup :
	mkdir -p target/

targets : target/simple_1_output.json target/simple_2_output.json target/complex_1_output.json target/complex_2_output.json

target/%_output.json : data/%_input.json
	cat $< | python allocate.py | jq > $@


