import pandas as pd

df = pd. read_csv("E:/python/nasa data/confirmed_planets.csv",comment = '#')

df1 = df.loc[:,['pl_name', 'hostname', 'discoverymethod',
        'disc_year', 'disc_facility','pl_orbper','pl_bmasse','st_teff','st_mass','sy_dist','pl_rade']].copy()

df1=df1.rename(columns={'pl_name':'planet name','hostname':'host star',
            'pl_orbper':'orbital period','pl_bmasse':'mass(earth mass)',
            'st_teff':'star temp(k)','sy_dist':'distance(ps)',
            'pl_rade':'radius(earth)', 'st_mass':'star mass'})
df1.duplicated().sum()

df1 = df1.drop_duplicates(subset=['planet name'])
df1 = df1.reset_index(drop=True)
df1 = df1.dropna(subset=['mass(earth mass)','radius(earth)'])
df1= df1.sort_values('distance(ps)',ascending=True)

df1.to_csv('cleaned_exoplanet_data2.csv',index = False)
df1.to_excel('cleaned_exoplanet_data2.xlsx',index = False, sheet_name='Cleaned Data')