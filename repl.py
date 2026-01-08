import os
import shutil

TARGET_EXTENSIONS = (".html", ".js", ".css")

def replace_word_in_file(file_path, old_word, new_word, backup=True):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if old_word not in content:
        return

    if backup:
        shutil.copy(file_path, file_path + ".bak")

    content = content.replace(old_word, new_word)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[REPLACED] {file_path}")


def replace_word_in_folder(root_dir, old_word, new_word, backup=True):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(TARGET_EXTENSIONS):
                file_path = os.path.join(root, file)
                replace_word_in_file(file_path, old_word, new_word, backup)


if __name__ == "__main__":
    folder = input("대상 폴더 경로: ").strip()
    old_word = input("바꿀 단어: ").strip()
    new_word = input("새 단어: ").strip()

    replace_word_in_folder(folder, old_word, new_word, backup=True)
    print("✅ 치환 완료")
