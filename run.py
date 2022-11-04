__author__ = "Shivam Shekhar"

from src.game import intro_screen, db

made_by = "Let`s-git-it"


def main():
    db.init_db()
    is_game_quit = intro_screen()
    if not is_game_quit:
        intro_screen()


if __name__ == "__main__":
    main()
