from pathlib import Path

#question 1
def add_path():
   current = Path.cwd()
   print(current)
   new_path = Path(current)/'files'/'data.txt'
   print(new_path)
   print(Path.home())
add_path()

#question 2
file_path = Path('notes.txt')
if file_path.exists():
    print("The file exists.")
else:
    file_path.write_text("This is a new file created by pathlib.")
print(file_path.read_text())