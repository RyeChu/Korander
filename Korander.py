import pickle
import os
import time
from Player import Player


def main():

	#load previous files
	save_folder = get_folder_path()
	player_save_file = get_save_path(save_folder, "char_save")
	items_save_file = get_save_path(save_folder, "item_save")

	user_name = "ryan"
	user_level = 100

	user_character = Player(user_name, user_level)

	print(user_character.get_name())
	print(user_character.get_level())

	user_character.set_name("bob")
	user_character.set_level(50)

	print("saving game")
	save_game(player_save_file, user_character)
	print("loading game")
	load_game(player_save_file, user_character)

	print(user_character.get_name())
	print(user_character.get_level())



	#intro
	#game loop
	pass


def game_loop():
	pass


def save_game(save_file, obj):
	with open(save_file, 'wb') as fout:
		pickle.dump(obj, fout, -1)


def load_game(save_file, obj):
	with open(save_file, 'rb') as fout:
		obj = pickle.load(fout)


def get_save_path(folder_path, folder_name):
	filesave = os.path.join(folder_path, folder_name + ".dat")
	return filesave


def get_folder_path():
	folder_name = "game_saves"
	current_path = os.path.dirname(__file__)
	full_path = os.path.join(current_path, folder_name)

	if not os.path.exists(full_path) or not os.path.isdir(full_path):
		print("Creating new {} folder at {}".format(folder_name, full_path))
		os.mkdir(full_path)

	return full_path


def delete_game(save_file):
	os.remove(save_file)



	save_game(save_file, obj)



if __name__ == "__main__":
	main()