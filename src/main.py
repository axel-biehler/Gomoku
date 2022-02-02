#!/usr/bin/env python3
from bot import Bot
from simple_ai import SimpleAI

def main():
    b = Bot(SimpleAI)
    b.run()

if __name__ == '__main__':
    main()