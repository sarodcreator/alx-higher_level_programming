#!/usr/bin/node
class Rectangle
{
	constructor (w, h)
	{
		if (w > 0 & h > 0)
		{
			this.width = w;
			this.height = h;
		}
	}


	print()
	{
		let i;
		for (i = 0; i < this.height; i++)
		{
			let row = 0;
			let col = '';
			for (row; row < this.width; row++)
			{
				col += 'X';
			}
			console.log(col);
		}
	}
}
module.exports = Rectangle;
