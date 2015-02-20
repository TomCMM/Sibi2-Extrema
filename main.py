
#===============================================================================
# Inter
#===============================================================================
# read the data from SiBi2
# do overmoller of the latent and sensible heat
# Sensitivity of Soil humidity and flux of latent heat for pasture and forest
# reread 
# Difference between Pasture and atlantic forest


net=LCB_net()


Files=[
"/home/tom/Documents/withoutRn/inter/out/Pasture/C09",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C08",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C07",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C06",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C04",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C10",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C11",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C12",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C13",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C14",
"/home/tom/Documents/withoutRn/inter/out/Pasture/C15"
 ]
Files=[
"/home/tom/Documents/withoutRn/inter/out/Forest/C04_new",
]
#Files=reversed(Files)

network=[]
for i in Files:
	print(i)
	rr=LCB_station(i)
# 	if rr.InPath =='/home/thomas/PhD/obs-lcb/LCBData/obs/Merge/C13clear_merge.TXT':
# 		rr.Data.index=rr.Data.index+ pd.DateOffset(days=1)+ pd.DateOffset(hours=1)
	net.add(rr)
	network.append(rr)

#position=range(0,2400,200)# Position of the WXT distance in meter
#name=[15,14,13,12,11,10,4,6,7,8]
#osition=[46.237139,46.238472,46.241278,46.243694,46.245861,46.246944,46.249083,46.252861,46.254528,46.256667]
name=[15,14,13,12,11,10,4,6,7,8,9]
position=[46.237139,46.238472,46.241278,46.243694,46.245861,46.246944,46.249083,46.252861,46.254528,46.256667,46.258833]
position=position[::-1]

nbsta=len(network)
time=range(0,24,1)#
#time=range(0,240,2)
Position, Time = np.meshgrid(position, time)
#Time=Time/60
Time=Time
Z=np.array([])
#Wind_speed=np.array([])
#Wind_dir=np.array([])
#Norm=np.array([])
#Theta=np.array([])
for rr in network:
	print(rr.InPath)
	#rr.Data['Date']=rr.Data.index.date
	#rr.Data=rr.Data[rr.Data.Date.isin(net_max.Data.index.date)]
	#print(rr.Data.index)
	#del rr.Data['Date']
	#print(len(rr.daily()['Ta C'].tolist()))
	#rr.Set_From('2014-10-05 00:00:00')
	#rr.Set_To('2014-11-25 00:00:00')
	#daily=rr.Data[rr.From:rr.To]
	#daily=rr.daily()
	#daily_wind=rr.Data.groupby(pd.TimeGrouper('30Min')).mean()
	#daily_wind=daily_wind.groupby(lambda t: (t.hour,t.minute)).mean()
	##daily=rr.Data.groupby(pd.TimeGrouper('1h')).mean()
	#daily=daily.groupby(lambda t: (t.hour,t.minute)).mean()
	#print(len(daily.index))
	#a=np.array([daily['Theta C'][:-1:]])
	#b=np.array([daily['Theta C'][1::]])
	#c=(b-a)/10
	Z=np.append(Z,rr.Data['Rn_C'].tolist())
	#Wind_speed=np.append(Wind_speed,daily['Sm m/s'].tolist())
	#Wind_dir=np.append(Wind_dir,daily['Dm G'].tolist())
	#Z=np.append(Z,c.tolist())
	#Norm=np.append(Norm,daily_wind['Sm m/s'].tolist())
	#Theta=np.append(Theta,daily_wind['Dm G'].tolist())
	


Z=Z.reshape(nbsta,24)
#V=np.cos(map(math.radians,Theta+180))*Norm
#U=np.sin(map(math.radians,Theta+180))*Norm

#------------------------------------------------------------------------------ 
#V_wind=np.cos(map(math.radians,Wind_dir+180))*Wind_speed
#U_wind=np.sin(map(math.radians,Wind_dir+180))*Wind_speed
#ratio_circ=((np.abs(U_wind)-np.abs(V_wind))/(np.abs(U_wind)+np.abs(V_wind)))*100# Wind ration between cross-valley mountain and plain valley circulatiion
#Z=ratio_circ.reshape (nbsta,720) 

#------------------------------------------------------------------------------ 
#V_wind=np.cos(map(math.radians,Wind_dir+180))*Wind_speed
#Z=V_wind.reshape(nbsta,720)

#U=U.reshape(nbsta,48)
#V=V.reshape(nbsta,48)
Z=Z.transpose()
#U=U.transpose()
#V=V.transpose()


start=0
end=24
#U.shape
#V.shape
Z.shape
Position.shape
Time.shape
Levels=np.linspace(Z.min(),Z.max(),100)
#Levels=np.linspace(-0.1,0.1,30)
#cmap = plt.cm.get_cmap("RdBu_r")
plt.contourf(Position[start:end,:],Time[start:end,:],Z[start:end,:],levels=Levels)	
plt.colorbar()


plt.gca().invert_xaxis()	



plt.savefig('hovermoler_OCT_NOV.png')
plt.close()



