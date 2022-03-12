from playwright.sync_api import sync_playwright
import time, random

def avoid_rules(page):
    page.locator('game-help').click()

def press_letter(page, key):
    page.locator(f'#keyboard button[data-key={key}]').click()

def guess_word(page, word):
    for letter in word:
        press_letter(page, letter)
    press_letter(page, '↵')

def get_hints(page, guess_num):
    rows = page.query_selector_all('game-row')
    tiles = rows[guess_num-1].query_selector_all('div.row game-tile')
    get_letter = lambda tile: tile.get_attribute('letter')
    get_evaluation = lambda tile: tile.get_attribute('evaluation')
    return [(get_letter(tile), get_evaluation(tile)) for tile in tiles]

def all_correct(page, hints):
    if len(hints) == 0:
        return False
    return all([i[1] == 'correct' for i in hints[-1]])

def prune(words, all_hints):
    # hints = [
    #           [('a', 'present'), ('b', 'correct'), ...],
    #           [...]
    #         ]

    valid_words = [i for i in words]
    for guess_hints in all_hints:
        keep_correct = lambda word: all(
        [word[i] == guess_hints[i][0] for i in range(len(word)) if guess_hints[i][1] == 'correct'])

        exclude_absent = lambda word: all(i[0] not in word for i in guess_hints if i[1] == 'absent')

        is_valid = lambda word: keep_correct(word) and exclude_absent(word)

        valid_words = list(filter(is_valid, valid_words))

    return valid_words

if __name__ == '__main__':
    with open('words.txt', 'r') as f:
        words = [i.strip('\n').strip('"') for i in f.read().split(',')]

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.nytimes.com/games/wordle/index.html')
        avoid_rules(page)

        guesses = []
        hints = []
        plausible = [word for word in words]

        while not all_correct(page, hints) and len(guesses) < 6:
            random.shuffle(plausible)
            guesses.append(plausible[0])
            guess_word(page, guesses[-1])
            time.sleep(2.1)
            hints.append(get_hints(page, len(guesses)))
            plausible = prune(words, hints)
