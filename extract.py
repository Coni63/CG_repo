import requests
import json
from pprint import pprint
from fake_useragent import UserAgent
import pandas as pd
import ast
from tabulate import tabulate
from pprint import pprint
import os

def extract_code(testSessionHandle, language="Python3"):
    data = [testSessionHandle, language]
    r = requests.post('https://www.codingame.com/services/TestSession/getPreviousCodeByLanguageId', cookies=cookies, data = str(data))
    code = json.loads(r.text)
    return code
    
def to_cat(x):
    pts = {
        "medium" : 2,
        "hard" : 3,
        "easy" : 1,
        "expert" : 4,
        "multi" : 7,
        "optim" : 6,
        "codegolf" : 5,
        "tutorial" : 0
    }
    return pts[x]

def to_emojis(x):
    if x==100:
        return ":heavy_check_mark:"  
    elif x>0: 
        return ":white_check_mark:" 
    else: 
        return ""
    
def compute_total(x):
    json_data = ast.literal_eval(x)
    return sum(json_data["feedbacks"])

def compute_average(x):
    json_data = ast.literal_eval(x)
    total = 0
    for pts, vote in zip([1, 2, 3, 4, 5], json_data["feedbacks"]):
        total += pts * vote
    return total / sum(json_data["feedbacks"])   

ua = UserAgent().chrome

cookie_key = input("cgSession :")
n_puzzle = int(input("Number of puzzles :"))

print("Get puzzle data")

full_data = [list(range(1, n_puzzle)), 270881,1]
r = requests.post('https://www.codingame.com/services/Puzzle/findProgressByIds',  data = str(full_data))

pd.DataFrame(json.loads(r.text)).to_csv("results_raw.csv", index=False)

df = pd.read_csv("results_raw.csv", encoding = "ISO-8859-1")

df['creationTime'] = pd.to_datetime(df['creationTime']*1000000)
df['lastActivity'] = pd.to_datetime(df['lastActivity']*1000000)
       
df["feedbackAvg"] = df["feedback"].apply(compute_average)
df["feedbackCount"] = df["feedback"].apply(compute_total)

df.drop(["chatRoom", "codinGamer", "contributor", 
         "coverBinaryId", "forumLink", "league", 
         "logoBinaryId", "openChallenge", "optimCriteria", 
         "optimCriteriaId", "optimPoints", "prettyId", 
         "previewBinaryId", "puzzleLeaderboardId", "rank", 
         "replayIds", "score", "thumbnailBinaryId",
         "topics", "feedback"], axis=1, inplace=True)  # "testSessionHandle"

df = df.set_index("id")
df = df.sort_index()

df.to_csv("results.csv")

print("Building README.md")

df = pd.read_csv("results.csv", encoding = "ISO-8859-1", index_col=0)

df["base"] = "https://www.codingame.com"
df["url"] = df["base"].str.cat(df["detailsPageUrl"])
df["percentDone"] = df.solvedCount / df.attemptCount

df["url"] = df["url"].apply(lambda x:"[Link]({})".format(x))
df["diff"] = df["level"].apply(to_cat)
df["Done"] = df["validatorScore"].apply(to_emojis)

df = df.sort_values(["diff", "validatorScore"], ascending=[True, False])

sub = df[["title", "level", "Done", "url"]]
sub = sub.set_index("title")
txt = tabulate(sub, tablefmt="pipe", headers="keys")

with open("README.md", "w") as f:
    f.write(txt)

print("Download of last puzzle done")
	
cookies = {"cgSession":cookie_key}

for row in df.iterrows():
    testSessionHandle = row[1]["testSessionHandle"]
    validatorScore = row[1]["validatorScore"]
    level = row[1]["level"]
    root, folder, title = row[1]["detailsPageUrl"][1:].split("/")
    title = title.replace(":", "")
    if validatorScore == 0:
        continue
    extension = {
        "Python3" : "py",
        "Javascript" : "js",
    }
    language = "Python3"
    filename = "{}/{}/{}.{}".format(root, folder, title, extension[language])
    if os.path.isfile(filename):
        continue
    if not os.path.exists("{}/{}".format(root, folder)):
        os.makedirs("{}/{}".format(root, folder))
    print("Extracting {} : {}".format(testSessionHandle, filename))
    code = extract_code(testSessionHandle, language=language)
    if code is None:
        continue
    with open(filename, "w") as f : 
        f.write(code)