import database

if __name__ == '__main__':
    # format books: isbn/ title/author/published/desc
    database.insert_book("9781731702777", "Ulysses", "James Joyce", "02/02/1922", "Chronicles the passage of Leopold Bloom through Dublin during an ordinary day, June 16, 1904.")
    database.insert_book("9780142437230", "Don Quixote", "Miguel de Cervantes", "2003", "Alonso Quixano, a retired country gentleman, lives in an unnamed section of La Mancha with his niece and a housekeeper.")
    database.insert_book("9781657599086", "A Tale of Two Cities", "Charles Dickens", "18/11/1859", "Set in London and Paris before and during the French Revolution.")
    database.insert_book("9780385504201", "The Da Vinci Code", "Dan Brown", "04/01/2003", "This is a mystery-detective fiction novel. Follows symbologist Robert Langdon and Pohie Neveu as they investigate a murder.")
    database.insert_book("9781618952769", "A Room of One's Own", "Virginia Woolf", "10/24/1929", "Based on a series of lectures she delivered at Newnham College and Girton College.")
    database.insert_book("9781936690015", "Relativity: The Special and the General Theory", "Albert Einstein", "1915", "General relativity or the general theory of relativity is the geometric theory of gravitation.")
    database.insert_book("9781640322790", "The Great Gatsby", "F. Scott Fitzgerald", "01/01/1925", "The novel chronicles an era that Fitzgerald himself dubbed the Jazz Age.")
    database.insert_book("9781788886529", "War and Peace", "Leo Tolstoy", "1869", "War and Peace transcends the restrictions that Tolstoy perceived int he conventional novel.")
    database.insert_book("9780679433132", "The Divine Comedy", "Dante Alighieri", "1320", "The Divine Comedy begins in a shadowed forest on Good Friday in the year of 1300.")
    database.insert_book("9780345339706", "The Fellowship of the Ring", "J.R.R Tolkien", "08/02/1986", "The dark, fearsome Ringwraiths are searching for a Hobbit. Baggins knows that they are seeking him and the Ring he bears.")

    # format games: title/developer/publisher/release/desc
    database.insert_game("Divinity: Original Sin 2", "Larian Studios", "Larian Studios", "09/14/2017", "The critically acclaimed RPG that raised the bar, from the creators of Baldur's Gate 3.")
    database.insert_game("Dishonored", "Arkane Studios", "Bethesda Softworks", "10/09/2012", "Dishonored is an immersive first-person action game that casts you as a supernatural assassin driven by revenge.")
    database.insert_game("Final Fantasy VII", "Square Enix", "Square Enix", "01/31/1997", "In Midgar, the No. 1 Mako Reactor has been blown up by a rebel group, AVALANCHE.")
    database.insert_game("Assassin's Creed IV: Black Flag", "Ubisoft", "Ubisoft", "10/29/2013", "Pirates rule the Caribbean and have established their own lawless Republic where corruption and cruelty are commonplace.")
    database.insert_game("Burnout 3: Takedown", "Criterion Games", "Electronic Arts", "09/08/2004", "Burnout 3: Takedown is a 2004 racing video game developed by Criterion Games and published by Electronic Arts.")
    database.insert_game("Fallout 2", "Black Isle Studios", "Interplay Productions", "October 1998", "The sequel to the critically acclaimed game that took RPG'ing out of dungeons and into a dynamic, apocalyptic retro-future.")
    database.insert_game("Undertale", "tobyfox", "tobyfox", "09/15/2015", "The RPG game where you don't have to destroy anyone.")
    database.insert_game("League of Legends", "Riot Games", "Riot Games", "10/27/2009", "League of Legends is a 2009 multiplayer online battle arena video game developed and published by Riot Games.")
    database.insert_game("Monkey Island 2: LeChuck's Revenge", "LucasArts", "LucasArts", "December 1991", "Monkey Island 2: LeChuck's Revenge is an adventure game developed and published by LucasArts in 1991.")
    database.insert_game("Borderlands 2", "Gearbox Software", "2K Games", "09/18/2012", "Borderlands 2 is a 2012 first-person shooter video game developed by Gearbox Software and published by 2K Games.")

    # format movies: title/director/release/desc
    database.insert_movie("Back to the Future", "Robert Zemeckis", "1985", "Marty McFly, a 17 year old high school student is accidentally sent thirty years into the past.")
    database.insert_movie("Rogue One:A Star Wars Story", "Gareth Edwards", "2016", "The daughter of an Imperial scientist joins the Rebel Alliance in a risky move to steal the plans for the Death Star.")
    database.insert_movie("Schindler's List", "Steven Spielberg", "1993", "Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazis.")
    database.insert_movie("2001: A Space Odyssey", "Stanley Kubrick", "1968", "A mysterious artifact buried beneath the Lunar surface, mankind sets off on a quest to find its origin.")
    database.insert_movie("Casablanca", "Michael Curtiz", "1942", "An expatriate American cafe owner has to decide whether to help his former lover and her fugitive husband escape the Nazis")
    database.insert_movie("The Shawshank Redemption", "Frank Darabont", "1994", "Two imprisoned men bond over a number of years, finding solace and eventual redemtpion through acts of common decency.")
    database.insert_movie("Citizen Kane", "Orson Welles", "1941", "Following the def publishing tycoon Charles Kane, reporters scrambled to uncover the meaning of his final utterance; Rosebud")
    database.insert_movie("The Godfather", "Francis Ford Coppola", "1972", "An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.")
    database.insert_movie("Indiana Jones and the Raiders of the Lost Ark", "Steven Spielberg", "1981", "U.S hired archaeologist, Indiana Jones to find the Ark of the Covenant before Adolf Hitler's Nazis can obtain its power.")
    database.insert_movie("Forrest Gump", "Robert Zemeckis", "1994", "Alabama man with an IQ of 75 who desired is to be reunited with his childhood sweetheart.")
