import pandas as pd



ChildCharacteristicsTest = pd.DataFrame({'Ethnicity':['WIRI', # 0
                                                  'WBRI', # 1
                                                  'BOTH', # 2
                                                  'MWBC', # 3
                                                  'FAIL' #4, designed to fail the test
                                                  ]})


def rule_4220(df):
    eth_list = [
        "ABAN",
        "AIND",
        "AOTH",
        "APKN",
        "BAFR",
        "BCRB",
        "BOTH",
        "CHNE",
        "MOTH",
        "MWAS",
        "MWBA",
        "MWBC",
        "NOBT",
        "OOTH",
        "REFU",
        "WBRI",
        "WIRI",
        "WIRT",
        "WOTH",
        "WROM",
        ]

    failing_indices = df[~df['Ethnicity'].isin(eth_list)].index

    failing_rows = list(failing_indices)

    return failing_rows

print(rule_4220(df=ChildCharacteristicsTest))

def test_rule_4220():

    ChildCharacteristicsTest = pd.DataFrame({'Ethnicity':['WIRI', # 0
                                                  'WBRI', # 1
                                                  'BOTH', # 2
                                                  'MWBC', # 3
                                                  'FAIL' #4, designed to fail the test
                                                  ]})
    
    result = rule_4220(ChildCharacteristicsTest)

    expected_results = [4]

    assert len(result) == 1
    assert result == expected_results




