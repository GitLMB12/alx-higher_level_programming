#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 2)
{
	console.log("Missing number of occurrences");
}
else
{
	const x = parseInt(argv[2]);
	if (isNaN(x))
	{
		console.log("Missing number of occurrences");
	}
	else
	{
		for (let i = 0; i < x; i++)
		{
			console.log("c is fun");
		}
	}
