import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True )
boat= sns.load_dataset("titanic")
print(boat)
# p=sns.countplot(x="sex",data=boat)  #in count plot we dont need y axis
# plt.show()


# p=sns.countplot(x="sex",data=boat,hue="class")    #when we have two variables we use Hue=
# plt.show()


p=sns.countplot(x="sex",data=boat,hue="class") 
p.set_title("my first graph")
plt.show()
