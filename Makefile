all:
	cp src/*.py .
	chmod +x main.py
	mv main.py pbrain-gomoku-ai

re: fclean all

clean:

fclean: clean
	rm -Rf pbrain-gomoku-ai *.py

windows:
	pyinstaller --onefile src\main.py src\bot.py src\ai.py src\simple_ai.py
