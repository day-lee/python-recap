https://leetcode.com/problems/recyclable-and-low-fat-products

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    condition = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products.loc[condition, ['product_id']]
    # df.loc[조건식, [선택열]]
