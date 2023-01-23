using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace TheGameTTHKSharp
{
	class Program
	{
		static Random rand = new Random();

		static List<Item> items = new List<Item>();
		static readonly string itemsFilePath = Path.Combine(Environment.CurrentDirectory, @"items.txt");
		
		static void Main(string[] args)
		{
#if !DEBUG
			throw new NotImplementedException("Bad!");
#endif
			ParseItems(itemsFilePath);

			Character[] characters = {
				new Character("Vasya"),
				new Character("Inga"),
				new Character("Oleg"),
				new Character("Samurai"),
				new Character("Marina")
			};

			foreach(Character character in characters)
			{
				int nRand = rand.Next(2, 10);
				for (int i = 0; i < nRand; i++)
				{
					character.addItem(items.OrderBy(item => rand.Next()).FirstOrDefault());
				}
			}

			Game game = new Game(characters);

			foreach(Character character in characters)
			{
				Console.WriteLine(character.info());
			}

			Console.WriteLine(" ");
			Console.WriteLine(" ");

			Console.WriteLine("Suurima Esemete Character:");

			var suurimaEsemeteChar = game.suurimaEsemeteArvuga();
			if (suurimaEsemeteChar != null)
			{
				Console.WriteLine(suurimaEsemeteChar.info());
				Console.WriteLine(" ");
				suurimaEsemeteChar.issueItems();
			}

			Console.WriteLine(" ");
			Console.WriteLine(" ");

			Console.WriteLine("Suurima Punktide Character:");

			var suurimaPunktideChar = game.suurimaPunktideArvuga();
			if (suurimaPunktideChar != null)
			{
				Console.WriteLine(suurimaPunktideChar.info());
				Console.WriteLine(" ");
			}

			Console.ReadKey();
		}

		static void ParseItems(string path)
		{
			try
			{
				using (StreamReader sr = new StreamReader(path, System.Text.Encoding.Default))
				{
					string ln;
					while ((ln = sr.ReadLine()) != null) {
						string[] iEntry = ln.Split(";", StringSplitOptions.RemoveEmptyEntries);
						items.Add(new Item(Convert.ToInt32(iEntry[1]), iEntry[0]));
					}
				}
			}
			catch (Exception ex)
			{
				Console.WriteLine($"Error: {ex.Message}");
				Console.ReadKey();
				Environment.Exit(0);
			}
		}
	}
}
