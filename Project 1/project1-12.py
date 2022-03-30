# Thomas Powell Horan
shares = 2000
price_per_share = 40
amount_for_purchased_shares = shares * price_per_share
comission = amount_for_purchased_shares * .03
final_dollar_amount = amount_for_purchased_shares + comission

sell_price_per_share = 42.75
amount_for_sold_shares = shares * sell_price_per_share
comission_sale = amount_for_sold_shares * .03
final_sale = amount_for_sold_shares - comission_sale

profit = final_sale - final_dollar_amount

print(f'''
This program calcualtes the profits and loss made by Joe in the Stock Market 
===========================================================================
                              BUY
===========================================================================
Number of shares purchased is: ${shares:,.2f}
Price per share is: ${price_per_share:,.2f}
Total amount for purchased shares is: ${amount_for_purchased_shares:,.2f}
The total commmison paid to broker (3%): ${comission:,.2f}
Joe's final total dollar amount is: ${final_dollar_amount:,.2f}
===========================================================================
                              SALE
===========================================================================
Number of shares sold is: ${shares:,.2f}
Price per share sold is: ${sell_price_per_share:,.2f}
Total amount for sold shares is: ${amount_for_sold_shares:,.2f}
The total commmison paid to broker for the sale (3%) is: ${comission_sale:,.2f}
Joe's final total dollar amount sold is: ${final_sale:,.2f}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Joe's difference dollar amount for sold-bought shares is: ${profit:,.2f}

	''' )

