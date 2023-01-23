namespace TheGameTTHKSharp
{
	class Item : IUnit
	{
		private int punktid;
		private string nimetus;

		public Item(int punktid, string nimetus)
		{
			this.punktid = punktid;
			this.nimetus = nimetus;
		}
		
		public int punktideArv()
		{
			return punktid;
		}

		public string info()
		{
			return nimetus;
		}
	}
}
