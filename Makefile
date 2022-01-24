all:
	pip install pyinstaller
	pyinstaller --onefile src\main.py

	echo $(OS)
	ifeq ($(OS),Windows_NT)
		copy dist\main.exe pbrain-gomoku-ai.exe
	else
		cp dist\main pbrain-gomoku-ai
	endif

re: fclean all

clean:
	ifeq ($(OS),Windows_NT)
		rd /s /q main.spec build dist src\__pycache__
	else
		rm -Rf main.spec build dist src\__pycache__
	endif

fclean: clean
	ifeq ($(OS),Windows_NT)
		rd /s /q pbrain-gomoku-ai.exe
	else
		rm -Rf pbrain-gomoku-ai
	endif
