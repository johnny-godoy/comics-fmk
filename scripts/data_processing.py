import pandas as pd

if __name__ == "__main__":
    # Loading dataframes
    dc_characters = pd.read_csv("../data/raw/dc-wikia-data.csv")
    marvel_characters = pd.read_csv("../data/raw/marvel-wikia-data.csv").rename(columns = {'Year': 'YEAR'})

    # Adding the editorial
    dc_characters["editorial"] = "DC"
    marvel_characters["editorial"] = "Marvel"

    # Fixing the urls
    dc_characters["url"] = "https://dc.fandom.com" + dc_characters.urlslug.str[7:]
    marvel_characters["url"] = "https://marvel.fandom.com/wiki" + marvel_characters.urlslug.str[1:]

    # Contatenating columns, replacing genders.
    characters = pd.concat((dc_characters, marvel_characters))
    characters.SEX.replace({"Male Characters": "M", "Female Characters": "F",
                            "Transgender Characters": "T", "Agender Characters": "NA",
                            "Genderless Characters": "NA", "Genderfluid Characters": "FLUID"}, inplace=True)
    characters.SEX.fillna("NA", inplace=True)
    characters.reset_index(drop=True, inplace=True)

    # Saving the data
    characters.to_csv("../data/processed/joint-data.csv")

    # Simplifying the data
    reduced_data = characters[["name", "url", "SEX", "editorial"]]
    reduced_data.to_csv("../data/processed/simple-data.csv")
    print("done")
