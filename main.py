"""
Group Members: # Dan To & Amelia Doe & H Grasso.
"""

# DO NOT CHANGE OR REMOVE THE FOLLOWING LINES
import interaction
import screen
# DO NOT CHANGE OR REMOVE THE PRECEDING LINES


def main():
    """
    Starting point for the whole game. Called automatically when script is run.
    """
    interaction.do_load_default_game()
    while True:
        screen.clear_screen()
        screen.draw_screen(interaction.last_message)
        interaction.last_message = ""

        user_input = interaction.get_user_command()
        should_continue = interaction.do_command(user_input)
        if not should_continue:
            break
        # TODOish: If should_continue is False then exit this loop. Don't exit the whole program, just this loop.
    screen.write_new_line()
    screen.write('Thank you for playing. Goodbye.')


if __name__ == '__main__':
    main()
