from quotes import get_quote


def main():
    quote = get_quote()
    
    print(quote.message)
    print(quote.author)


if __name__ == "__main__":
    main()
