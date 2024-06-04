import matplotlib.pyplot as plt
plt.show()

line1_points = [(29.7, 1000), (33.9, 2000), (36.8, 3000), (37.6, 4000), (38.1, 5000), (38.5, 6000)]
line2_points = [(34.6, 1000), (37.5, 2000), (39.6, 3000), (40.5, 4000), (41.3, 5000), (41.9, 6000)]
line3_points = [(36.7, 1000), (38.8, 2000), (39.5, 3000), (40.3, 4000), (40.9, 5000), (41.4, 6000)]
plt.plot([point[1] for point in line1_points], [point[0] for point in line1_points], label='vp8', color='red', linestyle='--')
plt.plot([point[1] for point in line2_points], [point[0] for point in line2_points], label='vp9', color='red', linestyle='-')
plt.plot([point[1] for point in line3_points], [point[0] for point in line3_points], label='Layer2', color='blue', linestyle='--')
for points in [line1_points, line2_points]:
    plt.scatter([point[1] for point in points], [point[0] for point in points], marker='o', facecolors='red')
plt.scatter([point[1] for point in line3_points], [point[0] for point in line3_points], marker='v', facecolors='blue')

plt.grid()
plt.ylabel('PSNR(dB)')
plt.xlabel('Bitrate(kbps)')
plt.legend(loc='lower right')

plt.savefig('C:/Users/sun/fig5.png',format='png')
# 显示图表
#plt.show()
#fig6 = plt.figure(11)
#plt.subplot(111)
#plt.plot(np.linspace(0,1,Nsim)*Nsim,Rank_lin[0:],'r-*')
#plt.ylabel('Rank (Lin)')
#plt.xlim(0.0,Nsim)
#plt.savefig('fig11.pdf', format='pdf')


