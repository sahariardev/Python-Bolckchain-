blockchain=[];
def get_last_block_chain_value():
    return blockchain[-1]
def add_value(transaction_amount,lasttransactionamount=[10]):
    blockchain.append([lasttransactionamount,transaction_amount])
def get_user_input():
    u_input = float(input('Enter value: '))
    return u_input        
def print_chain():
    print("-----blockchain------")
    print(blockchain)
user_input = get_user_input()
add_value(user_input)
add_value(get_user_input(),get_last_block_chain_value())
print_chain()