import pandas as pd
from pandas.testing import assert_frame_equal

def test_df_equality():
    df1 = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    df2 = pd.DataFrame({"A": [1, 2], "B": [3, 5]})

    print(df1)
    print(df2)

    # assert df1 == df2
    assert_frame_equal(df1, df2)
