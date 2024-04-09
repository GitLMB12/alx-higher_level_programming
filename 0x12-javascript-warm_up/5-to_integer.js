#!/usr/bin/node
const argv = process.argv;
const [,, number] = argv;
if (argv.length <= 2)
{
	console.log("No Argument !");
}
else
{
	let number = parseInt(argv[2]);
	if (isNaN(number))
	{
		console.log("Not Number !");
	}
	else
	{
		console.log("my number is : " + number);
	}
}
