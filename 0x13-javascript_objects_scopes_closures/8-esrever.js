#!usr/bin/node
exports.esrever = function (list)
{
	let reversed = [];
	let i = 0;
	for (i = list.length - 1; i >= 0; i--)
	{
		reversed.push(list[i]);
	}
	return (reversed);
}
