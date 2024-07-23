# Description: One Stop Insurance Company - Formatted Values
# Author: Harini Manohar
# Dates: July 15 - July 26, 2024


def FNumber(value):
    return "${:,.2f}".format(value)

def FDate(date_value):
    return date_value.strftime("%Y-%m-%d")

