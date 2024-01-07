def organize_into_profits_losses(lst):
    # variables
    organized_lst = []
    subsequent_weeks = []
    num = 0

    # for-loop
    for index in range(len(lst)):
        if lst[num] > 0:
            if lst[index] > 0:
                subsequent_weeks.append(lst[index])
                print(num)
            elif lst[index] < 0:
                organized_lst.append(list(subsequent_weeks))
                subsequent_weeks.clear()
                subsequent_weeks.append(lst[index])
                num = index
        elif lst[num] < 0:
            if lst[index] < 0:
                subsequent_weeks.append(lst[index])
            elif lst[index > 0]:
                organized_lst.append(list(subsequent_weeks))
                subsequent_weeks.clear()
                subsequent_weeks.append(lst[index])
                num = index

    # return
    return organized_lst
        
def spending_statistics(lst_lsts):
    # variables
    loss_period = 0
    profit_period = 0
    total_balance = 0

    # for-loop
    for period in lst_lsts:
        # for-loop
        for idx in range(len(period)):
            # conditional
            if idx < (len(period) - 1):
                # codnitonals
                if period[idx] < period[idx + 1]:
                    print(idx)
                    profit_period += 1

                elif period[idx] > period[idx - 1]:
                    loss_period += 1
            
            elif idx == (len(period) - 1):
                pass

            # adjust variable
            total_balance += period[idx]

    # final prints
    print(f"You've had {profit_period} period(s) of subsequent profit.")
    print(f"You've had {loss_period} period(s) of subsequent loss(es)")
    print(f"Total balance: {total_balance}")
    
    # conditionals
    if total_balance <= 0:
        print("Try harder!")
    else:
        print("You're doing great! Keep it up!")

def main():
    weeks_lst = [1, 4, -2, 3, -3, -5, 3]
    organized_weeks_lst = organize_into_profits_losses(weeks_lst)
    print("Here are your spending habits over the last few weeks:", organized_weeks_lst)
    spending_statistics(organized_weeks_lst)

main()
