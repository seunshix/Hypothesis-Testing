import numpy as np
import noshmishmosh

# how many visitor visit the noshmishmosh site in a typical week
all_visitors = noshmishmosh.customer_visits
# print(all_visitors)

# how many visitors end up buying a meal or set of meals in a typical week
paying_visitors = noshmishmosh.purchasing_customers

# calculating the length of both lists
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# calculating the baseline 
baseline_percent = (paying_visitor_count/total_visitor_count) * 100
# print(baseline_percent) Output: 18.6

# Noshmishmosh want to pull in at least $1240 every week
# Determining the effect size. Let's start by investigating the average revenue generated 
# from a given sale
payment_history = noshmishmosh.money_spent # money spent by each customer in a typical week

# how many purchases will it take to reach $1240 in additional revenue
average_payment = np.mean(payment_history)
# print(average_payment)  # Output: 26.543655913978498


new_customers_needed = np.ceil(1240/average_payment)
# print(new_customers_needed) # Output: 47

percentage_point_increase = (new_customers_needed / total_visitor_count) * 100
# print(percentage_point_increase) # Output: 9.4

# calculating the minimum desirable effect
mde = (percentage_point_increase/baseline_percent) * 100
# print(mde)  # Output: 50.53763440860215

significance = 0.1

ab_sample_size = 500