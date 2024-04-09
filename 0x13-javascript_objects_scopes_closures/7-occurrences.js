#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let num = 0
	for (const item of list)
	{
		if(item === searchElement) {
			num++;
		}
	}
	return num ;
};
