#!/usr/bin/node
const argv = process.argv;
const [,,a,b] = argv;
function add(a, b)
{
	let result = a + b ;
	console.log(result);
}
add(paseInt(a),paseInt(b));
