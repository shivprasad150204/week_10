# wiki.py
import wikipedia

def main():
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, autosuggest=False)
            print(f"\n{page.title}\n{page.summary}\n{page.url}\n")
        except wikipedia.DisambiguationError as e:
            print(f"\nWe need a more specific title. Try one of the following, or a new search:\n{e.options}\n")
        except wikipedia.PageError:
            print(f"\nPage id \"{title}\" does not match any pages. Try another id!\n")

if __name__ == "__main__":
    main()
