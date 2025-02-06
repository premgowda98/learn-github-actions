import os


def sample():
    name_input = os.getenv("INPUT_NAME", None)
    print("Recieved input from workflow: ", name_input)
    with open(os.getenv("GITHUB_OUTPUT"), "a") as f:
        f.write("output-from-container=hello")

if __name__ == "__main__":
    sample()