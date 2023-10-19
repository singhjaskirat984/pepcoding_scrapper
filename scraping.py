from bs4 import BeautifulSoup
import requests

lvl1_html = requests.get('https://www.pepcoding.com/resources/online-java-foundation').text
soup = BeautifulSoup(lvl1_html, 'lxml')
# print(soup)
categories = soup.find_all('li', class_ = 'collection-item row list-item')

categoryName = []
categoryRoute = []

for c in categories :
    categoryName.append(c.find('span', class_ = 'no-padding col l10 s9 m10 push-s1 no-margin').text.replace(' ', '').replace('\r\n', ''))
    categoryRoute.append(c.find('a', href=True))


# print(categoryName)
# print(categoryRoute)

# for a in categoryRoute:
#     print(a['href'])

lvl1 = {}
i = 0

while i<len(categoryRoute):
    insideCategoryHtml = requests.get('https://www.pepcoding.com' + categoryRoute[i]['href']).text
    # print(insideCategoryHtml)
    soup2 = BeautifulSoup(insideCategoryHtml, 'lxml')
    # print(soup2)
    questions = soup2.find_all('div', class_='col l12 s12 l-desc-icon')
    # print(questions)
    questionsRouteList = []
    for q in questions:
        questionsRouteList.append(q.find('a', href=True))
        # questionsName.append(q.find('span' , class_ = 'name').text.replace(' ', '').replace('\r\n', ''))

    questionsName = []
    questionsVideo = []

    for q in questionsRouteList:
        insideQuestion = requests.get('https://www.pepcoding.com' + q['href']).text
        soup3 = BeautifulSoup(insideQuestion, 'lxml')
        eachQuestionname = soup3.find('div', class_='col l10 s12')
        # print(eachQuestionname)
        if(eachQuestionname is not None):
            questionsName.append(eachQuestionname.text)
        # removeEmpties = [ele for ele in eachQuestionname if ele != []]
        # for e in removeEmpties:
        #     print(e.text)
        eachVideoUrl = soup3.find('iframe')
        if(eachVideoUrl is not None):
            questionsVideo.append(eachVideoUrl.attrs['src'])

    res = dict(zip(questionsName, questionsVideo))
    # print(res)
    lvl1[categoryName[i]] = res
    i += 1
    print(i)

print(lvl1)
# print(questionsName)
# print(questionsVideo)

