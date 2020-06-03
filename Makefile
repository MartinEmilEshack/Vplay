.PHONY: beauty_start beauty_end import
.ONESHELL:
.NOTPARALLEL:
.SILENT:

beauty_start:
	tput setaf 5
	date "+[%H:%M:%S|%d-%m-%Y] Server is running..🏃"
	tput sgr0

beauty_end:
	echo
	tput setaf 5
	printf `date "+[%H:%M:%S|%d-%m-%Y]"`
	echo " Server died"
	tput sgr0

clean_media:
	$(RM) vsrc/**

import:
	python -m pip install django
	python -m pip install ffmpeg-python
