import sys
import pathlib

def main():
    file_name = pathlib.Path(sys.argv[1])
    print(file_name.absolute())
    
    
    
if __name__ == "__main__":
    main()