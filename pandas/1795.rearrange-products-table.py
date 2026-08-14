https://leetcode.com/problems/rearrange-products-table

- 2890의 pd.melt() 문서 참고
- value_vars 인자를 따로 지정하지 않으면 "id_var" 지정 열 제외하고 모두 변환 대상으로 잡는다.
- 1번 자동 인식하게되면 컬럼이 늘어나도 유연하게 대처할 수 있다. 명시성은 떨어짐  
- 2번 하드 코딩으로 명시적 지정하면 안정성, 가독성이 있다


Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output: 
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+


-- 1번
- value_vars 생략 

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = products.melt(
    id_vars=['product_id'],
    var_name='store',
    value_name='price'
    )
    result.dropna(subset=['price'], inplace=True)
    return result


-- 2번
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    result = pd.melt(
    products, 
    id_vars='product_id', 
    value_vars=['store1', 'store2', 'store3'], 
    var_name='store', 
    value_name='price')

    return result.dropna(subset='price')
