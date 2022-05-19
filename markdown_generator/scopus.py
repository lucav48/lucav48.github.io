import pandas as pd


def authors(x):
    aut = x.split("|")
    new_aut = []
    for a in aut:
        cog, nom = a.split(", ")
        new_aut.append(nom + " " + cog)
    return ", ".join(new_aut)


def institutions(x):
    ins = x.split("|")
    new_ins = []
    for i in ins:
        new_ins.append(i.replace("Marche Polytechnic University", "Polytechnic University of Marche"))
    return ",".join(new_ins)


pub = pd.read_csv("scopus.csv")
pub["Authors"] = pub["Authors"].apply(lambda x: authors(x))
pub["Institutions"] = pub["Institutions"].apply(lambda x: institutions(x))
pub = pub.rename(columns={"Scopus Source title": "Journal"})

for _, p in pub.iterrows():
    filename = p["Full date"] + "-" + p["Journal"] + ".md"
    f = open("../_publications/" + filename, "w")
    f.write("---\n")
    f.write("title: '" + p["Title"].replace("'", "").replace("–", "-") + "'\n")
    f.write("collection: publications\n")
    f.write("permalink: /publication/" + filename + "\n")
    f.write("excerpt: '" + p["Authors"] + "'\n")
    f.write("date: " + p["Full date"] + "\n")
    f.write("venue: '" + p["Journal"] + "'\n")
    f.write("link: 'https://doi.org/" + p["DOI"] + "'\n")
    f.write("location: '" + p["Institutions"] + "'\n")
    f.write("---")