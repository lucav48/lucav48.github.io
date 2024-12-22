import os

import pandas as pd


def authors(x):
    aut = x.split(", ")
    new_aut = []
    for a in aut:
        parts = a.split(" ")
        new_aut.append(parts[-1] + " " + " ".join(parts[:-1]))
    return ", ".join(new_aut)


def institutions(x):
    ins = x.split(";")
    new_ins = []
    for i in ins:
        i = i.replace("\xa0", "")
        new_ins.append(i.replace("Marche Polytechnic University", "Polytechnic University of Marche"))
    return ",".join(new_ins)


pub = pd.read_csv("scopus.csv")
pub["Authors"] = pub["Authors"].apply(lambda x: authors(x))
pub["Institutions"] = pub["Affiliations"].apply(lambda x: institutions(x))
pub["Institutions"] = pub["Institutions"].apply(lambda x: x.replace("“", "").replace("”", "")
                                                .replace("'", " ").replace("“", ""))
pub["Institutions"] = pub["Institutions"].apply(lambda x: x.replace("à", "a").replace('"', '')
                                                .replace("'", " ").replace("”", "").replace("’", " "))
pub = pub.rename(columns={"Scopus Source title": "Journal"})

for i, p in pub.iterrows():
    print(i)
    filename = str(p["Year"]) + "-" + p["Source title"] + "-" + "-".join(p["Title"].replace(":", "").split(" ")[:2]) + ".md"
    if filename not in os.listdir("../_publications/") and "Correction" not in p["Title"]:
        print(p["Institutions"])
        f = open("../_publications/" + filename, "w")
        f.write("---\n")
        f.write("title: '" + p["Title"].replace("'", "").replace("–", "-") + "'\n")
        f.write("collection: publications\n")
        f.write("permalink: /publication/" + filename + "\n")
        f.write("excerpt: '" + p["Authors"] + "'\n")
        f.write("date: " + str(p["Year"]) + "-01-01\n")
        f.write("venue: '" + p["Source title"] + "'\n")
        if type(p["DOI"]) == str:
            f.write("link: 'https://doi.org/" + p["DOI"] + "'\n")
        f.write("location: '" + p["Institutions"] + "'\n")
        f.write("---")
        f.close()