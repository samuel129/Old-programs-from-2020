//Solutions to the quadratic equation Ax^2 + Bx + C = 0 may be calculated using the quadratic formulas:

// x = (-B + (B^2-4AC)^1/2)/2A or x = (-B -(B^2 -4AC)^1/2)/2A

//These formulas may be used, of course, only if the leading coefficient, A, is not zero. The number and type of 
//solutions is determined by the value of the expression under the radical sign, B^2 - 4AC, known as the discriminant:

//Value of discriminant: | positive |   zero   |   negative   |
//Number of solutions:   |     2    |     1    |       2      |
//Kind of solutions:     |   real   |   real   |   imaginary  |

// Your job is to write a program which will read the coefficients of a quadratic equation and, if the leading coefficient
// is non-zero, calculate and report the solutions. Since the programming languages does not provide the imaginary type, youll
// have to take appropriate steps to give imaginary results in te form shown. Just remember that every imaginary number is really
// determined by a pair of real numbers.

#include <iostream>

using namespace std;

int main()
{
	double discriminant;
	int a;
	int b;
	int c;
	double result;
while(a != 0){
	cout << "Please enter an integer value for A.";
	cin >> a;
	if (a == 0){
		cout << "Please enter a non-zero value for A!";
	}
}
	cout << "Please enter an integer value for B.";
	cin >> b;
	cout << "Please enter an integer value for C.";
	cin >> c;

	discriminant = ((b**2) - (4*a*c));
	if (discriminant > 0){
		
	}
    return 0;
}

