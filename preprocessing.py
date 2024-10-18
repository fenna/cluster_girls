import pandas as pd

columns_to_normalize = ['Mannen_6', 'Vrouwen_7', 'k_0Tot15Jaar_8',
       'k_15Tot25Jaar_9', 'k_25Tot45Jaar_10', 'k_45Tot65Jaar_11',
       'k_65JaarOfOuder_12', 'Ongehuwd_13', 'Gehuwd_14', 'Gescheiden_15',
       'Verweduwd_16', 'WestersTotaal_17', 'NietWestersTotaal_18',
       'Marokko_19', 'NederlandseAntillenEnAruba_20', 'Suriname_21',
       'Turkije_22', 'OverigNietWesters_23', 'GeboorteTotaal_24',
       'SterfteTotaal_26', 'HuishoudensTotaal_28', 'Eenpersoonshuishoudens_29',
       'HuishoudensZonderKinderen_30', 'HuishoudensMetKinderen_31', 'Koopwoningen_40', 'HuurwoningenTotaal_41',
       'InBezitWoningcorporatie_42', 'InBezitOverigeVerhuurders_43',
       'EigendomOnbekend_44', 'BouwjaarVoor2000_45', 'BouwjaarVanaf2000_46', 'Appartement_48',
       'Tussenwoning_49', 'Hoekwoning_50', 'TweeOnderEenKapWoning_51',
       'VrijstaandeWoning_52', 'Huurwoning_53', 'EigenWoning_54','Appartement_56',
       'Tussenwoning_57', 'Hoekwoning_58', 'TweeOnderEenKapWoning_59',
       'VrijstaandeWoning_60', 'Huurwoning_61', 'EigenWoning_62', 'OpleidingsniveauLaag_64',
       'OpleidingsniveauMiddelbaar_65', 'OpleidingsniveauHoog_66',
       'Nettoarbeidsparticipatie_67', 'k_40PersonenMetLaagsteInkomen_73',
       'k_20PersonenMetHoogsteInkomen_74', 'k_40HuishoudensMetLaagsteInkomen_76',
       'k_20HuishoudensMetHoogsteInkomen_77',
       'HuishoudensMetEenLaagInkomen_78', 'HuishOnderOfRondSociaalMinimum_79',
       'HuishoudensTot110VanSociaalMinimum_80',
       'HuishoudensTot120VanSociaalMinimum_81', 'PersonenPerSoortUitkeringBijstand_83',
       'PersonenPerSoortUitkeringAO_84', 'PersonenPerSoortUitkeringWW_85',
       'PersonenPerSoortUitkeringAOW_86', 'JongerenMetJeugdzorgInNatura_87', 'WmoClienten_89']



def normalize_columns(df, columns_to_normalize, divisor_column):
    """Normalize specified columns by a divisor column and multiply by 100."""
    df[columns_to_normalize] = df[columns_to_normalize].div(df[divisor_column], axis=0) * 100
    return df

def filter_columns_by_non_null_percentage(df, threshold=0.25):
    """Filter columns with less than the specified threshold of non-null values."""
    non_null_percentages = df.notnull().mean()
    columns_to_drop = non_null_percentages[non_null_percentages < threshold].index
    return df.drop(columns=columns_to_drop), columns_to_drop

def fill_na_with_value(df, column, value=0):
    """Fill NaN values in a specific column with a specified value."""
    df[column] = df[column].fillna(value)
    return df

def drop_rows_with_many_nans(df, nan_threshold=0.5):
    """Drop rows with more than a specified percentage of NaN values."""
    df = df.dropna(thresh=df.shape[1] * (1 - nan_threshold))
    return df

def remove_columns(df, columns_to_remove):
    """Remove specified columns from the DataFrame."""
    df = df.drop(columns=columns_to_remove, inplace=False)
    return df

def process_regions(df, region_type, index_column='Codering_3', drop_column='SoortRegio_2'):
    """Process regions by filtering, setting index, and dropping columns."""
    region_df = df[df['SoortRegio_2'].str.contains(region_type)]
    region_df.set_index(index_column, inplace=True)
    region_df.drop(columns=[drop_column], inplace=True)
    return region_df

# Main processing pipeline

def process_file(df, columns_to_normalize=columns_to_normalize):


    #typecasting
    df['IndelingswijzigingGemeenteWijkBuurt_4'] = df['IndelingswijzigingGemeenteWijkBuurt_4'].astype(str).str.replace('.', '0', regex=False)
    df['IndelingswijzigingGemeenteWijkBuurt_4'] = pd.to_numeric(df['IndelingswijzigingGemeenteWijkBuurt_4'])

    # Normalize specified columns by 'AantalInwoners_5'
    columns_to_normalize = columns_to_normalize 
    divisor_column = 'AantalInwoners_5'
    df = normalize_columns(df, columns_to_normalize, divisor_column)

    # Fill NaN values in 'PercentageWoningenMetStadsverwarming_63' with 0
    df = fill_na_with_value(df, 'PercentageWoningenMetStadsverwarming_63', value=0)

    # Drop columns with less than 25% non-null values
    df, columns_dropped = filter_columns_by_non_null_percentage(df, threshold=0.25)
    print(f"Columns dropped due to too few non-null values: {columns_dropped}")

    # Drop rows with more than 50% NaN values
    df = drop_rows_with_many_nans(df, nan_threshold=0.5)

    # Fill remaining NaN values with 0
    df.fillna(0, inplace=True)

    # Remove unnecessary columns
    columns_to_remove = ['ID', 'WijkenEnBuurten', 'Gemeentenaam_1', 'MeestVoorkomendePostcode_114']
    df = remove_columns(df, columns_to_remove)

    # Process 'Wijken' and 'Buurten'
    wijken = process_regions(df, region_type='Wijk')
    buurten = process_regions(df, region_type='Buurt')

    return wijken, buurten


def main():
    df = pd.read_excel("Kerncijfers.xlsx")
    wijken, buurten = process_file(df)
    wijken.to_csv('wijken.csv')
    buurten.to_csv('buurten.csv')

if __name__ == "__main__":
    main()


