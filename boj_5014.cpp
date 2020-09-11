#include <iostream>
#include <cmath>
using namespace std;

int main(void)
{
	int f, s, g, u, d;
	int x;
	double y;
	double axis;
	double constant;
	int result;
	scanf("%d %d %d %d %d", &f, &s, &g, &u, &d);

	if (u == 0 || d == 0)
	{
		if (u == 0 && d != 0)
		{
			axis = s - g;
			axis = axis / (double)d;
			if (axis < 0)
			{
				cout << "use the stairs" << endl;
			}
			else
			{
				if ((int)axis != axis)
				{
					cout << "use the stairs" << endl;
				}
				else
				{
					result = axis;
					cout << result << endl;
				}
			}
		}
		else if (u != 0 && d == 0)
		{
			axis = g - s;
			axis = axis / (double)u;
			if (axis < 0)
			{
				cout << "use the stairs" << endl;
			}
			else
			{
				if ((int)axis != axis)
				{
					cout << "use the stairs" << endl;
				}
				else
				{
					result = axis;
					cout << result << endl;
				}
			}
		}
		else if (u == 0 && d == 0)
		{
			if (s == g)
			{
				cout << 0 << endl;
			}
			else
			{
				cout << "use the stairs" << endl;
			}
		}
	}
	else
	{
		axis = s - g;
		constant = (double)u / (double)d;
		axis = axis / (double)d;

		x = 0;

		while (1)
		{
			y = constant * (double)x + axis;
			if (y >= 0)
			{
				y = (round(y * 1000000000)) / 1000000000.0;
				if (int(y) == y)
				{
					if (s + u - d != 0)
					{
						result = x + y;
						cout << result << endl;
						break;
					}
					else
					{
						cout << "use the stairs" << endl;
						break;
					}

				}
			}
			x++;
			if (x == 1000000)
			{
				cout << "use the stairs" << endl;
				break;
			}
		}
	}
	return 0;
}

