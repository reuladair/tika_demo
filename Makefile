# -*- makefile -*-

all : clean

clean :
	@rm -f *~
	@rm -rf __pycache__

test-string :
	@echo ""
	@echo "test-string:"
	@echo ""
	@python tika_demo.py "It was a dark and stormy night. And all the gypsies were gathered around the campfire."

test-document :
	@echo ""
	@echo "test-document:"
	@echo ""
	@python tika_demo.py docs/Anthem.odt

test-directory :
	@echo ""
	@echo "test-directory:"
	@echo ""
	@python tika_demo.py docs

test : test-string test-document test-directory
