DATA_URL=https://codalab.coresearch.club/my/datasets/download/b0f60eb2-a93c-447d-b713-95049a3733c7

.PHONY: data


data:
	mkdir -p data
	cd data && \
	wget -O d.zip $(DATA_URL) && \
	unzip d.zip



test:
	mkdir -p out && \
	python solution.py data out


pack:
	cd out && \
	zip submission.zip data.predict
