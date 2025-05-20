def write_into_file(data, file_path):
  with open(file_path, "w") as file:
    file.write("\n".join(data))


def read_from_file(file_path):
  with open(file_path, "r") as file:
    data = file.readlines()
    cleaned_data = [name.replace("\n", "") for name in data]
  return cleaned_data


if __name__ == "__main__":
  names = ["Ed", "Al", "Hughes", "Riza", "Roy"]
  path = "names.txt"
  write_into_file(names, path)
  print(f"Names written to file {path}")

  print(f"Reading contents of file {path}")
  file_contents = read_from_file(path)
  print(names)
  print(file_contents)
  assert file_contents == names
