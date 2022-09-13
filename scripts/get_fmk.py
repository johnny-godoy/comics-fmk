def filter_characters(editorial=None, gender=None):
    """Filters the characters according to editorial and a list of genders
    Accepted editorials: DC, Marvel
    Accepted genders: F, M, NA, FLUID, T"""
    filtered_characters = reduced_characters.copy()
    if editorial is not None:
        filtered_characters = reduced_characters[reduced_characters.editorial.str.lower() == editorial.lower()]
        filtered_characters = filtered_characters.drop("editorial", axis=1)
    if gender is not None:
        if not isinstance(gender, list):
            gender = [gender]
        filtered_characters = filtered_characters[filtered_characters.SEX.str.lower().isin(map(str.lower, gender))]
        if len(gender) == 1:
            filtered_characters = filtered_characters.drop("SEX", axis=1)
    return filtered_characters


def get_fmk(editorial=None, gender=None):
    """Returns a DataFrame with 3 characters, filtered by editorial and gender (see filter_characters)."""
    return filter_characters(editorial, gender).sample(3)


if __name__ == "__main__":
    import pandas as pd

    reduced_characters = pd.read_csv("../data/processed/simple-data.csv")

    # Choosing an editorial
    editorial = input("Please input an editorial (Marvel, DC, or press enter if you don't with to filter by editorial): ").lower()
    while editorial not in ("", "marvel", "dc"):
        print(f"Editorial {editorial} is not valid. Try Marvel or DC")
        editorial = input("Please input an editorial (Marvel, DC, or press enter if you don't with to filter by editorial): ").lower()
    if editorial == "":
        editorial = None

    # Choosing genders
    print("Valid genders: F (female), M (male), T (transgender), NA (no gender), FLUID (genderfluid)")
    print("Input the genders you wish to include, one by one. When you are done, press Enter without including a gender")
    print("if you don't with to filter by gender, just press Enter")
    valid_genders = {"f", "m", "t", "na", "fluid"}
    genders = []
    gender = input("Please input a valid gender: ").lower()
    if gender not in valid_genders:
        print(f"Invalid gender {gender} ignored.")
    elif gender != "":
        genders.append(gender)
    while gender != "":
        gender = input("Please input a valid gender (Enter to stop input): ").lower()
        if gender not in valid_genders:
            print(f"Invalid gender {gender} ignored.")
        elif gender != "":
            genders.append(gender)
    genders = list(set(genders)) if len(genders) > 0 else None
    print(f"You chose the following genders to filter by: {genders}")
    print("Choose who to f*ck, who to marry, and who to kill!:")
    print(get_fmk(editorial, genders))
