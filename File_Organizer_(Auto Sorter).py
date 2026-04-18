import os
import shutil

# mapping folder berdasarkan ekstensi
FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".mkv", ".avi"],
    "documents": [".pdf", ".docx", ".txt"],
    "music": [".mp3", ".wav"],
    "archives": [".zip", ".rar"]
}

def organize_folder(path):
    if not os.path.exists(path):
        print("Folder tidak ditemukan!")
        return

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()

            moved = False

            for folder, extensions in FILE_TYPES.items():
                if ext in extensions:
                    target_folder = os.path.join(path, folder)

                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, file))

                    print(f"{file} → {folder}/")
                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(path, "others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"{file} → others/")

def main():
    path = input("Masukkan path folder: ")
    organize_folder(path)
    print("\nSelesai! File sudah dirapikan 📂")

if __name__ == "__main__":
    main()