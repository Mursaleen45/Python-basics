#Dictionary
aliens={'x_increment':0,'y_increment':25,'speed':'medium'}
print(f"Original x_increment value: {aliens['x_increment']}")

if aliens['speed']=='slow':
    x_increment=1
elif aliens['speed']=='medium':
    x_increment=2
else:
    x_increment=3

    aliens['x_increment']=aliens['x_increment'] + x_increment
    print(f"New x_increment value: {aliens['x_increment']}")
