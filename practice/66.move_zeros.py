"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Input: nums = [0]
Output: [0]

"""        
def move_zeroes(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """









print(move_zeroes(nums = [0,1,0,3,12])) # [1,3,12,0,0]
print(move_zeroes(nums = [0])) # [0]


""" 
    read pointer(탐색): 칠판 왼->오른쪽으로 글자를 읽는 사람 (for loop element)
    write pointer(대기): 필요없는거 지우고, 새 글자를 적을 빈 자리에 멈춰 기다리는 사람 
    snowball effect: 0이 아닌 숫자가 들어올 다음 자리 인덱스 관리 (즉 현재 0이 있는 자리),
                    지금까지 발견된 0들의 시작점, 0 이 밀려와서 대기 타고 있는 자리 

    1. read pointer가 0이 아닌 숫자를 만나면, write pointer가 가리키는 위치에 그 숫자를 쓴다.
    2. write pointer를 오른쪽으로 한 칸 이동한다.
    3. read pointer는 배열의 끝까지 계속 이동한다.
    4. read pointer가 배열의 끝에 도달하면, write pointer부터 배열의 끝까지 0을 채운다.

    메모리 공간 안쓰고 기존 배열 안에서 (자원 내에서) 최적화 기본기 
    예시) 장바구니에서 유저가 품절 상품을 일괄 삭제했다. 남은 상품을 빈칸없이 앞으로 당겨서 화면에 보여달라. 메모리 부족하니 리스트 새로 만들지 마세요.
         로그에서 정상 로그는 앞에 두고 오류 로그는 맨 뒤로 몰아서 보여달라. 메모리 부족하니 리스트 새로 만들지 말라. 
"""