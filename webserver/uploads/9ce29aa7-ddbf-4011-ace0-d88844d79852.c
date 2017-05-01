#include <stdio.h>

int main()
{
    int asc[] = {1,3,4,6,9,11};
    int desc[] = {15,10,8,6,2};
    
    int asc_size, desc_size, merged_size, merged_index=0;
    int asc_index = 0, desc_index;
    asc_size = sizeof(asc)/sizeof(int);
	desc_size = sizeof(desc)/sizeof(int);
	desc_index = desc_size-1;
	merged_size = asc_size + desc_size;
	
	int sorted[merged_size];
	
	while(merged_index < merged_size){
		if(asc[asc_index] < desc[desc_index]){
			sorted[merged_index] = asc[asc_index];
			asc_index += 1;
		}else{
			sorted[merged_index] = desc[desc_index];
			desc_index -= 1;
		}
		printf("\n %d", sorted[merged_index]);
		merged_index  += 1;
	}
}

