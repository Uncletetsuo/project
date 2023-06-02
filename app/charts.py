import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'/app/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels) # <--- This is how the pie chart works it differs to the bar chart 
    ax.axis('equal')
    plt.savefig('./pay.png') # That's how it roll so 
    plt.close()


if __name__ == '__main__':
    labels = ['a','b','c']
    values = [100,200,80]
    generate_bar_chart(labels, values) 
    generate_pie_chart(labels, values)