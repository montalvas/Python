from account import Account

acc1 = Account('123-4', 'Lucas', 100)
acc1.get_info_account()

acc2 = Account('123-5', 'Adriana')
acc2.get_info_account()

acc3 = Account('221-5', 'Miguel', 500)
acc3.get_info_account()

print(F"\nTotal of registered accounts: {Account.get_total_accounts()}")