#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 2 )
{
	console.log("Missing size");
}
else
{
	const x = parseInt(argv[2]);
	let row ="";
	if (isNaN(x))
	{
		console.log("Missing size");
	}
	else
	{
		for (let i = 0; i <= x; i++)
		{
			for (let j = 0; j <= x; j++)
			{
				row +="X";
			}
		}
		console.log(row);
	}
}
