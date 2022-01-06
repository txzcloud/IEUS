from blessed import Terminal

import database

term = Terminal()

# ========== UI CONSTANTS ==========
MID_WIDTH = term.width // 2
MID_HEIGHT = term.height // 2

UI_WIDTH = 150
UI_HEIGHT = 50

BORDER_TOP_WIDTH = MID_WIDTH - (UI_WIDTH // 2)
BORDER_TOP_HEIGHT = MID_HEIGHT - (UI_HEIGHT // 2)

# Login Page
BANNER = ["      ___           ___                                     ___                         ___           ___           ___     ",
          "     /\  \         /\__\         _____                     /\  \                       /\  \         /\  \         /|  |    ",
          "    |::\  \       /:/ _/_       /::\  \       ___         /::\  \         ___         /::\  \       /::\  \       |:|  |    ",
          "    |:|:\  \     /:/ /\__\     /:/\:\  \     /\__\       /:/\:\  \       /\__\       /:/\:\__\     /:/\:\  \      |:|  |    ",
          "  __|:|\:\  \   /:/ /:/ _/_   /:/  \:\__\   /:/__/      /:/ /::\  \     /:/  /      /:/ /:/  /    /:/ /::\  \   __|:|  |    ",
          " /::::|_\:\__\ /:/_/:/ /\__\ /:/__/ \:|__| /::\  \     /:/_/:/\:\__\   /:/__/      /:/_/:/__/___ /:/_/:/\:\__\ /\ |:|__|____",
          " \:\~~\  \/__/ \:\/:/ /:/  / \:\  \ /:/  / \/\:\  \__  \:\/:/  \/__/  /::\  \      \:\/:::::/  / \:\/:/  \/__/ \:\/:::::/__/",
          "  \:\  \        \::/_/:/  /   \:\  /:/  /   ~~\:\/\__\  \::/__/      /:/\:\  \      \::/~~/~~~~   \::/__/       \::/~~/~    ",
          "   \:\  \        \:\/:/  /     \:\/:/  /       \::/  /   \:\  \      \/__\:\  \      \:\~~\        \:\  \        \:\~~\     ",
          "    \:\__\        \::/  /       \::/  /        /:/  /     \:\__\          \:\__\      \:\__\        \:\__\        \:\__\    ",
          "     \/__/         \/__/         \/__/         \/__/       \/__/           \/__/       \/__/         \/__/         \/__/    "]

LOGIN_WIDTH = 50
ENTRY_BOX_WIDTH = 37

LOGIN_BOX = ["╭" + "─" * LOGIN_WIDTH + "╮",
             "|" + " " * LOGIN_WIDTH + "|",
             "|" + " " * 10 + "╭" + "─" * ENTRY_BOX_WIDTH + "╮ |",
             "| Username |" + " " * ENTRY_BOX_WIDTH + "| |",
             "|" + " " * 10 + "╰" + "─" * ENTRY_BOX_WIDTH + "╯ |",
             "|" + " " * LOGIN_WIDTH + "|",
             "|" + " " * 10 + "╭" + "─" * ENTRY_BOX_WIDTH + "╮ |",
             "| Password |" + " " * ENTRY_BOX_WIDTH + "| |",
             "|" + " " * 10 + "╰" + "─" * ENTRY_BOX_WIDTH + "╯ |",
             "|" + " " * LOGIN_WIDTH + "|",
             "|" + " " * 11 + "╭" + "─" * 9 + "╮" + " " * 7 + "╭" + "─" * 8 + "╮" + " " * 11 + "|",
             "|" + " " * 11 + "| Sign Up |" + " " * 7 + "| Log In |" + " " * 11 + "|",
             "|" + " " * 11 + "╰" + "─" * 9 + "╯" + " " * 7 + "╰" + "─" * 8 + "╯" + " " * 11 + "|",
             "|" + " " * LOGIN_WIDTH + "|",
             "╰" + "─" * LOGIN_WIDTH + "╯"]

# List Pages
SEARCH_BAR_WIDTH = 116
ITEM_WIDTH = 128

# UI Globals
current_page = ""
frame_stack = []
current_frame = 0


def render_login():  # login page
    global current_page

    # draw main border
    x, y = BORDER_TOP_WIDTH, BORDER_TOP_HEIGHT
    print(term.home + term.clear + term.move_xy(x, y) + "╭" + "─" * UI_WIDTH + "╮")
    for _ in range(UI_HEIGHT - 2):
        y += 1
        print(term.move_xy(x, y) + "|" + " " * UI_WIDTH + "|")
    y += 1
    print(term.move_xy(x, y) + "╰" + "─" * UI_WIDTH + "╯")

    # create new frame
    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # add banner to frame
    index = 5  # starting location of banner
    for line in BANNER:
        frame[index] = f"{line:^{UI_WIDTH}}"
        index += 1

    # add login box to frame
    index += 5
    for line in LOGIN_BOX:
        frame[index] = f"{line:^{UI_WIDTH}}"
        index += 1

    current_page = "LOGIN"
    render_frame(frame)


def render_login_error_message(message):  # render error message on login page
    x, y = BORDER_TOP_WIDTH + 1, BORDER_TOP_HEIGHT + 21
    print(term.move_xy(x, y) + f"{message:^{UI_WIDTH}}")


def render_username(username):  # render username on login page
    if len(username) >= ENTRY_BOX_WIDTH:
        return

    x, y = BORDER_TOP_WIDTH + 62, BORDER_TOP_HEIGHT + 25
    print(term.move_xy(x, y) + f"{username:<{ENTRY_BOX_WIDTH}}")


def render_password(password):  # render password on login page
    if len(password) >= ENTRY_BOX_WIDTH:
        return

    x, y = BORDER_TOP_WIDTH + 62, BORDER_TOP_HEIGHT + 29
    print(term.move_xy(x, y) + f"{password:<{ENTRY_BOX_WIDTH}}")


def render_books(search, page, home=False):
    global current_page

    if home:  # if this is home page render
        frame_stack.pop()  # pop login page from stack

    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # render top bar (navbar)
    frame[0] = "      ╭───────╮ ╭───────╮ ╭────────╮" + " " * 74 + "╭──────────╮ ╭──────────╮ ╭───────────╮ "
    frame[1] = " ← →  | Books | | Games | | Movies |" + " " * 74 + "| My Books | | My Games | | My Movies | "
    frame[2] = "      ╰───────╯ ╰───────╯ ╰────────╯" + " " * 74 + "╰──────────╯ ╰──────────╯ ╰───────────╯ "

    # render search bar
    frame[4] = " " * 15 + "╭" + "─" * SEARCH_BAR_WIDTH + "╮" + " " * 15
    frame[5] = " " * 15 + "|" + f"{search:<{SEARCH_BAR_WIDTH}}" + "|" + " " * 15
    frame[6] = " " * 15 + "╰" + "─" * SEARCH_BAR_WIDTH + "╯" + " " * 15

    # render books
    if search != "":
        books, total_books = database.search_books(search, page)
    else:
        books = database.get_books(page)
        total_books = database.get_books_count()

    index = 9  # start index for rendering books
    for book in books:
        frame[index] = " " * 10 + "╭" + "─" * ITEM_WIDTH + "╮" + " " * 10
        frame[index + 1] = " " * 10 + f"| {book[1]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book title
        frame[index + 2] = " " * 10 + f"| {'Author: ' + book[2]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book author
        frame[index + 3] = " " * 10 + f"| {'Published: ' + book[3]:<{ITEM_WIDTH - 6}}+    |" + " " * 10  # book publish date
        frame[index + 4] = " " * 10 + f"| {'ISBN: ' + book[0]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book isbn
        frame[index + 5] = " " * 10 + "|" + " " * ITEM_WIDTH + "|" + " " * 10
        frame[index + 6] = " " * 10 + f"| {book[4]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book description
        frame[index + 7] = " " * 10 + "╰" + "─" * ITEM_WIDTH + "╯" + " " * 10
        index += 9  # move to next book render

    # render page number
    total_pages = total_books // 4 + 1

    frame[-2] = f"{'Page ' + str(page) + ' of ' + str(total_pages):^{UI_WIDTH}}"

    current_page = "BOOKS"
    render_frame(frame)

    return books, total_pages


def render_games(search, page):
    global current_page

    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # render top bar (navbar)
    frame[0] = "      ╭───────╮ ╭───────╮ ╭────────╮" + " " * 74 + "╭──────────╮ ╭──────────╮ ╭───────────╮ "
    frame[1] = " ← →  | Books | | Games | | Movies |" + " " * 74 + "| My Books | | My Games | | My Movies | "
    frame[2] = "      ╰───────╯ ╰───────╯ ╰────────╯" + " " * 74 + "╰──────────╯ ╰──────────╯ ╰───────────╯ "

    # render search bar
    frame[4] = " " * 15 + "╭" + "─" * SEARCH_BAR_WIDTH + "╮" + " " * 15
    frame[5] = " " * 15 + "|" + f"{search:<{SEARCH_BAR_WIDTH}}" + "|" + " " * 15
    frame[6] = " " * 15 + "╰" + "─" * SEARCH_BAR_WIDTH + "╯" + " " * 15

    # render games
    if search != "":
        games, total_games = database.search_games(search, page)
    else:
        games = database.get_games(page)
        total_games = database.get_games_count()

    index = 9  # start index for rendering games
    for game in games:
        frame[index] = " " * 10 + "╭" + "─" * ITEM_WIDTH + "╮" + " " * 10
        frame[index + 1] = " " * 10 + f"| {game[1]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 2] = " " * 10 + f"| {'Developer: ' + game[3]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 3] = " " * 10 + f"| {'Publisher: ' + game[2]:<{ITEM_WIDTH - 6}}+    |" + " " * 10
        frame[index + 4] = " " * 10 + f"| {'Release: ' + game[4]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 5] = " " * 10 + "|" + " " * ITEM_WIDTH + "|" + " " * 10
        frame[index + 6] = " " * 10 + f"| {game[5]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 7] = " " * 10 + "╰" + "─" * ITEM_WIDTH + "╯" + " " * 10
        index += 9

    # render page number
    total_pages = total_games // 4 + 1

    frame[-2] = f"{'Page ' + str(page) + ' of ' + str(total_pages):^{UI_WIDTH}}"

    current_page = "GAMES"
    render_frame(frame)

    return games, total_pages


def render_movies(search, page):
    global current_page

    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # render top bar (navbar)
    frame[0] = "      ╭───────╮ ╭───────╮ ╭────────╮" + " " * 74 + "╭──────────╮ ╭──────────╮ ╭───────────╮ "
    frame[1] = " ← →  | Books | | Games | | Movies |" + " " * 74 + "| My Books | | My Games | | My Movies | "
    frame[2] = "      ╰───────╯ ╰───────╯ ╰────────╯" + " " * 74 + "╰──────────╯ ╰──────────╯ ╰───────────╯ "

    # render search bar
    frame[4] = " " * 15 + "╭" + "─" * SEARCH_BAR_WIDTH + "╮" + " " * 15
    frame[5] = " " * 15 + "|" + f"{search:<{SEARCH_BAR_WIDTH}}" + "|" + " " * 15
    frame[6] = " " * 15 + "╰" + "─" * SEARCH_BAR_WIDTH + "╯" + " " * 15

    # render movies
    if search != "":
        movies, total_movies = database.search_movies(search, page)
    else:
        movies = database.get_movies(page)
        total_movies = database.get_movies_count()

    index = 9
    for movie in movies:
        frame[index] = " " * 10 + "╭" + "─" * ITEM_WIDTH + "╮" + " " * 10
        frame[index + 1] = " " * 10 + f"| {movie[1]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 2] = " " * 10 + f"| {'Director: ' + movie[2]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 3] = " " * 10 + f"| {'Release: ' + movie[3]:<{ITEM_WIDTH - 6}}+    |" + " " * 10
        frame[index + 4] = " " * 10 + "|" + " " * ITEM_WIDTH + "|" + " " * 10
        frame[index + 5] = " " * 10 + f"| {movie[4]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 6] = " " * 10 + "╰" + "─" * ITEM_WIDTH + "╯" + " " * 10
        index += 8

    # render page number
    total_pages = total_movies // 4 + 1

    frame[-2] = f"{'Page ' + str(page) + ' of ' + str(total_pages):^{UI_WIDTH}}"

    current_page = "MOVIES"
    render_frame(frame)

    return movies, total_pages


def render_search(search):
    if len(search) >= SEARCH_BAR_WIDTH:
        return

    x, y = BORDER_TOP_WIDTH + 17, BORDER_TOP_HEIGHT + 6
    print(term.move_xy(x, y) + f"{search:<{SEARCH_BAR_WIDTH}}")


def render_user_books(username, page, rerender=False):
    global current_page

    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # render top bar (navbar)
    frame[0] = "      ╭───────╮ ╭───────╮ ╭────────╮" + " " * 74 + "╭──────────╮ ╭──────────╮ ╭───────────╮ "
    frame[1] = " ← →  | Books | | Games | | Movies |" + " " * 74 + "| My Books | | My Games | | My Movies | "
    frame[2] = "      ╰───────╯ ╰───────╯ ╰────────╯" + " " * 74 + "╰──────────╯ ╰──────────╯ ╰───────────╯ "

    # render user books
    user_books = database.get_user_books(username, page)

    index = 6
    for book in user_books:
        # create rating string
        rating_string = f"{'★' * book[5]:{'☆'}<{5}}"

        frame[index] = " " * 10 + "╭" + "─" * ITEM_WIDTH + "╮" + " " * 10
        frame[index + 1] = " " * 10 + f"| {book[1]:<{ITEM_WIDTH - 8}}{rating_string}  |" + " " * 10  # book title
        frame[index + 2] = " " * 10 + f"| {'Author: ' + book[2]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book author
        frame[index + 3] = " " * 10 + f"| {'Published: ' + book[3]:<{ITEM_WIDTH - 6}}x    |" + " " * 10  # book publish date
        frame[index + 4] = " " * 10 + f"| {'ISBN: ' + book[0]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book isbn
        frame[index + 5] = " " * 10 + "|" + " " * ITEM_WIDTH + "|" + " " * 10
        frame[index + 6] = " " * 10 + f"| {book[4]:<{ITEM_WIDTH - 1}}|" + " " * 10  # book description
        frame[index + 7] = " " * 10 + "╰" + "─" * ITEM_WIDTH + "╯" + " " * 10
        index += 9  # move to next book render

    # render page number
    total_pages = database.get_user_books_count(username) // 4 + 1

    frame[-2] = f"{'Page ' + str(page) + ' of ' + str(total_pages):^{UI_WIDTH}}"

    current_page = "USERBOOKS"
    render_frame(frame, rerender)

    return user_books, total_pages


def render_user_games(username, page, rerender=False):
    global current_page

    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # render top bar (navbar)
    frame[0] = "      ╭───────╮ ╭───────╮ ╭────────╮" + " " * 74 + "╭──────────╮ ╭──────────╮ ╭───────────╮ "
    frame[1] = " ← →  | Books | | Games | | Movies |" + " " * 74 + "| My Books | | My Games | | My Movies | "
    frame[2] = "      ╰───────╯ ╰───────╯ ╰────────╯" + " " * 74 + "╰──────────╯ ╰──────────╯ ╰───────────╯ "

    # render user games
    user_games = database.get_user_games(username, page)

    index = 6
    for game in user_games:
        # create rating string
        rating_string = f"{'★' * game[5]:{'☆'}<{5}}"

        frame[index] = " " * 10 + "╭" + "─" * ITEM_WIDTH + "╮" + " " * 10
        frame[index + 1] = " " * 10 + f"| {game[1]:<{ITEM_WIDTH - 8}}{rating_string}  |" + " " * 10
        frame[index + 2] = " " * 10 + f"| {'Developer: ' + game[3]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 3] = " " * 10 + f"| {'Publisher: ' + game[2]:<{ITEM_WIDTH - 6}}x    |" + " " * 10
        frame[index + 4] = " " * 10 + f"| {'Release: ' + game[4]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 5] = " " * 10 + "|" + " " * ITEM_WIDTH + "|" + " " * 10
        frame[index + 6] = " " * 10 + f"| {game[5]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 7] = " " * 10 + "╰" + "─" * ITEM_WIDTH + "╯" + " " * 10
        index += 9

    # render page number
    total_pages = database.get_user_games_count(username) // 4 + 1

    frame[-2] = f"{'Page ' + str(page) + ' of ' + str(total_pages):^{UI_WIDTH}}"

    current_page = "USERGAMES"
    render_frame(frame, rerender)

    return user_games, total_pages


def render_user_movies(username, page, rerender=False):
    global current_page

    frame = [" " * UI_WIDTH for _ in range(UI_HEIGHT - 2)]

    # render top bar (navbar)
    frame[0] = "      ╭───────╮ ╭───────╮ ╭────────╮" + " " * 74 + "╭──────────╮ ╭──────────╮ ╭───────────╮ "
    frame[1] = " ← →  | Books | | Games | | Movies |" + " " * 74 + "| My Books | | My Games | | My Movies | "
    frame[2] = "      ╰───────╯ ╰───────╯ ╰────────╯" + " " * 74 + "╰──────────╯ ╰──────────╯ ╰───────────╯ "

    # render user movies
    user_movies = database.get_user_movies(username, page)

    index = 6
    for movie in user_movies:
        # create rating string
        rating_string = f"{'★' * movie[5]:{'☆'}<{5}}"

        frame[index] = " " * 10 + "╭" + "─" * ITEM_WIDTH + "╮" + " " * 10
        frame[index + 1] = " " * 10 + f"| {movie[1]:<{ITEM_WIDTH - 8}}{rating_string}  |" + " " * 10
        frame[index + 2] = " " * 10 + f"| {'Director: ' + movie[2]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 3] = " " * 10 + f"| {'Release: ' + movie[3]:<{ITEM_WIDTH - 6}}x    |" + " " * 10
        frame[index + 4] = " " * 10 + "|" + " " * ITEM_WIDTH + "|" + " " * 10
        frame[index + 5] = " " * 10 + f"| {movie[4]:<{ITEM_WIDTH - 1}}|" + " " * 10
        frame[index + 6] = " " * 10 + "╰" + "─" * ITEM_WIDTH + "╯" + " " * 10
        index += 8

    # render page number
    total_pages = database.get_user_movies_count(username) // 4 + 1

    frame[-2] = f"{'Page ' + str(page) + ' of ' + str(total_pages):^{UI_WIDTH}}"

    current_page = "USERMOVIES"
    render_frame(frame, rerender)

    return user_movies, total_pages


def render_back():
    global current_page, current_frame

    if current_frame <= 1:
        return

    current_frame -= 1
    current_page = frame_stack[current_frame][1]
    render_frame(frame_stack[current_frame][0])


def render_forward():
    global current_page, current_frame

    if current_frame == len(frame_stack) - 1:
        return

    current_frame += 1
    current_page = frame_stack[current_frame][1]
    render_frame(frame_stack[current_frame][0])


def render_frame(frame, rerender=False):
    global current_frame

    if current_frame + 1 < len(frame_stack):  # frame stack currently has forward frame(s) (replace them)
        while current_frame + 1 < len(frame_stack):
            frame_stack.pop()

    if not rerender:
        frame_stack.append((frame, current_page))
        current_frame += 1

    x, y = BORDER_TOP_WIDTH + 1, BORDER_TOP_HEIGHT + 1
    for line in frame:
        print(term.move_xy(x, y) + line)
        y += 1
