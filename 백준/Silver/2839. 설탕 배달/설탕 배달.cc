#include <stdio.h>

int main()
{
	int kg = 0;//설탕의 무게
	int set5 = 0;//5kg 묶음
	int set3 = 1;//3kg 묶음

	scanf("%d", &kg);

	set5 = kg / 5;

	if (kg % 5 == 0)//5kg로 다 묶을 수 있다면
	{
		printf("%d", set5);
	}
	else//5kg로 다 묶을 수 없다면
	{
		int i = 0;

		for (i = set5; i >= 0; i--)//5kg 묶음을 하나씩 줄여가면서 테스트하기
		{
			set3 = (kg - i * 5) / 3;
			if (kg == i * 5 + set3 * 3)
			{
				printf("%d\n", i + set3);
				break;
			}
			else
			{
				continue;
			}
		}

		if (i == -1)
		{
			printf("%d", -1);
		}
	}
}