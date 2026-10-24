import numpy as np

#-------preparing data-------

products_names=np.array(["Laptop", "Mouse","Keyboard", "Monitor"])
products_prices=np.array([850, 25, 60, 220])
Week_days=np.array(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"])
daily_sales=np.array([[2,10,5,3],
                      [1,15,8,2],
                      [3,8,4,4],
                      [0,20,10,1],
                      [4,12,6,5],
                      [5,18,9,6]
                      ])
print(daily_sales)
print(daily_sales.ndim)
print(daily_sales.shape)

#-------sales Analysis-------

total_unit_sold=daily_sales.sum(axis=0)
total_unit_sold_per_day=daily_sales.sum(axis=1)
print(total_unit_sold)
print(total_unit_sold_per_day)
print(total_unit_sold_per_day.max())
Best_selling_index=np.argmax(total_unit_sold)
Best_selling_item=products_names[Best_selling_index]
print(Best_selling_item) 

#-------Revenue Analysis-------
revenue_per_day=daily_sales*products_prices
print(revenue_per_day)

revenue_per_item=total_unit_sold*products_prices
print(revenue_per_item)

store_revenue_per_week=revenue_per_item.sum()
print(store_revenue_per_week)

Best_revenue_index=np.argmax(revenue_per_item)
Best_revenue_item_name=products_names[Best_revenue_index]
print(Best_revenue_item_name)

#-------Business Insights-------

three_laptops_sold=(daily_sales[:,0])>3 #Boolean Mask 
print(Week_days[three_laptops_sold])

Sorted_items_indices=np.argsort(revenue_per_item)[::-1]
Sorted_items_names=products_names[Sorted_items_indices]
print(Sorted_items_names)

contribution_of_product=np.round((revenue_per_item/store_revenue_per_week)*100,2)
print(contribution_of_product)