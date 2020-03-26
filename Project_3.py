from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import csv


# Global Variables
import_file_path = Path()
imported_shows = list()
current_show_index = 0
show_list_len = int()
banana_state = False


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
    """
    Returns the average views for the
    shows that have been given view counts.

    Modified the summing to be able to work
    with the dictionary format.
    """
    sum = float()
    show_count = 0
    for show in views_list:
        if len(show) == 4:
            # sum += show[-1]
            sum += show["Views"]
            show_count += 1
    try:
        average = sum / show_count
    except:
        average = 0
    return round(average)


def get_most_popular(views_list: list) -> dict:
    # show_list = list()
    # max_num = 0.0
    # for show in views_list[1:]:
    #     if float(show[-1]) > max_num:
    #         max_num = show[-1]
    #         show_name = show[2]
    #         show_list = [show_name, max_num]
    # return show_list
    most_viewed = dict()
    max_num = 0.0
    for show in views_list:
        if len(show) == 4 and show["Views"] > max_num:
            most_viewed = show
            max_num = show["Views"]
    return most_viewed


def get_least_popular(views_list: list) -> dict:
    # show_list = [views_list[1][2], views_list[1][-1]]
    # min_num = float(views_list[1][-1])
    # for show in views_list[2:]:
    #     if float(show[-1]) < min_num:
    #         min_num = show[-1]
    #         show_name = show[2]
    #         show_list = [show_name, min_num]
    # return show_list
    least_viewed = dict()
    show_index = 0
    while show_index < len(views_list):
        if len(views_list[show_index]) == 4:
            least_viewed = views_list[show_index]
            show_index += 1
            break
        show_index += 1
    for show in views_list[show_index:]:
        if len(show) == 4 and show["Views"] < least_viewed["Views"]:
            least_viewed = show
    return least_viewed


# def create_export_file(in_file: Path, views_list: list) -> Path:
#     file_extension = Path("_views.csv")
#     out_file = in_file.stem / file_extension
#     with open(out_file, "w") as new_file:
#         for line in views_list:
#             season_num = line[0]
#             episode_num = line[1]
#             name = line[2]
#             views = line[3]
#             new_string = f"{season_num},{episode_num},{name},{views}"
#             new_file.write(new_string)
#     return out_file


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


# --------------------WIDGET FUNCTIONS------------------------
def ___WIDGET___():
    pass


def enable_button(button: Button) -> None:
    """Enables a state of a button"""
    button["state"] = "normal"


def disable_button(button: Button) -> None:
    """Disables the state of a button"""
    button["state"] = "disabled"


def remove_widget(widget: Widget) -> None:
    """Removes a widget from the GUI"""
    widget.grid_remove()


def insert_widget(widget: Widget) -> None:
    """
    Reinserts a widget to the GUI.
    Widget has to be removed by widget.remove()
    and not widget.forget().
    """
    widget.grid()


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
    output_text.see(END)
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
    if len(show) == 4:
        show_output += f"Views: {str(show['Views'])}\n"
    else:
        show_output += "\n"
    clear_output_text()
    append_output_text(show_output)
    if banana_state:
        bananacise()


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


def print_views_results() -> None:
    most_viewed = get_most_popular(imported_shows)
    least_viewed = get_least_popular(imported_shows)
    avg_views = average_views(imported_shows)

    program_name = Path(__file__).name
    name = "Tony Samaniego"

    most_name = most_viewed["Episode Name"]
    most_season = most_viewed["Season"]
    most_episode = most_viewed["Episode Number"]
    most_popular = f"{most_name} Season {most_season} / Episode {most_episode}"

    least_name = least_viewed["Episode Name"]
    least_season = least_viewed["Season"]
    least_episode = least_viewed["Episode Number"]
    least_popular = f"{least_name} Season {least_season} / Episode {least_episode}"

    more_than = most_viewed["Views"] - avg_views
    less_than = avg_views - least_viewed["Views"]

    report_string = (
        f"{program_name}\n"
        f"------------------\n"
        f"{name}\n"
        "------------------\n"
        f"The average number of views for all episodes so far is {avg_views} views. The most popular episode was {most_popular} with {more_than:.1f} more than average. The least popular episode was {least_popular} with {less_than:.1f} less than average"
    )
    append_output_text(report_string)


# --------------------UI FUNCTIONS------------------------
def ___UI___():
    pass


def init_ui() -> None:
    """
    Initializes the GUI to it's initial
    program begin settings.
    """
    print_welcome_message()
    remove_widget(enter_views_button)
    remove_widget(rename_button)
    remove_widget(next_button)
    remove_widget(exit_button)
    remove_widget(banana_label)
    remove_widget(enter_name_button)
    insert_widget(begin_button)


def init_viewer_buttons() -> None:
    """
    Sets the button states on the
    GUI for a shows views input.
    """
    remove_widget(begin_button)
    remove_widget(banana_label)
    insert_widget(enter_views_button)
    insert_widget(next_button)
    insert_widget(exit_button)
    insert_widget(rename_button)


def reset_viewer_buttons() -> None:
    """
    Resets all the UI controls to
    enter show views
    """
    enable_button(next_button)
    enable_button(exit_button)
    enable_button(rename_button)
    remove_widget(enter_name_button)
    remove_widget(banana_label)
    insert_widget(enter_views_button)


def disable_views_buttons() -> None:
    """
    Disables all views buttons
    """
    disable_button(enter_views_button)
    disable_button(rename_button)
    disable_button(next_button)
    disable_button(exit_button)


def bananacise() -> None:
    """bananacise"""
    insert_widget(banana_label)
    append_output_text('"BANANA"\n')


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


def export_shows_list() -> None:
    """
    Exports the updated imported shows list
    to the program file directory. The file 
    name will have the same name as the file
    imported with "_views" added to the file
    name.
    """
    # builds the export file name
    file_name = import_file_path.stem
    file_tag = "_views"
    file_type = import_file_path.suffix
    export_file = file_name + file_tag + file_type
    # creates the file and uploads the data to it in csv format
    with open(export_file, "w", newline="") as out_file:
        # Gets the header from the dictionary keys
        keys = get_dictionary_keys()
        writer = csv.DictWriter(out_file, fieldnames=keys)
        # writes the file header
        writer.writeheader()
        # writes the data to the file
        for item in imported_shows:
            writer.writerow(item)


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
    # If the file was empty, notify the user
    else:
        empty_file = "Imported file has no shows saved.\n"
        append_output_text(empty_file)
        print_welcome_message()


def get_view_count() -> float:
    """
    Returns the number of views entered into
    the text entry field. If invalid entry,
    returns -1.
    """
    try:
        view_cnt = entry_field.get()
        # Verifies that the given input is a valid float
        view_cnt = float(view_cnt)
        if view_cnt < 0:
            raise Exception
    except:
        # If not valid, user is prompted
        append_output_text(f'Error - Invalid Entry "{view_cnt}"\n')
        view_cnt = -1
    return view_cnt


def store_view_count(count: float) -> None:
    """
    Stores the given number of views 
    to the current show. number of views
    is stored with a dictionary key of
    'Views'
    """
    imported_shows[current_show_index]["Views"] = count


def get_dictionary_keys() -> list:
    """
    Returns a list of the keys for the
    imported shows list. Checks the list
    for the correct number of keys by 
    cycles through and verifying that "Views"
    should be included with the list of 
    keys.
    """
    MAX_KEYS = 4
    # Gets the default 3 set of keys
    keys = imported_shows[0].keys()
    for item in imported_shows:
        # if an item in the list has 4 elements
        if len(item) == MAX_KEYS:
            # get a list of its keys an break
            keys = item.keys()
            break
    return keys


# --------------------BUTTON FUNCTIONS-------------------------------
def ___BUTTON___():
    pass


def begin_button_press() -> None:
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
        # Saves the file path as a global variable
        global import_file_path
        import_file_path = upload_file
        # imports the shows list
        import_csv_file(import_file_path)
        # initializes the GUI for entering shows viewings
        init_shows_viewer()
    # If the file was not a valid .csv file,
    # notify the user.
    elif upload_file.is_file():
        message = "Invalid file type.\n"
        append_output_text(message)


def enter_views_button_press() -> None:
    """
    Gets the number of views entered by
    the user in the entry field and stores
    the value in the current show list index.
    """
    # Gets the view count form user
    view_cnt = get_view_count()
    # If the entered value is valid, store the
    # value and display it to the output text box.
    if view_cnt != -1:
        store_view_count(view_cnt)
        display_current_show()
    clear_entry_field()


def rename_button_press() -> None:
    """
    Begins the sequence to replace the
    name for the current show
    """
    # initializes the UI buttons and labels
    remove_widget(enter_views_button)
    insert_widget(enter_name_button)
    disable_button(rename_button)
    disable_button(next_button)
    disable_button(exit_button)
    entry_label["text"] = "New Name:"


def enter_name_button_press():
    """
    Stores the entered name to the show,
    resets the all the UI buttons to 
    viewer settings, and bananacise the UI.
    """
    # Gets the new name from the entry field
    new_name = entry_field.get()
    clear_entry_field()
    # Verifies that a new name was entered
    if len(new_name) > 0:
        # Resets the UI
        reset_viewer_buttons()
        remove_widget(enter_name_button)
        entry_label["text"] = "Views"
        # Stores the new name to the shows list and
        # replaces the old name with the new name in
        # the output text box
        imported_shows[current_show_index]["Episode Name"] = new_name
        # displays banana
        global banana_state
        banana_state = True
        display_current_show()


def next_button_press():
    """
    Increments to the next show in the 
    shows list. 
    """
    global banana_state
    global current_show_index
    banana_state = False
    current_show_index += 1
    if current_show_index == show_list_len:
        exit_button_press()
    else:
        init_viewer_buttons()
        display_current_show()


def exit_button_press():
    """ """
    disable_views_buttons()
    clear_output_text()
    print_views_results()
    export_shows_list()


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
begin_button = ttk.Button(content, text="Begin", command=begin_button_press)
enter_views_button = ttk.Button(
    content, text="Enter1", command=enter_views_button_press
)
enter_name_button = ttk.Button(content, text="Enter2", command=enter_name_button_press)
rename_button = ttk.Button(content, text="Rename", command=rename_button_press)
next_button = ttk.Button(content, text="Next", command=next_button_press)
exit_button = ttk.Button(content, text="Exit List", command=exit_button_press)
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
enter_views_button.grid(column=3, row=2, padx=5, pady=3)
enter_name_button.grid(column=3, row=2, padx=5, pady=3)
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
