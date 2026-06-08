'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

'''

'''
그리디: 바로 눈 앞의 최선의 선택을 함 
가장 큰 순서대로, 가장 작은 순서대로, 정렬 한 후에 순서대로, 접근하는 문제에서 자주 쓰임 

미리 이익을 계산한 뒤 비교해가며 업데이트해 나감
min(), max() 비교
'''

def max_profit(prices:list[int])-> int:
    # no or one data in the list, can't calculate
    if len(prices) <= 1:
        return 0

    min_price = prices[0]
    max_profit = 0 

    for price in prices:
        # min_price = min(min_price, price) 
        # current_profit = price - min_price 
        # max_profit = max(current_profit, max_profit)  

        # same comparing logic with if statement 
        if price < min_price:
            min_price = price 
        else:
            current_profit = price - min_price 
            if max_profit < current_profit:
                max_profit = current_profit  

    return max_profit     


print(max_profit([1, 2, 4])) # 3
print(max_profit([7, 2, 3, 1])) # 1 
print(max_profit([7,6,4,3,1])) # 0 





