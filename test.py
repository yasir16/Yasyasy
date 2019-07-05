import re
import urllib.request
import mistune
from bs4 import BeautifulSoup
checkbox = re.compile("[\[]\s?[\]]")
def aw():


    global change4

    url = urllib.request
    link = "https://raw.githubusercontent.com/onlyphantom/sqlalchemy-tutorial/master/quiz.md"

    f = url.urlopen(link)
    myfile = f.read()
    # print(myfile)
    myfile1 = myfile.decode("utf-8")
    myfile2 = mistune.markdown(myfile1)

    soup = BeautifulSoup(myfile2, "html.parser")

    questions = []
    listitems = []
    lis = []
    for ol in soup.findAll("ol"):
        for quest in ol.findAll("li", recursive=False):
            print(f"question: {quest.find('p')}")
            print("----")
            print(f"choices: {quest.find('ul')}")
            print("----")
            x = list(quest.find("ul").li)
            print(x)
            matching = [s for s in x if "points" in s]
            print("this is : %s" %matching)
    return questions, listitems 


    # change = myfile2.replace("<ol><li>", "<ol><li>")
    # change1 = myfile2.replace("<ul>", "<select>") #.replace("<li>", "<option>").replace("<ol>\n<option>","<ol>\n<li>").replace("</ul>\n</li>", "</select></li>").replace("</li>", "</option>").replace("</select></option>", "</select>\n</li>").replace("</li>\n<option>", "</li>\n<li>")
    # change2 = change1.replace("<li>", "<option>")
    # change = change2.replace("<ol>\n<option>","<ol>\n<li>").replace("</ul>\n</li>", "</select></li>").replace("</li>", "</option>")
    # change3 = change.replace("</select></option>", "</select>\n</li>")
    # change4 = change3.replace("</li>\n<option>", "</li>\n<li>")
    # # print(change4)
    # print(change1)


# def test():
#     aw()
#     # print(change4)
    
#     soup = BeautifulSoup(change4, "html.parser")

#     questions = []
#     listitems = []
#     lis = []
#     for ol in soup.findAll("ol"):
#         for quest in ol.findAll("li", recursive=False):
#             print(f"question: {quest.find('p')}")
#             print("----")
#             print(f"choices: {quest.find('ul')}")
#             print("----")
#             x = list(quest.find("ul").li)
#     return questions, listitems, x

q, l = aw()
print(q)
print(l)
# print(x)
    # # print(soup.blockquote)
    # # print(soup)
    # question = []
    # listitems = []
    # for ol in soup.find_all("ol"):
    #     # print (ol)
    #     lis = ol.find_all("li")
    #     print(lis)
    #     req = re.compile("[")

    #     # if lis.find(re.compile("[")):
    #     #     break
    #     question.append(lis) 
    #     uls = ol.findAll("ul")
    #     for ul in uls:
    #         listitems.append(ul.findAll("li"))
    # print(listitems)
    # print(len(listitems))
    # print(question)
    # return question, listitems
    # print(question)
        # print(lis.find())
        # if lis.find(re.compile("[")):
        #     break
        # questions += lis
    #     uls = ol.findAll("ul")
    #     for ul in uls:
    #         listitemst += ul.findAll("li")
    # print(listitems)

    # for ol in soup.find_all("ol"):
    #     lis = ol.find_all("li")
    #     if lis.find(re.compile("[")):
    #         break
    #     questions += lis
    #     uls = ol.find_all("ul")
    #     for ul in uls:
    #         listitems += ul.find_all("li")
    # print(listitems)
    # print(len(listitems))
    # return questions, listitems

    # reg = re.compile("")

    # for x in range (0,9):

    # black = change4.split("<blockquote><p>",1)[1]
    # quote = black.split("</p>\n</blockquote>",1)[0]
    # a1 = change4.split("<li><p>",1)[1]
    # b1 = a1.split("</p>",1)[0]
    # select = change4.split("<select>",1)[1]
    # option = select.split("</select>",1)[0]
    # option = option.replace("<option>[ ]", "").replace("</option>", "").replace("<option>", "")
    
    # print(quote)
    # print(b1)
    # print(option)


# import re

# regex = re.compile(r"^.*interfaceOpDataFile.*$", re.IGNORECASE)
# for line in some_file:
#     line = regex.sub("interfaceOpDataFile %s" % fileIn, line)

    # instruction = change4.split("<blockquote><p>",1)[1]
    # question = instruction.split("<li><p>",1)[1]
    # select = question.split("<select>",1)[1]
    
    # a = {}
    # b = {}
    # c = {}
    # # k = 1

    # for k in range(0,1)  :
    #     a[k] = instruction.split("</p>\n</blockquote>",1)[0]
    #     print(a[k]) #instruction printed

    #     b[k] = question.split("</p>",1)[0]
    #     print(b[k]) #question printed
    #     # c[k] = select.split("</select>",1)[1]
    #     # # c[k] = c[k].replace("<option>[ ]", "").replace("</option>","")

    #     # # c[k+1] = c[]
    #     # print (c[k])

    
 


    

    # pro = re.sub(r"[]]+[]"," ", change4)
    # change5 = change4.replace("<option>[ ]", "<option>")
    # print(change4)
    # a = change4.split("<li>",1)[1]
    # b = a.split("</li>",1)[0]
    # print (b)

    # a = {}
    # k = 0
    # while k < 10:    
    #     a[k] = ""
    #     a[4] = 213
    #     k += 1

    # print(a[4])

    # a = {}
    # b = {}
    # k = 1
    # count = change4.count("<li>")
    # print (count)

    # do {
    #     a[count] =
    # } while(count == 0)

    # while k < count:
    #     a[k] = change4.split("<li><p>",1)[1]
    #     b[k] = a[k].split("</p>",1)[0]

    #     print(b[k])

    # print(change4)
    
   
    

    # a2 = a1.split("<li><p>",1)[1]
    # b2 = a2.split("</p>",1)[0]
    # print (b2)

    # a3 = a2.split("<li><p>",1)[1]
    # b3 = a3.split("</p>",1)[0]
    # print(b3)

    # a4 = a3.split("<li><p>",1)[1]
    # b4 = a4.split("</p>",1)[0]
    # print(b4)

    # a5 = a4.split("<li><p>",1)[1]
    # b5 = a5.split("</p>",1)[0]
    # print(b5)

    # a6 = a5.split("<li><p>",1)[1]
    # b6 = a6.split("</p>",1)[0]
    # print(b6)

    # a7 = a6.split("<li><p>",1)[1]
    # b7 = a7.split("</p>",1)[0]
    # print(b7)
    



    # a8 = a7.split("<li><p>",1)[1]
    # b8 = a8.split("</p>",1)[0]
    # print(b8)


    # count = change4.count("<li>")





# aw = myfile2
# # aw1 = "ul" in myfile2
# print (aw)
# if aw1 == True:
#     aw = myfile2.replace("ul", "select")
#     aw2 = aw.replace("li", "option")



# print(aw2)


# s1 = "hello python world, i'm a beginner "
# s2 = "world,"

# print(s1.index(s2))

# def linearSearch(item,my_list):
#     found = False
#     position = 0
#     while position < len(my_list) and not found:
#         if my_list[position] == item:
#             found = True
#         position = position + 1
#     return found

# bag = ['book','pencil','pen','note book','sharpener','rubber']
# item = input('What item do you want to check for in the bag?')
# itemFound = linearSearch(item,bag)
# if itemFound:
#     print ('Yes, the item is in the bag')
# else:
#     print ('Oops, your item seems not to be in the bag')


# txt = "Hello, welcome to my world."

# x = txt.find("welcome",0, 10)

# print(x)


# text = "H3 foo barH3 H3baz H3 quH3ux"
# text.replace("H3","H1")
# print(text)


# s = 'shak#spea#e'
# c = '#'
# print([pos for pos, char in enumerate(s) if char == c])


# word = 'geeks for geeks'
# # aw = "fuck" in word

# print(aw)

# Use slicing to extract those parts of the original string to be kept
# s = s[:position] + replacement + s[position+length_of_replaced:]

# Example: replace 'sat' with 'slept'
# text = "The cat sat on the mat"
# text = text[:8] + "slept" + text[11:]



# import re

# line = "Cats are smarter than dogs"

# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")


# variables = {}
# variables["first"] = 34
# variables["second"] = 45
# print(variables["first"], variables["second"])

# # using namedtuple
# Variables = namedtuple('Variables', ['first', 'second'])
# vars = Variables(34, 45)
# print(vars.first, vars.second)


