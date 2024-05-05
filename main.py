import json


def load_data():
  try:
    with open('youtube.txt', 'r') as file:
      test = json.load(file)
      return test
  except FileNotFoundError:
    return []


def save_data_helper(videos):
  with open('youtube.txt', 'w') as file:
    json.dump(videos, file)


def list_all_videos(videos):
  print("\n")
  print("*" * 70)
  for index, video in enumerate(videos, start=1):
    print(f"{index}. {video['name']}, Duration: {video['time']}")


def add_video(videos):
  name = input("Enter the video name: ")
  while not name.strip():
    print("Video name cannot be empty.")
    name = input("Enter the video name: ")
  time = input("Enter the video time: ")
  videos.append({"name": name, "time": time})
  save_data_helper(videos)
  print("Video added successfully!")


def update_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to update: ")) - 1
  if 0 <= index < len(videos):
    name = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[index] = {"name": name, "time": time}
    save_data_helper(videos)
  else:
    print("Invalid video number.")


def delete_video(videos):
  list_all_videos(videos)
  index = int(input("Enter the video number to delete: ")) - 1
  if 0 <= index < len(videos):
    del videos[index]
    save_data_helper(videos)
  else:
    print("Invalid video number.")


def main():
  videos = load_data()
  while True:
    print("\n Youtube Manager | Choose an option")
    print("1. List all Youtube videos")
    print("2. Upload a new video")
    print("3. Update a youtube video details")
    print("4. Delete a youtube video")
    print("5. Exit")
    choice = input("Enter your choice: ")

    match choice:
      case "1":
        list_all_videos(videos)
      case "2":
        add_video(videos)
      case "3":
        update_video(videos)
      case "4":
        delete_video(videos)
      case "5":
        print("Exiting...")
        break
      case _:
        print("Invalid choice. Please try again.")


if __name__ == "__main__":
  main()
