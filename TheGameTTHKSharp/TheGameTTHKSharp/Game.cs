using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TheGameTTHKSharp
{
	class Game
	{
		private Character[] characters;

		public Game(Character[] characters)
		{
			this.characters = new Character[characters.Length];
			characters.CopyTo(this.characters, 0);
		}

		public Character suurimaEsemeteArvuga()
		{
			int index = 0;
#if true
			for (int i = 0; i < characters.Length; i++)
			{
				var c = characters.ElementAt(i);
				var comp = c.CompareTo(characters.ElementAt(index));
				if (comp > 0)
				{
					index = i;
				}
			}

			return characters.ElementAt(index);
#else
			var ret = characters.Where((c, i) => {
				var comp = c.CompareTo(characters.ElementAtOrDefault(index));
				if (comp > 0)
				{
					index = i;
				}
				return comp > 0;
			}).LastOrDefault();

			return ret;
#endif
		}

		public Character suurimaPunktideArvuga()
		{
			return characters.FirstOrDefault(character => character.punktideArv() == characters.Max(character => character.punktideArv()));
		}
	}
}
