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
	
	rotate()
	{
		let c = this.height;
		this.height = this.width;
		this.width = c;
	}

	double() 
	{
		this.width = this.width * 2;
		this.height = this.height * 2;
	}

}
module.exports = Rectangle;
