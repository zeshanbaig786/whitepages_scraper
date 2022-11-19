import pandas as pd

f = open("..\\links.txt", "w")



state_names_short = ["AL", "AK", "AZ", "AR"]
state_names_long = ["Albama", "Alaska", "Arizona", "Arkansas"]

df1 = pd.read_csv("..\\StateNames.csv")
state_names = df1["Name"].unique()
for state_index, state_name_full in enumerate(state_names_long):
    state_name_short = state_names_short[state_index]
    for name in state_names:
        capitalize_name = name.capitalize()
        for i in range(1,6):                
            link = (f'https://www.whitepages.com/name/{capitalize_name}/{state_name_short}?fs=1&page={i}'
            +f'&searchedLocation={state_name_full}&searchedName={name}')
            f.write(f'{link}\n')    
            print(link)
f.close()