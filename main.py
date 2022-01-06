from pynput import mouse, keyboard

import database
import ui


# used to track focused text boxes
focused_text_box = ""

# holds the text inside the login text boxes
username = ""
password = ""

# holds the text inside search bar (books, games, movies pages)
search = ""

# holds currently logged in user
current_user = ""

# holds current page (for book, game, and movie lists)
page = 1
pages_total = 1

# holds items on current page
page_items = []


def on_click(x, y, button, pressed):
    global focused_text_box, current_user, page, page_items, pages_total

    if ui.current_page == "LOGIN":
        if 1156 <= x <= 1460 and 704 <= y <= 735:  # username text box clicked on
            focused_text_box = "username"
        elif 1156 <= x <= 1460 and 770 <= y <= 800:  # password text box clicked on
            focused_text_box = "password"
        elif 1160 <= x <= 1250 and 830 <= y <= 860:  # sign up button
            if username == "" or password == "":
                ui.render_login_error_message("Please fill out all fields before signing up / logging in.")
            elif database.check_existing_user(username) > 0:
                ui.render_login_error_message("Chosen username already taken.")
            else:  # username does not already exist
                database.create_user(username, password)
                current_user = username

                page_items, pages_total = ui.render_books("", page, True)
        elif 1308 <= x <= 1380 and 830 <= y <= 860:  # login button
            if username == "" or password == "":
                ui.render_login_error_message("Please fill out all fields before signing up / logging in.")
            elif database.login_user(username, password) > 0:  # account exists
                page_items, pages_total = ui.render_books("", page, True)
            else:  # account does not exist
                ui.render_login_error_message("Account with given information does not exist.")

        # ui.render_username(f"{x},{y}")
    elif ui.current_page == "BOOKS":
        if 680 <= x <= 687 and 350 <= y <= 354:  # back button
            if pressed:
                ui.render_back()
        elif 696 <= x <= 703 and 350 <= y <= 354:  # forward button
            if pressed:
                ui.render_forward()
        elif 805 <= x <= 867 and 336 <= y <= 367:  # games button
            page = 1
            page_items, pages_total = ui.render_games("", page)
        elif 885 <= x <= 954 and 336 <= y <= 367:  # movies button
            page = 1
            page_items, pages_total = ui.render_movies("", page)
        elif 1556 <= x <= 1643 and 336 <= y <= 367:  # user books button
            page = 1
            page_items, pages_total = ui.render_user_books(current_user, page)
        elif 1661 <= x <= 1747 and 336 <= y <= 367:  # user games button
            page = 1
            page_items, pages_total = ui.render_user_games(current_user, page)
        elif 1765 <= x <= 1858 and 336 <= y <= 367:  # user movies button
            page = 1
            page_items, pages_total = ui.render_user_movies(current_user, page)
        elif 797 <= x <= 1730 and 400 <= y <= 430:  # search bar
            focused_text_box = "search"
        elif 1745 <= x <= 1750 and 525 <= y <= 530:  # add first item in list
            # check if user already added book to their collection
            if pressed and database.check_book_already_added(current_user, page_items[0][0]) == 0:
                database.insert_user_book(current_user, page_items[0][0])
        elif 1745 <= x <= 1750 and 670 <= y <= 675:  # add second item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 2 and database.check_book_already_added(current_user, page_items[1][0]) == 0:
                database.insert_user_book(current_user, page_items[1][0])
        elif 1745 <= x <= 1750 and 815 <= y <= 820:  # add third item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 3 and database.check_book_already_added(current_user, page_items[2][0]) == 0:
                database.insert_user_book(current_user, page_items[2][0])
        elif 1745 <= x <= 1750 and 958 <= y <= 963:  # add fourth item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 4 and database.check_book_already_added(current_user, page_items[3][0]) == 0:
                database.insert_user_book(current_user, page_items[3][0])

        # ui.render_username(f"{x},{y}")
    elif ui.current_page == "GAMES":
        if 680 <= x <= 687 and 350 <= y <= 354:  # back button
            if pressed:
                ui.render_back()
        elif 696 <= x <= 703 and 350 <= y <= 354:  # forward button
            if pressed:
                ui.render_forward()
        elif 724 <= x <= 787 and 336 <= y <= 367:  # books button
            page = 1
            page_items, pages_total = ui.render_books("", page)
        elif 885 <= x <= 954 and 336 <= y <= 367:  # movies button
            page = 1
            page_items, pages_total = ui.render_movies("", page)
        elif 1556 <= x <= 1643 and 336 <= y <= 367:  # user books button
            page = 1
            page_items, pages_total = ui.render_user_books(current_user, page)
        elif 1661 <= x <= 1747 and 336 <= y <= 367:  # user games button
            page = 1
            page_items, pages_total = ui.render_user_games(current_user, page)
        elif 1765 <= x <= 1858 and 336 <= y <= 367:  # user movies button
            page = 1
            page_items, pages_total = ui.render_user_movies(current_user, page)
        elif 797 <= x <= 1730 and 400 <= y <= 430:  # search bar
            focused_text_box = "search"
        elif 1745 <= x <= 1750 and 525 <= y <= 530:  # add first item in list
            # make sure user has not already added item to their collection
            if pressed and database.check_game_already_added(current_user, page_items[0][0]) == 0:
                database.insert_user_game(current_user, page_items[0][0])
        elif 1745 <= x <= 1750 and 670 <= y <= 675:  # add second item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 2 and database.check_game_already_added(current_user, page_items[1][0]) == 0:
                database.insert_user_game(current_user, page_items[1][0])
        elif 1745 <= x <= 1750 and 815 <= y <= 820:  # add third item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 3 and database.check_game_already_added(current_user, page_items[2][0]) == 0:
                database.insert_user_game(current_user, page_items[2][0])
        elif 1745 <= x <= 1750 and 958 <= y <= 963:  # add fourth item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 4 and database.check_game_already_added(current_user, page_items[3][0]) == 0:
                database.insert_user_game(current_user, page_items[3][0])

    elif ui.current_page == "MOVIES":
        if 680 <= x <= 687 and 350 <= y <= 354:  # back button
            if pressed:
                ui.render_back()
        elif 696 <= x <= 703 and 350 <= y <= 354:  # forward button
            if pressed:
                ui.render_forward()
        elif 724 <= x <= 787 and 336 <= y <= 367:  # books button
            page = 1
            page_items, pages_total = ui.render_books("", page)
        elif 805 <= x <= 867 and 336 <= y <= 367:  # games button
            page = 1
            page_items, pages_total = ui.render_games("", page)
        elif 1556 <= x <= 1643 and 336 <= y <= 367:  # user books button
            page = 1
            page_items, pages_total = ui.render_user_books(current_user, page)
        elif 1661 <= x <= 1747 and 336 <= y <= 367:  # user games button
            page = 1
            page_items, pages_total = ui.render_user_games(current_user, page)
        elif 1765 <= x <= 1858 and 336 <= y <= 367:  # user movies button
            page = 1
            page_items, pages_total = ui.render_user_movies(current_user, page)
        elif 797 <= x <= 1730 and 400 <= y <= 430:  # search bar
            focused_text_box = "search"
        elif 1745 <= x <= 1750 and 525 <= y <= 530:  # add first item in list
            # make sure user has not already added item to their collection
            if pressed and database.check_movie_already_added(current_user, page_items[0][0]) == 0:
                database.insert_user_movie(current_user, page_items[0][0])
        elif 1745 <= x <= 1750 and 655 <= y <= 660:  # add second item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 2 and database.check_movie_already_added(current_user, page_items[1][0]) == 0:
                database.insert_user_movie(current_user, page_items[1][0])
        elif 1745 <= x <= 1750 and 783 <= y <= 788:  # add third item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 3 and database.check_movie_already_added(current_user, page_items[2][0]) == 0:
                database.insert_user_movie(current_user, page_items[2][0])
        elif 1745 <= x <= 1750 and 910 <= y <= 915:  # add fourth item in list
            # check that item exists and the user has not already added this item to their collection
            if pressed and len(page_items) >= 4 and database.check_movie_already_added(current_user, page_items[3][0]) == 0:
                database.insert_user_movie(current_user, page_items[3][0])

    elif ui.current_page == "USERBOOKS":
        if 680 <= x <= 687 and 350 <= y <= 354:  # back button
            if pressed:
                ui.render_back()
        elif 696 <= x <= 703 and 350 <= y <= 354:  # forward button
            if pressed:
                ui.render_forward()
        elif 724 <= x <= 787 and 336 <= y <= 367:  # books button
            page = 1
            page_items, pages_total = ui.render_books("", page)
        elif 805 <= x <= 867 and 336 <= y <= 367:  # games button
            page = 1
            page_items, pages_total = ui.render_games("", page)
        elif 885 <= x <= 954 and 336 <= y <= 367:  # movies button
            page = 1
            page_items, pages_total = ui.render_movies("", page)
        elif 1661 <= x <= 1747 and 336 <= y <= 367:  # user games button
            page = 1
            page_items, pages_total = ui.render_user_games(current_user, page)
        elif 1765 <= x <= 1858 and 336 <= y <= 367:  # user movies button
            page = 1
            page_items, pages_total = ui.render_user_movies(current_user, page)
        elif 1745 <= x <= 1750 and 477 <= y <= 484:  # delete first item in list
            if pressed:
                database.delete_user_book(current_user, page_items[0][0])
                page_items, pages_total = ui.render_user_books(current_user, page, True)
        elif 1745 <= x <= 1750 and 621 <= y <= 627:  # delete second item in list
            if pressed and len(page_items) >= 2:
                database.delete_user_book(current_user, page_items[1][0])
                page_items, pages_total = ui.render_user_books(current_user, page, True)
        elif 1745 <= x <= 1750 and 765 <= y <= 772:  # delete third item in list
            if pressed and len(page_items) >= 3:
                database.delete_user_book(current_user, page_items[2][0])
                page_items, pages_total = ui.render_user_books(current_user, page, True)
        elif 1745 <= x <= 1750 and 909 <= y <= 916:  # delete fourth item in list
            if pressed and len(page_items) >= 4:
                database.delete_user_book(current_user, page_items[3][0])
                page_items, pages_total = ui.render_user_books(current_user, page, True)

    elif ui.current_page == "USERGAMES":
        if 680 <= x <= 687 and 350 <= y <= 354:  # back button
            if pressed:
                ui.render_back()
        elif 696 <= x <= 703 and 350 <= y <= 354:  # forward button
            if pressed:
                ui.render_forward()
        elif 724 <= x <= 787 and 336 <= y <= 367:  # books button
            page = 1
            page_items, pages_total = ui.render_books("", page)
        elif 805 <= x <= 867 and 336 <= y <= 367:  # games button
            page = 1
            page_items, pages_total = ui.render_games("", page)
        elif 885 <= x <= 954 and 336 <= y <= 367:  # movies button
            page = 1
            page_items, pages_total = ui.render_movies("", page)
        elif 1556 <= x <= 1643 and 336 <= y <= 367:  # user books button
            page = 1
            page_items, pages_total = ui.render_user_books(current_user, page)
        elif 1765 <= x <= 1858 and 336 <= y <= 367:  # user movies button
            page = 1
            page_items, pages_total = ui.render_user_movies(current_user, page)
        elif 1745 <= x <= 1750 and 477 <= y <= 484:  # delete first item in list
            if pressed:
                database.delete_user_game(current_user, page_items[0][0])
                page_items, pages_total = ui.render_user_games(current_user, page, True)
        elif 1745 <= x <= 1750 and 621 <= y <= 627:  # delete second item in list
            if pressed and len(page_items) >= 2:
                database.delete_user_game(current_user, page_items[1][0])
                page_items, pages_total = ui.render_user_games(current_user, page, True)
        elif 1745 <= x <= 1750 and 765 <= y <= 772:  # delete third item in list
            if pressed and len(page_items) >= 3:
                database.delete_user_game(current_user, page_items[2][0])
                page_items, pages_total = ui.render_user_games(current_user, page, True)
        elif 1745 <= x <= 1750 and 909 <= y <= 916:  # delete fourth item in list
            if pressed and len(page_items) >= 4:
                database.delete_user_game(current_user, page_items[3][0])
                page_items, pages_total = ui.render_user_games(current_user, page, True)

    elif ui.current_page == "USERMOVIES":
        if 680 <= x <= 687 and 350 <= y <= 354:  # back button
            if pressed:
                ui.render_back()
        elif 696 <= x <= 703 and 350 <= y <= 354:  # forward button
            if pressed:
                ui.render_forward()
        elif 724 <= x <= 787 and 336 <= y <= 367:  # books button
            page = 1
            page_items, pages_total = ui.render_books("", page)
        elif 805 <= x <= 867 and 336 <= y <= 367:  # games button
            page = 1
            page_items, pages_total = ui.render_games("", page)
        elif 885 <= x <= 954 and 336 <= y <= 367:  # movies button
            page = 1
            page_items, pages_total = ui.render_movies("", page)
        elif 1556 <= x <= 1643 and 336 <= y <= 367:  # user books button
            page = 1
            page_items, pages_total = ui.render_user_books(current_user, page)
        elif 1661 <= x <= 1747 and 336 <= y <= 367:  # user games button
            page = 1
            page_items, pages_total = ui.render_user_games(current_user, page)
        elif 1745 <= x <= 1750 and 477 <= y <= 484:  # delete first item in list
            if pressed:
                database.delete_user_movie(current_user, page_items[0][0])
                page_items, pages_total = ui.render_user_movies(current_user, page, True)
        elif 1745 <= x <= 1750 and 606 <= y <= 613:  # delete second item in list
            if pressed and len(page_items) >= 2:
                database.delete_user_movie(current_user, page_items[1][0])
                page_items, pages_total = ui.render_user_movies(current_user, page, True)
        elif 1745 <= x <= 1750 and 734 <= y <= 741:  # delete third item in list
            if pressed and len(page_items) >= 3:
                database.delete_user_movie(current_user, page_items[2][0])
                page_items, pages_total = ui.render_user_movies(current_user, page, True)
        elif 1745 <= x <= 1750 and 862 <= y <= 869:  # delete fourth item in list
            if pressed and len(page_items) >= 4:
                database.delete_user_movie(current_user, page_items[3][0])
                page_items, pages_total = ui.render_user_movies(current_user, page, True)


def on_press(key):
    global username, password, search, page, page_items, pages_total

    if ui.current_page == "LOGIN":
        if focused_text_box == "username":
            try:
                username += key.char
            except Exception:
                if key == keyboard.Key.backspace:
                    username = username[:-1]

            ui.render_username(username)
        else:
            try:
                password += key.char
            except Exception:
                if key == keyboard.Key.backspace:
                    password = password[:-1]

            ui.render_password(password)
    elif ui.current_page == "BOOKS":
        if key == keyboard.Key.right:
            if page < pages_total:
                page += 1
                page_items, pages_total = ui.render_books(search, page, pages_total)
        elif key == keyboard.Key.left:
            if page > 1:
                page -= 1
                page_items, pages_total = ui.render_books(search, page, pages_total)
        elif focused_text_box == "search":
            try:
                search += key.char
            except Exception:
                if key == keyboard.Key.backspace:
                    search = search[:-1]
                    ui.render_search(search)
                elif key == keyboard.Key.enter:
                    page = 1
                    page_items, pages_total = ui.render_books(search, page)

            ui.render_search(search)
    elif ui.current_page == "GAMES":
        if key == keyboard.Key.right:
            if page < pages_total:
                page += 1
                page_items, pages_total = ui.render_games(search, page)
        elif key == keyboard.Key.left:
            if page > 1:
                page -= 1
                page_items, pages_total = ui.render_games(search, page)
        elif focused_text_box == "search":
            try:
                search += key.char
            except Exception:
                if key == keyboard.Key.backspace:
                    search = search[:-1]
                    ui.render_search(search)
                elif key == keyboard.Key.enter:
                    page = 1
                    page_items, pages_total = ui.render_games(search, page)

            ui.render_search(search)
    elif ui.current_page == "MOVIES":
        if key == keyboard.Key.right:
            if page < pages_total:
                page += 1
                page_items, pages_total = ui.render_movies(search, page)
        elif key == keyboard.Key.left:
            if page > 1:
                page -= 1
                page_items, pages_total = ui.render_movies(search, page)
        elif focused_text_box == "search":
            try:
                search += key.char
            except Exception:
                if key == keyboard.Key.backspace:
                    search = search[:-1]
                    ui.render_search(search)
                elif key == keyboard.Key.enter:
                    page = 1
                    page_items, pages_total = ui.render_movies(search, page)

            ui.render_search(search)
    elif ui.current_page == "USERBOOKS":
        if key == keyboard.Key.right:
            if page < pages_total:
                page += 1
                page_items, pages_total = ui.render_user_books(current_user, page)
        elif key == keyboard.Key.left:
            if page > 1:
                page -= 1
                page_items, pages_total = ui.render_user_books(current_user, page)
    elif ui.current_page == "USERGAMES":
        if key == keyboard.Key.right:
            if page < pages_total:
                page += 1
                page_items, pages_total = ui.render_user_games(current_user, page)
        elif key == keyboard.Key.left:
            if page > 1:
                page -= 1
                page_items, pages_total = ui.render_user_games(current_user, page)
    elif ui.current_page == "USERMOVIES":
        if key == keyboard.Key.right:
            if page < pages_total:
                page += 1
                page_items, pages_total = ui.render_user_movies(current_user, page)
        elif key == keyboard.Key.left:
            if page > 1:
                page -= 1
                page_items, pages_total = ui.render_user_movies(current_user, page)


if __name__ == '__main__':
    mouse_listener = mouse.Listener(on_click=on_click)
    keyboard_listener = keyboard.Listener(on_press=on_press)

    mouse_listener.start()
    keyboard_listener.start()

    focused_text_box = "username"
    ui.render_login()

    while True:
        ...
