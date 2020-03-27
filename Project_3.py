from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import csv


# Global Variables
# import file path
import_file_path = Path()
# imported csv file
imported_shows = list()
# index to track what show is currently being viewed
current_show_index = 0
# the number of items stored in imported_shows
show_list_len = int()
# True if the current episode has been renamed
episode_renamed = False
# True if a views count has been entered for any episode
views_submitted = False


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
    """
    Increments through the imported shows
    list and returns the dictionary element
    with the most amount of views.

    Rewritten to work with the dictionary list.
    """
    # show_list = list()
    # max_num = 0.0
    # for show in views_list[1:]:
    #     if float(show[-1]) > max_num:
    #         max_num = show[-1]
    #         show_name = show[2]
    #         show_list = [show_name, max_num]
    # return show_list
    HAS_VIEWS = 4
    most_viewed = dict()
    max_num = 0.0
    for show in views_list:
        if len(show) == HAS_VIEWS and show["Views"] > max_num:
            most_viewed = show
            max_num = show["Views"]
    return most_viewed


def get_least_popular(views_list: list) -> dict:
    """
    Increments through the imported shows
    list and returns the dictionary element
    with the least amount of views.

    Rewritten to work with the dictionary list.
    """
    # show_list = [views_list[1][2], views_list[1][-1]]
    # min_num = float(views_list[1][-1])
    # for show in views_list[2:]:
    #     if float(show[-1]) < min_num:
    #         min_num = show[-1]
    #         show_name = show[2]
    #         show_list = [show_name, min_num]
    # return show_list
    HAS_VIEWS = 4
    least_viewed = dict()
    show_index = 0
    # Cycles through the given list until an element with
    # 4 items are found (has a views amount given). Stores
    # the element in least_viewed and then then breaks.
    while show_index < len(views_list):
        if len(views_list[show_index]) == HAS_VIEWS:
            least_viewed = views_list[show_index]
            show_index += 1
            break
        show_index += 1
    # Increment through the remaining list compairing the
    # value of views for each elements with views.
    for show in views_list[show_index:]:
        if len(show) == HAS_VIEWS and show["Views"] < least_viewed["Views"]:
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
    Imports the csv file from the path given
    and returns a list with dictionary format

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


def print_welcome_message() -> None:
    """
    Prints the welcome message to the
    output text box.
    """
    message = (
        "INSTRUCTIONS:\n"
        'Press "Begin" to enter a .csv file to upload\n\n'
        "Enter the number of views for each episode received in millions"
        '(e.g. 1.86 = 1,860,000) an press "Enter"\n\n'
        'To correct the name of an episode. Press the "Rename" button, '
        'enter the corrected name, and press "Enter"\n\n'
        'Press "Next" to proceed to the next episode\n\n'
        'At any time to see the results, press the "Exit List" button\n'
    )
    append_output_text(message)
    output_text.see("1.0")


def append_output_text(message: str) -> None:
    """
    Appends the given string argument
    to the end of the output text box.
    """
    set_output_write_enable()
    # appends the string to the text box
    output_text.insert(END, message)
    # set the scroll bar to the bottom of text box
    output_text.see(END)
    set_output_read_only()


def display_current_show():
    """
    Displays the current show to the
    output text box.
    """
    HAS_VIEWS = 4
    # gets the current episode and stores it to a variable
    show = imported_shows[current_show_index]
    # builds the episode string
    show_output = (
        f"Episode: {show['Episode Name']}\n"
        f"Season: {show['Season']}, Episode: {show['Episode Number']}\n"
    )
    # if the episode has views already entered
    # append the views
    # else, add an empty line
    if len(show) == HAS_VIEWS:
        show_output += f"Views: {str(show['Views'])}\n"
    else:
        show_output += "\n"
    # clear the text box and print the episode to the output text box
    clear_output_text()
    append_output_text(show_output)
    # if episode_renamed equals True, bananacise
    if episode_renamed:
        bananacise()
    # updates the progress label at bottom of GUI
    update_progress_label()


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
    """
    Prints a summary of the most and least
    watched episodes to the output text box.
    """
    # stores the name of the program and author
    program_name = Path(__file__).name
    name = "Tony Samaniego"
    # builds the string to output
    report_string = (
        f"""{program_name}\n"""
        """----------------------\n"""
        f"""{name}\n"""
        """----------------------\n"""
    )
    # If views were entered for any of the episodes,
    # append the results to the output string.
    # Else, append that no views were entered to the output string.
    if views_submitted:
        # gets the most viewed episode
        most_viewed = get_most_popular(imported_shows)
        # gets the least viewed episode
        least_viewed = get_least_popular(imported_shows)
        # gets the average amount of views
        avg_views = average_views(imported_shows)

        most_popular = (
            f"""{most_viewed["Episode Name"]} Season """
            f"""{most_viewed["Season"]} / Episode """
            f"""{most_viewed["Episode Number"]}"""
        )

        least_popular = (
            f"""{least_viewed["Episode Name"]} Season """
            f"""{least_viewed["Season"]} / Episode """
            f"""{least_viewed["Episode Number"]}"""
        )

        more_than = most_viewed["Views"] - avg_views
        less_than = avg_views - least_viewed["Views"]

        report_string += (
            f"""The average number of views for all episodes so far is """
            f"""{avg_views} views. The most popular episode was """
            f"""{most_popular} with {more_than:.2f} more than average. """
            f"""The least popular episode was {least_popular} with """
            f"""{less_than:.2f} less than average\n"""
        )
    else:
        report_string += "No views entered to report\n"
    append_output_text(report_string)


def update_progress_label() -> None:
    """
    Updates the progress label on what
    episode is currently being viewed
    at the bottom of the GUI.
    """
    progress = f"Show {current_show_index + 1} of {show_list_len}"
    progress_label["text"] = progress


# --------------------UI FUNCTIONS------------------------


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


def init_rename_buttons() -> None:
    """
    Sets the button states on the
    GUI for renaming an episode
    """
    remove_widget(enter_views_button)
    insert_widget(enter_name_button)
    disable_button(rename_button)
    disable_button(next_button)
    disable_button(exit_button)
    entry_label["text"] = "New Name:"


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


def get_import_file() -> Path:
    """
    Opens a filedialog window to the
    user to select a file to import.
    Returns a Path to the selected file.
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
        # Gets the headers from the dictionary keys
        keys = get_dictionary_keys()
        writer = csv.DictWriter(out_file, fieldnames=keys)
        # writes the file header
        writer.writeheader()
        # writes the data to the file
        for item in imported_shows:
            writer.writerow(item)


# --------------------SEQUENCE FUNCTIONS-------------------------------


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
        # If not valid, prompt the user
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
    # Gets a default set of keys
    keys = imported_shows[0].keys()
    # if the amount of keys doesn't equal 4
    # search the list for an element with 4 keys
    if len(keys) != MAX_KEYS:
        for item in imported_shows:
            # if an item in the list has 4 elements
            # get a list of its keys an break
            if len(item) == MAX_KEYS:
                keys = item.keys()
                break
    return keys


# --------------------BUTTON FUNCTIONS-------------------------------


def begin_button_press() -> None:
    """
    Begins the episode views sequence once
    the user selects a valid .csv file.
    If an invalid file is selected, user
    is notified on the output text box
    that the file selected was invalid.
    """
    # Gets the path of the csv file to import
    upload_file = get_import_file()
    # Verifies that the file has a .csv suffix
    if upload_file.is_file() and upload_file.suffix == ".csv":
        # Saves the file path to a global variable
        global import_file_path
        import_file_path = upload_file
        # imports the episode list
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
        global views_submitted
        views_submitted = True
    clear_entry_field()


def rename_button_press() -> None:
    """
    Begins the sequence to replace the
    name for the current show
    """
    init_rename_buttons()


def enter_name_button_press():
    """
    Stores the entered name to the show,
    resets the all the UI buttons to
    viewer settings, and bananacises the UI.
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
        global episode_renamed
        episode_renamed = True
        display_current_show()


def next_button_press():
    """
    Increments to the next episode in the
    shows list.
    """
    global episode_renamed
    global current_show_index
    episode_renamed = False
    current_show_index += 1
    # if the last episode was been viewed,
    # end the enter views sequence
    if current_show_index == show_list_len:
        exit_button_press()
    # else, reset the UI buttons and display the next show
    else:
        init_viewer_buttons()
        display_current_show()


def exit_button_press():
    """
    Ends the views entry sequence and
    prints a result summary to the
    output text box.
    """
    # changes the progress label to dispaly "Show Summary"
    progress_label["text"] = "Show Summary"
    # disables all buttons
    disable_views_buttons()
    # prints the views results to the output text box
    clear_output_text()
    print_views_results()
    # exports the modified imported_shows list to a new csv file
    export_shows_list()


# Main GUI Window
root = Tk()
root.title("Lively Earth Studios")
root.iconbitmap("PyCrust.ico")
root.geometry("540x182")
root.resizable(0, 0)

# Widget Items
# Text
content = ttk.Frame(root, padding=(10, 10, 10, 10))
text_frame = Frame(content, relief="groove")
text_scrollbar = Scrollbar(text_frame)
progress_label = ttk.Label(content, text="    ")
entry_label = ttk.Label(content, text="Views")
entry_field = ttk.Entry(content)
output_text = Text(
    text_frame,
    yscrollcommand=text_scrollbar.set,
    width=40,
    height=8,
    font=("Helvetica", 11),
    wrap=(WORD),
    state="disabled",
)
# Buttons
begin_button = ttk.Button(content, text="Begin", command=begin_button_press)
enter_views_button = ttk.Button(
    content, text="Enter", command=enter_views_button_press
)
enter_name_button = ttk.Button(
    content, text="Enter", command=enter_name_button_press
)
rename_button = ttk.Button(content, text="Rename", command=rename_button_press)
next_button = ttk.Button(content, text="Next", command=next_button_press)
exit_button = ttk.Button(content, text="Exit List", command=exit_button_press)
# Photos
banana = PhotoImage(file="bananadance.gif")
small_banana = banana.subsample(2)
banana_label = Label(content, image=small_banana)

# Widget Placement
content.grid(column=0, row=0, sticky=(N, S, E, W))
text_frame.grid(column=0, row=0, columnspan=3, rowspan=5, sticky=(N, S, E, W))
text_scrollbar.grid(row=0, column=1, sticky=(N, S, E))
text_scrollbar.config(command=output_text.yview)
output_text.grid(row=0, column=0, sticky=(N, S, W, E))
progress_label.grid(row=6, column=0, sticky=(N, W))
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
    # initializes and runs the program GUI
    init_ui()
    root.mainloop()


if __name__ == "__main__":
    main()
