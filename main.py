import requests
from bs4 import BeautifulSoup

res1 = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
# print(res.text)
soup1 = BeautifulSoup(res1.text,"html.parser")
soup2 = BeautifulSoup(res2.text,"html.parser")

titles1 = soup1.find_all("tr",class_="athing")
titles2 = soup2.find_all("tr",class_="athing")

# votes = soup.find_all("td",class_="subtext").find_all("span",class_="subline")

votes1 = soup1.select(".subtext")
votes2 = soup1.select(".subtext")

t_titles = titles1+titles2
t_votes = votes1+votes2

def sort_data(data):
    return sorted(data,key=lambda k:k['votes'],reverse=True)

def clean_data(titles,votes):
    data = []
    for i,item in enumerate(titles):

        title = titles[i].find("span",class_="titleline").find('a').text

        link = titles[i].find("span",class_="titleline").find('a').get("href",None)
        # print(link)

        vote = votes[i].select(".score")

        if len(vote)>0:
            
            points = int(vote[0].getText().replace(" points",""))

            if points>99:
                data.append({"title":title,"link":link,"votes":points})
                

    return sort_data(data)

# print(clean_data(t_titles,t_votes))
# print(len(clean_data(t_titles,t_votes)))
# clean_data(t_titles,t_votes)

def show_data(data):
    print("*************************************************************************************************")
    print("*                                         TOP NESWS                                             *")
    print("*************************************************************************************************")
    for d in data:
        title,link,votes = d.values()
        print(f"Head Line: \"{title}\"\nLink: {link}\nVotes: {votes}")
        print("*************************************************************************************************")

show_data(clean_data(t_titles,t_votes))




