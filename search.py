import sys
import webbrowser

"""googleCLIsearch is a quick way to perform a Google search while coding without the need to manually open a browser 
to search. """

GOOGLE_MAIN = "https://www.google.com/search?q="
GOOGLE_IMAGE = "https://images.google.com/search?q="
GOOGLE_MAPS = "https://maps.google.com/search?q="


def main():
    if len(sys.argv) < 1:  # if len(sys.argv) is < 1, then there was no input, so quit
        sys.quit()
    else:
        query = "+".join(sys.argv[1:])
        if "image" in query:
            webbrowser.open(GOOGLE_IMAGE + query)
        if "map" in query:
            webbrowser.open(GOOGLE_MAPS + query)
        else:
            webbrowser.open(GOOGLE_MAIN + query)


if __name__ == "__main__":
    main()
