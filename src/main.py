#!/usr/bin/env python3
from bot import Bot
from simple_ai import SimpleAI
from basic_ai import BasicAi

def main():
    b = Bot(BasicAi)
    b.run()

if __name__ == '__main__':
    main()