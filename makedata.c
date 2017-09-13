#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LEN 100

char *get_numstring(int i) {
   	char *res = (char *)malloc(6 * sizeof(char));
	sprintf(res,"%d",i);
	if(i/10 == 0) {
		sprintf(res, "00000%d", i);
	}
	else if(i/100 == 0) {
 		sprintf(res, "0000%d",i);
	}
	else if(i/1000 == 0) {
		sprintf(res, "000%d", i);
	}
	else if(i/10000 == 0) {
		sprintf(res, "00%d", i);
	}
	else {
		sprintf(res, "0%d", i);
	}
	return res;
}

int main(int argc, char *argv []) {
	if(argc != 5) {
		printf("Incorrect number of parameters entered!\n");
		return 0;
	}
	 
	int x1 = atoi(argv[1]);
	int x2 = atoi(argv[2]);
	int x3 = atoi(argv[3]);
	int x4 = atoi(argv[4]);

	//char pref[LEN] = "/home/jishnu/Datasets/Arabic/AT";
	char pref2[LEN] = "img";
	//char buf1[LEN];
	//sprintf(buf1, "%s%d",pref,len);
	//char buf2[LEN];
	//sprintf(buf2, "%s%s",buf1,pref2);
	char suf[LEN] = ".jpg";
	char buf[LEN];
	
	int i;
	char fname[20];
	//sprintf(fname, "val.txt", len);
	FILE *fptr;
	fptr = fopen("val.txt", "w");
	if(fptr == NULL) {
		printf("File creation error!!\n");
		return 0;
	}
	
	//for(i=0;i<len;i++) {
	for(i=x1;i<=x2;i++) {
		char *n = get_numstring(i);
		int class = i%10;
		sprintf(buf, "%s%s%s %d",pref2,n,suf,class);
		fprintf(fptr,"%s\n",buf);
	}
	for(i=x3;i<=x4;i++) {
		char *n = get_numstring(i);
		int class = i%10;
		sprintf(buf, "%s%s%s %d",pref2,n,suf,class);
		fprintf(fptr,"%s\n",buf);
	}
	fclose(fptr);
	return 0;
}
	
