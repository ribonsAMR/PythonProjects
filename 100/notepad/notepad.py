
def main():
    try:
        while True:
            filename = input("filename (leave blank to exit): ")
            if not filename:
                raise KeyboardInterrupt

            with open(filename, 'a+') as f:
                content_to_write = ""

                print("Enter text to the file, '-w' to save it, '-c' to cancel: ")  # NOQA

                while True:
                    user_input = input("-> ")

                    if user_input.lower() == "-w":
                        f.write(content_to_write)
                        print("Changes saved.")
                        break

                    if user_input.lower() == "-c":
                        print("Changes canceled.")
                        break

                    content_to_write += user_input + '\n'

            print('File closed.')

    except KeyboardInterrupt:
        print("\nGoodbye! 👋")
        exit(0)


if __name__ == '__main__':
    main()
