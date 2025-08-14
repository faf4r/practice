#include<stdio.h>

int main(void){  // ***学会最基础的冒泡排序和直接选择排序 ***
	const int n = 3;
	int ar[n]; //可变数组不能初始化值 
	int temp, i;
	printf("please input three numbers: ");
	scanf("%d%d%d", &ar[0],&ar[1],&ar[2]); //必须传入元素的内存地址，即&符号。或者（ar+i ）表示地址。*（ar+i）解析地址 
	
	/* for (i=0; i<n-2; i++){
		if (ar[i]>ar[i+1]){ //升序排序 
			temp = ar[i];
			ar[i] = ar[i+1];
			ar[i+1] = temp;
		}
	} */ //错误答案，没有单个元素与全部元素比较 
	
	//我的排序：对每个元素，最小或最大的移到前面，注意最前的已经不需要再比较了 
	int k;
	for (i=0; i<n; i++){//确定第i个元素的值（全部比较后移上去的，比较了就是确定的，不会再变） 
		for (k=i+1; k<n; k++){
			if (ar[i]>ar[k]){
				temp = ar[i];
				ar[i] = ar[k];
				ar[k] = temp;
			}
		}
	} //我的排序更像直接选择排序，而不是冒泡那种连着调换
	 
	
	//标准的冒泡排序：值是连续的比较，不断涌动，把最大的给挤到最后面
	for (i=0; i<n; i++){
		for (k=0; k<n-i-1; k++){ //这是让后面的大数挤在末尾不动 （-1是因为代码里数组有+1） 
			if (ar[k]>ar[k+1]){
				temp = ar[k];
				ar[k] = ar[k+1];
				ar[k+1] = temp;
			}
		}
	} 
	
	//快速选择排序：其实和冒泡排序差不多，只不过用索引index，确定最大值后才交换
	int index;
	for (i=0; i<n; i++){
		index = 0;
		for (k=0; k<n-i;k++){
			if (ar[k]>ar[index])index=k;
		}
		temp = ar[n-i-1]; // 把最大或最小的数放最后，之后不再比较他们 
		ar[n-i-1] = ar[index];
		ar[index] = temp;
	} 
	 
	printf("%d<%d<%d\n", ar[0], ar[1], ar[2]);
	
	//书上用if分支，用t做中间值，交换abc的值进行排序（a>b  a>c  b>c）这几种情况 
	return 0;
}
