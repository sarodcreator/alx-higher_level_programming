#!/usr/bin/node
exports.nbOccurences = function (list, searchElement)
{
	let count = 0;
	let i = 0;
	for (i; i < list.length; i++)
	{
		if (list[i] === searchElement)
			count++;
	}
	return count;
}
