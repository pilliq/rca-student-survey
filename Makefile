all: convert generate

.PHONY: convert
convert:
	cp 'data/Students for Students survey Result - Form Responses 1.csv' ./responses.csv
	python remove-null.py responses.csv # python2
	python3 rename.py responses.csv
	rm responses.csv
	mv responses-renamed.csv responses.csv
	dos2unix responses.csv # clean up new line characters
	sqlite3 rca.db < import.sql

.PHONY: clean
clean:
	-rm responses.csv
	-rm responses-renamed.csv
	-rm questions.csv
	-rm rca.db
	-rm results/*

.PHONY: db
db:
	-sqlite3 rca.db

.PHONY: generate
generate:
	bash generate
