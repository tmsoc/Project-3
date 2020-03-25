from pathlib import Path
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import csv

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
    show_list = list()
    with open(import_file, "r") as in_file:
        for line in in_file:
            show_data = line.split(",")
            show_list.append(show_data)
    return show_list


# def views_calculator():
#     in_file = get_user_path()
#     show_list = import_file(in_file)
#     views_list = user_view_input(show_list)

#     most_viewed = get_most_popular(views_list)
#     least_viewed = get_least_popular(views_list)
#     average = average_views(views_list)

#     ##    print(views_list[1][-1])
#     ##    print(type(views_list[1][-1]))

#     more_views = int(most_viewed[-1]) - average
#     less_views = average - int(least_viewed[-1])

#     print(f"{most_viewed[0]} had {more_views} million more views than average")
#     print(f"{least_viewed[0]} had {less_views} million less views than average")

# --------------------END OF ORIGINAL CODE------------------------


def main():
    pass


if __name__ == "__main__":
    main()
