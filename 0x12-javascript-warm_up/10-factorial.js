#!/usr/bin/node
function Factorial(x)
{
	if(isNaN(x) || x < 2)
	{
		return (1);
	}
	else
	{
		return (x * Factorial(x-1));
	}
}
console.log(Factorial(process.argv[2]));
