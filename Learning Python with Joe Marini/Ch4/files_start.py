#
# Read and write files using the built-in Python file methods
#


def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open("textfile.txt", "w")

    # Open the file for appending text to the end
    f = open("textfile.txt", "w")

    # write some lines of data to the file
    for i in range(5):
        string = f'{str(i)}, {str(i**2)} \n'
        f.write(string)
        
    # close the file when done
    f.close()

    with open("textfile.txt") as f:
        # text_all = f.read()
        # text_line = f.readline()
        # text_lines = f.readlines()
        # print('All', text_all)
        print('All / line / lines', text_line)
        

        
    # # Open the file back up and read the contents
    # f = open('textfile.txt')
    # txt = f.read()
    # f.close()
    # print(txt)

if __name__ == "__main__":
    main()
