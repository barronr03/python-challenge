import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")
# Open the CSV file and read the contents
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    next(csv_reader)

# Store variables
    acum_profit_losses = []
    rowcount = 0
    total = 0
    prev_profit_loss= 0
    profit_loss_change = 0
    profit_loss_changes = []
    dates=[]
    # Iterate over the rows in the CSV file
    for row in csv_reader:
        date=row[0]
        profit_loss = int(row[1])
        acum_profit_losses.append(int(row[1]))
        dates.append(date)
        # Set the "profit/loss" changes 
        if rowcount>0:
            profit_loss_change += profit_loss - prev_profit_loss
            profit_loss_changes.append(profit_loss - prev_profit_loss)
        prev_profit_loss = profit_loss
        rowcount+=1

    profit_losses_sum = sum(acum_profit_losses)
    rowcount= len(acum_profit_losses)
# Set max and mins "profit/loss"
    max_change = max(profit_loss_changes)
    max_change_index=profit_loss_changes.index(max_change)
    max_change_date = dates[max_change_index+1]

    min_change = min(profit_loss_changes)
    min_change_index=profit_loss_changes.index(min_change)
    min_change_date = dates[min_change_index +1]

# Print the results
    print ("Financial Analysis")
    print('-------------------------------')
    print (f'Total Months:  {rowcount}')
    print (f'Total: $ {profit_losses_sum}')
    print (f'Average Change: $ {profit_loss_change/(rowcount-1)}')
    print(f'Greatest Increase in profits: {max_change_date} ($ {max_change})')
    print(f'Greatest Decrease in profits: {min_change_date} ($ {min_change})')

# Create text file with the results
with open("resultsPyBank.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write('-------------------------------\n')
    text_file.write(f'Total Months:  {rowcount}\n')
    text_file.write(f'Total: $ {profit_losses_sum}\n')
    text_file.write(f'Average Change: $ {profit_loss_change/(rowcount-1)}\n')
    text_file.write(f'Greatest Increase in profits: {max_change_date} ($ {max_change})\n')
    text_file.write(f'Greatest Decrease in profits: {min_change_date} ($ {min_change})\n')
    


