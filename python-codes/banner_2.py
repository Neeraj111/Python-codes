def banner_text(text: str =  " ", screen_width: int = 80): #function with default value
                                          #no need to write the argument

    if len(text) > screen_width - 4:
        print("EEK !!")
        print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*"*screen_width)
    else:
        centerd_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centerd_text)
        print(output_string)        


banner_text("*")
banner_text("always look on the bright side of the light")
banner_text("always look on the bright side of the light")
banner_text("always look on the bright side of the light")
banner_text("always look on the bright side of the light")
banner_text()
banner_text("always look on the bright side of the light")
banner_text("always look on the bright side of the light")
banner_text("*")

result = banner_text("abcd")
print(result)