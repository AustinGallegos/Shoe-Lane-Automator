def write_output(logins, path="results/eligible.txt"):
    """Write a list of login values to a text file"""
    with open(path, "w") as file:
        for login in logins:
            file.write(f"{login}\n")