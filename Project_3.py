from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import csv


# Global Variables
imported_shows = list()
current_show_index = 0
show_list_len = int()

# --------------------ORIGINAL CODE------------------------

# def get_user_path() -> Path:
#     prompt = "Enter in a Path to import: "
#     while True:
#         user_path = input(prompt)
#         user_path = Path(user_path)
#         try:
#             assert user_path.exists() == True, "get_user_path() - File does not exist"
#         except:
#             print("That is not a valid Path")
#         else:
#             break
#     return user_path


# def user_view_input(show_list: list) -> list:
#     # views_list = list(["Season", "Episode Number","Episode Name"])
#     views_list = list()
#     views_list.append(show_list[0])
#     prompt = (
#         "Enter the number of views in millions of views\n"
#         'Example: enter "1.86" for 1,860,000.\n'
#     )
#     print(prompt)
#     for row in show_list[1:]:
#         season_num = row[0]
#         episode_num = row[1]
#         name = row[2]
#         while True:
#             views = input(
#                 f"Enter the number of view for {name}, "
#                 + f"episode {episode_num}, season {season_num}: "
#             )

#             try:
#                 views = float(views)
#             except:
#                 print("Please enter a number of views\n")
#             else:
#                 break
#         cont = input("Continue: ").lower()
#         views_list.append([season_num, episode_num, name, views])
#         if cont == "no":
#             break

#     return views_list


def average_views(views_list: list) -> int:
    sum = float()
    show_count = 0
    for show in views_list[1:]:
        sum += show[-1]
        show_count += 1
    try:
        average = sum / show_count
    except:
        average = 0
    return round(average)


def get_most_popular(views_list: list) -> list:
    show_list = list()
    max_num = 0.0
    # length = len(views_list)
    for show in views_list[1:]:
        # if int(show[-1]) > max_num:
        if float(show[-1]) > max_num:
            max_num = show[-1]
            show_name = show[2]
            show_list = [show_name, max_num]
    return show_list


def get_least_popular(views_list: list) -> list:
    show_list = [views_list[1][2], views_list[1][-1]]
    min_num = float(views_list[1][-1])
    for show in views_list[2:]:
        # if int(show[-1]) < min_num:
        if float(show[-1]) < min_num:
            min_num = show[-1]
            show_name = show[2]
            show_list = [show_name, min_num]
    return show_list


def create_export_file(in_file: Path, views_list: list) -> Path:
    file_extension = Path("_views.csv")
    out_file = in_file.stem / file_extension
    with open(out_file, "w") as new_file:
        for line in views_list:
            season_num = line[0]
            episode_num = line[1]
            name = line[2]
            views = line[3]
            new_string = f"{season_num},{episode_num},{name},{views}"
            new_file.write(new_string)
    return out_file


def import_file(import_file: Path) -> list:
    """
    Imports the .csv path to the imported 
    shows list

    Rewritten to import with a csv.DictReader
    and to store the file to a global list
    """
    # show_list = list()
    # with open(import_file, "r") as in_file:
    #     for line in in_file:
    #         show_data = line.split(",")
    #         show_list.append(show_data)
    # return show_list
    csv_in = list()
    with open(import_file, newline="") as in_file:
        reader = csv.DictReader(in_file)
        for line in reader:
            csv_in.append(line)
    return csv_in


# def views_calculator():
#     in_file = get_user_path()
#     show_list = import_file(in_file)
#     views_list = user_view_input(show_list)

#     most_viewed = get_most_popular(views_list)
#     least_viewed = get_least_popular(views_list)
#     average = average_views(views_list)

#     more_views = int(most_viewed[-1]) - average
#     less_views = average - int(least_viewed[-1])

#     print(f"{most_viewed[0]} had {more_views} million more views than average")
#     print(f"{least_viewed[0]} had {less_views} million less views than average")

# --------------------END OF ORIGINAL CODE------------------------


# --------------------WIGET FUNCTIONS------------------------
def ___WIGET___():
    pass


def enable_button(button: Button) -> None:
    """Enables a state of a button"""
    button["state"] = "normal"


def disable_button(button: Button) -> None:
    """Disables the state of a button"""
    button["state"] = "disabled"


def remove_button(button: Button) -> None:
    """Removes a button from the GUI"""
    button.grid_remove()


def insert_button(button: Button) -> None:
    """
    Reinserts a button to the GUI
    Button has to be removed by button.remove()
    and not button.forget().
    """
    button.grid()


def set_output_write_enable() -> None:
    """
    Sets the output Text box to
    write enable
    """
    output_text["state"] = "normal"


def set_output_read_only() -> None:
    """
    Sets the output Text box to
    read-only
    """
    output_text["state"] = "disabled"


# --------------------TEXT BOX / ENTRY FUNCTIONS------------------------


def ___TEXT_BOX___():
    pass


def print_welcome_message() -> None:
    """
    Prints the welcome message to the
    output text box.
    """
    set_output_write_enable()
    message = 'Press "Begin" to enter a .csv file to upload\n'
    output_text.insert(END, message)
    set_output_read_only()


def append_output_text(message: str) -> None:
    """
    Appends the given string argument
    to the end of the output text box.
    """
    set_output_write_enable()
    output_text.insert(END, message)
    set_output_read_only()


def display_current_show():
    """
    Displays the current show to the 
    output text box. 
    """
    show = imported_shows[current_show_index]
    show_output = (
        f"Episode: {show['Episode Name']}\n"
        f"Season: {show['Season']}, Episode: {show['Episode Number']}\n"
    )
    append_output_text(show_output)


def clear_output_text() -> None:
    """
    Clears the output text box
    """
    set_output_write_enable()
    output_text.delete(1.0, END)
    set_output_read_only()


def clear_entry_field() -> None:
    """Clears the text entry filed"""
    entry_field.delete(0, "end")


# --------------------UI FUNCTIONS------------------------
def ___UI___():
    pass


def init_ui() -> None:
    """
    Initializes the GUI to it's initial
    program begin settings.
    """
    print_welcome_message()
    remove_button(enter_button)
    remove_button(rename_button)
    remove_button(next_button)
    remove_button(exit_button)
    remove_button(banana_label)
    remove_button(submit_name_button)
    insert_button(begin_button)


def init_viewer_buttons() -> None:
    """
    Sets the button states on the
    GUI for a shows views input.
    """
    remove_button(begin_button)
    remove_button(banana_label)
    insert_button(enter_button)
    insert_button(next_button)
    insert_button(exit_button)
    insert_button(rename_button)


# --------------------IMPORT / EXPORT FUNCTIONS------------------------
def ___IMPORT___():
    pass


def get_import_file() -> Path:
    """
    Returns a Path to the selected file
    by the user. Opens a filedialog 
    window to the user to select a file 
    to import.
    """
    return Path(filedialog.askopenfilename())


def import_csv_file(import_path: Path) -> None:
    """
    Imports the given path to imported_shows
    list and sets the show_list_len to the
    imported number of items imported.
    """
    global imported_shows
    global show_list_len
    imported_shows = import_file(import_path)
    show_list_len = len(imported_shows)


# --------------------SEQUENCE FUNCTIONS-------------------------------
def ___SEQUENCE___():
    pass


def init_shows_viewer() -> None:
    """
    Clears all text fields, initializes
    all buttons, and displays the current
    show for views entry.
    """
    # Clears all text fields
    clear_output_text()
    clear_entry_field()

    if show_list_len > 0:
        # Initializes GUI buttons
        init_viewer_buttons()
        # displays the current show to the output text
        display_current_show()
    else:
        empty_file = "Imported file has no shows saved.\n"
        append_output_text(empty_file)
        print_welcome_message()


# --------------------BUTTON FUNCTIONS-------------------------------
def ___BUTTON___():
    pass


def begin_user_view_entry():
    """
    Begins the shows views sequence once
    the user selects a valid .csv file.
    If an invalid file is selected, user
    is notified on the output text box
    that the file selected was invalid.
    """
    # Gets the path of the csv file to import
    upload_file = get_import_file()
    # Verifies that the file has a .csv suffix
    if upload_file.is_file() and upload_file.suffix == ".csv":
        # imports the shows list
        import_csv_file(upload_file)
        # initializes the GUI for entering shows viewings
        init_shows_viewer()
    # If the file was not a valid .csv file,
    # notify the user.
    elif upload_file.is_file():
        message = "Invalid file type.\n"
        append_output_text(message)


def submit_text_entry():
    rename_button["state"] = "disabled"  # Test Code


def submit_new_name():
    # Test Code
    enable_button(next_button)
    exit_button["state"] = "normal"
    enter_button.grid()
    submit_name_button.grid_remove()
    banana_label.grid()


def next_show():
    # Test Code
    rename_button["state"] = "normal"
    banana_label.grid_remove()


def exit_list():
    pass


def rename_show():
    """

    """
    # Test Code
    remove_button(enter_button)
    insert_button(submit_name_button)
    disable_button(next_button)
    disable_button(exit_button)


# Main Window
root = Tk()
root.title("Lively Earth Studios")
root.iconbitmap("PyCrust.ico")
# Grid Layout
content = ttk.Frame(root, padding=(10, 10, 10, 10))
text_frame = Frame(content, relief="groove")
text_scrollbar = Scrollbar(text_frame)
entry_label = ttk.Label(content, text="Views")
entry_field = ttk.Entry(content)
output_text = Text(
    text_frame,
    yscrollcommand=text_scrollbar.set,
    width=35,
    height=8,
    font=("Helvetica", 12),
    wrap=(WORD),
    state="disabled",
)
# Buttons
begin_button = ttk.Button(content, text="Begin", command=begin_user_view_entry)
enter_button = ttk.Button(content, text="Enter1", command=submit_text_entry)
submit_name_button = ttk.Button(content, text="Enter2", command=submit_new_name)
rename_button = ttk.Button(content, text="Rename", command=rename_show)
next_button = ttk.Button(content, text="Next", command=next_show)
exit_button = ttk.Button(content, text="Exit List", command=exit_list)
# Photos
banana = PhotoImage(file="bananadance.gif")
small_banana = banana.subsample(2)
banana_label = Label(content, image=small_banana)
# Wiget Placement
content.grid(column=0, row=0, sticky=(N, S, E, W))
text_frame.grid(column=0, row=0, columnspan=3, rowspan=5, sticky=(N, S, E, W))
text_scrollbar.grid(row=0, column=1, sticky=(N, S, E))
text_scrollbar.config(command=output_text.yview)
output_text.grid(row=0, column=0, sticky=(N, S, W, E))
entry_label.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx=5)
entry_field.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), padx=5)
begin_button.grid(column=3, row=2, padx=5, pady=3, sticky=(N))
enter_button.grid(column=3, row=2, padx=5, pady=3)
submit_name_button.grid(column=3, row=2, padx=5, pady=3)
rename_button.grid(column=4, row=2, padx=5)
next_button.grid(column=3, row=3, padx=5, pady=6)
exit_button.grid(column=3, row=4, padx=5, pady=3)
banana_label.grid(column=4, row=3, rowspan=3)
# GUI Formatting
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=1)
content.columnconfigure(2, weight=1)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)


def main():
    init_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
