import numpy as np
import matplotlib.pyplot as plt

num_epochs = 200
## Resultados Lau
log_folder = '/media/SSD2/cariotipos/classification-net/' 
exp_name = '_1000epochs_lr0.001_batch_size80/'
legends = ['densenet121', 'resnet18', 'resnet34', 'resnet50', 'resnet101']
folder_names = [legends[0]+exp_name, legends[1]+exp_name, legends[2]+exp_name, legends[3]+exp_name, legends[4]+exp_name]
#colors = ['#000066', '#0000CC', '#3333FF', '#004C99', '#0080FF', '#00CCCC']

for i in range(len(legends)):

    data = np.genfromtxt(log_folder+folder_names[i]+'test.txt')
    #plot new data to figure
    x_axis = range(0,num_epochs)
    plt.plot(x_axis, data[:num_epochs], label=legends[i])

## Resultados Guillo
log_folder = '/media/SSD1/resultados_cariotipo/'
exp_name = '_1000epochs_lr0.001_batch_size80/'
legends = ['alexnet', 'vgg11', 'vgg11_bn', 'vgg16', 'vgg16_bn']
folder_names = [legends[0]+exp_name, legends[1]+exp_name, legends[2]+exp_name, legends[3]+exp_name, legends[4]+exp_name]
#colors = ['#000066', '#0000CC', '#3333FF', '#004C99', '#0080FF', '#00CCCC']

for i in range(len(legends)):

    data = np.genfromtxt(log_folder+folder_names[i]+'test.txt')
    #plot new data to figure
    x_axis = range(0,num_epochs)
    #plt.plot(x_axis, data, color=colors[i], label=legends[i])
    plt.plot(x_axis, data[:num_epochs], label=legends[i])

plt.legend()
plt.title("Precisión de clasificación según época")
plt.xlabel("Época")
plt.ylabel("Precisión (%)")
#plt.ylim(0,100)
#ymin, ymax = plt.ylim()
plt.show()

plt.savefig('Top-1_accuracy'+exp_name[:-1]+'.png')
