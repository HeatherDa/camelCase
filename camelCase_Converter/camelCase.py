def camelCase(sentance):
    error = False
    forbidden=['and','as','assert','break','class','continue','def','del','elif','else','except','exec','finally','for','from','global','if','import','in','is','lambda','nonlocal','not','or','pass','raise','return','try','while','with','yield','True','False','None']

    if sentance not in forbidden:

        words=sentance.split(" ")

        camelCase=""

        for i in words:
            if okay(i):
                if i==words[0]:
                    if i[0].isdigit():
                        raise SyntaxError("python variable names cannot start with a number.")
                    else:
                        i=words[0].lower()
                        camelCase=camelCase+i
                else:
                    i=i.capitalize()
                    camelCase=camelCase+i
            else:
                raise SyntaxError("python variable names cannot contain special characters (except for '_')")

        return camelCase #good so far
    else:
        raise SyntaxError("That is a keyword and cannot be used as a variable name.")

def okay(word):
    #Only numbers, letters, and underscores are okay
    w=""
    for char in word:
        if char.isalnum():
            w=w+char
        elif char=='_':
            w=w+char
        else:
            return False
    if len(w)==len(word):
        return True
    else:
        return False

def main():
    sentance = input("Write a sentance or phrase to convert to camelCase.")
    camelCase(sentance)

#main()
