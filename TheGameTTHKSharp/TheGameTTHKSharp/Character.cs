using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TheGameTTHKSharp
{
	class Character : IUnit, IComparable<Character>
	{
		// Klassis on privaatsed isendiväljad järgmise info jaoks: nimi (String) ja esemete nimekiri (List<Item>).
		private string nimi;
		private List<Item> Items = new List<Item>();

		public Character(string nimi)
		{
			if (String.IsNullOrEmpty(nimi))
				throw new Exception("Bad character name.");
			
			this.nimi = nimi;
		}

		public void addItem(Item item)
		{
			if (item == null)
				return;

			Items.Add(item);
		}

		public int punktideArv()
		{
			return Items.Sum(item => item.punktideArv());
		}

		public string info()
		{
			return $"Nimi {nimi}, items {Items.Count}, points {this.punktideArv()}";
		}

		public void issueItems()
		{
			if (Items.Count == 0)
			{
				Console.WriteLine("No items.");
				return;
			}

			Console.WriteLine("Items:");
			Items.ForEach((i) => Console.WriteLine($"Item {i.info()}, points {i.punktideArv()}"));
		}

		public int CompareTo(Character other)
		{
			if (other == null)
				return 1;

			return this.Items.Count.CompareTo(other.Items.Count);
		}
	}
}
