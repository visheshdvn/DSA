#include<stdio.h>
int max(int a, int b) {
   if(a>b){
      return a;
   } else {
      return b;
   }
}
int knapsack(int W, int wt[], int val[], int n) {
   int i, w;
   int knap[n+1][W+1];
   for (i = 0; i <= n; i++) {
      for (w = 0; w <= W; w++) {
         if (i==0 || w==0)
            knap[i][w] = 0;
         else if (wt[i-1] <= w)
            knap[i][w] = max(val[i-1] + knap[i-1][w-wt[i-1]], knap[i-1][w]);
         else
            knap[i][w] = knap[i-1][w];
      }
   }
   return knap[n][W];
}
int main() {
	int n, W;
	printf("\nEnter the number of elements: ");
	scanf("%d", &n);

	int val[n], wt[n];
	printf("Enter the profit and weights of the elements\n");
	for (int i=0; i<n; i++) {
		scanf("%d%d", &val[i], &wt[i]);
	}
	
	printf("\nEnter Max weight: ");
	scanf("%d", &W);

	printf("The maximum profit is : %d\n", knapsack(W, wt, val, n));
	return 0;
}