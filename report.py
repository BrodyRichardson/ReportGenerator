import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--team-map", help="TeamMap file name")
parser.add_argument("-p", "--product-master", help="ProductMaster file name")
parser.add_argument("-s", "--sales", help="Sales file name")
parser.add_argument("--team-report", help="TeamReport file name")
parser.add_argument("--product-report", help="ProductReport file name")
args = parser.parse_args()


productMaster = []
with open(args.product_master) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        productMaster.append(row)


sales = []
with open(args.sales) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        sales.append(row)


teamMap = []
with open(args.team_map) as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        teamMap.append(row)


# Team,GrossRevenue
with open(args.team_report, 'w', newline= '') as f:
    writer = csv.writer(f)

    #Header
    writer.writerow(["TeamId", "TeamName", "GrossSales"])

    #Data
    for team in teamMap:
        grossSales = 0

        teamId = team[0]
        teamName = team[1]

        for sale in sales:
            if sale[2] == teamId:
                productId = sale[1]
                quantity = int(sale[3])
                discount = float(sale[4]) / 100

                for product in productMaster:
                    if product[0] == productId:
                        price = float(product[2])
                        grossSales += price * quantity


        writer.writerow([teamId, teamName, grossSales])

outArr = []

for product in productMaster:
    grossRevenue = 0
    totalUnits = 0
    discountCost = 0

    productId = product[0]
    productName = product[1]

    for sale in sales:
        if sale[1] == productId:
            quantity = int(sale[3])
            discount = float(sale[4]) / 100

            price = float(product[2])
            grossRevenue += price * quantity
            totalUnits += quantity
            discountCost += grossRevenue * discount

    outArr.append([productName, grossRevenue, totalUnits, discountCost])

outArr.sort(key=lambda x: x[1], reverse=True)

with open(args.product_report, 'w', newline= '') as f:
    writer = csv.writer(f)

    # Write header
    writer.writerow(["ProductName", "GrossRevenue", "TotalUnits", "DiscountCost"])

    # Write data
    for row in outArr:
        writer.writerow(row)