
prefix = "myprefix/"
id = "ABC-123"
word = "Hello World"

def hyphenate(word):
    return prefix + id + '-' + word.lower().replace(" ", "-")

print(hyphenate("Hello World")) # hello-world