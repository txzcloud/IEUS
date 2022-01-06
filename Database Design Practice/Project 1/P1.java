//START OF CODE_______________________________________________________________________________________________________________________

//Author: Tom Zheng U98418371
//Project #1 - Database COP4710

//libs
import java.util.*;
import java.io.*;

public class P1 {

   /* Define data structures for holding the data here */
   ArrayList<Coach> coachList;
   ArrayList<Team> teamList;

   public class Team{
      //variables and data types declared
      private String teamID;
      private String loc;
      private String teamName;
      private String league;
      
      //setter function for assignment
      public Team(String teamID, String loc, String teamName, String league){
         this.teamID = teamID;
         this.loc = loc;
         this.teamName = teamName;
         this.league = league;   
      }      
      
      //getter function for location
      public String retTeamID(){
         return teamID;
      }
      public String retTeamName(){
         return teamName;
      }
      public String retLocation(){
         return loc;
      }
      public String retLeague(){
         return league;
      }
      
      //@override- decide if this should be here
      //@Override
      public String toString(){ return teamID + " " + loc + " " + teamName + " " + league; }

}//end of class Team


public class Coach{
   
   //variables and datatypes declared
   private String coachID;
   private int year;
   private String firstName;
   private String lastName;
   private int seasonWin;
   private int seasonLoss;
   private int playWin;
   private int playLoss;
   private String teamCode;
   
   //setter function for assignment
   public Coach(String coachID, int year, String firstName, String lastName, int seasonWin, int seasonLoss, int playWin, int playLoss, String teamCode){
      
      this.coachID = coachID;
      this.year = year;
      this.firstName = firstName;
      this.lastName = lastName;
      this.seasonWin = seasonWin;
      this.seasonLoss = seasonLoss;
      this.playWin = playWin;
      this.playLoss = playLoss;
      this.teamCode = teamCode;
   }
   
   //getter functions below:
   public String getCoachID(){ return coachID; }
   public int getYear(){ return year; }
   public String getFirstName(){ return firstName; }
   public String getLastName(){ return lastName; }
   public int getSeasonWin(){ return seasonWin; }
   public int getSeasonLoss(){ return seasonLoss; }
   public int getPlayWin(){ return playWin; }
   public int getPlayLoss(){ return playLoss; }
   public String getTeamCode(){ return teamCode; }
   
   //@Override - decide if it is necessary to override this? child class to be override? test on Element compiler first
   @Override
   public String toString(){
      return coachID + " " + year + " " + firstName + " " + lastName + " " + seasonWin + " " + seasonLoss + " " + playWin + " " + playLoss + " " + teamCode;       
   }

}//end of class Coach



//Above is all of the classes of the objects
//__________________________________________________________________________________________________________________________
//Below is all of the functions of the database


   
    public P1() {
      /* initialize the data structures */
      coachList = new ArrayList<Coach>();
      teamList = new ArrayList<Team>();
    }
    
    //run function consisting of all queries and tasks functions
    public void run() {
        CommandParser parser = new CommandParser();

        System.out.println("The mini-DB of NBA coaches and teams");
        System.out.println("Please enter a command.  Enter 'help' for a list of commands.");
        System.out.println();
        System.out.print("> ");

        Command cmd = null;
        while ((cmd = parser.fetchCommand()) != null) {
            //System.out.println(cmd);
            boolean result=false;
            //nested if statements for taking input commands
            if (cmd.getCommand().equals("help")) {
                result = doHelp();
		      /* You need to implement all the following commands */
        	   } 
               //
			      else if (cmd.getCommand().equals("add_coach")) {
               
                  //add_coach function
                  String[] parameters = cmd.getParameters();              
                  Coach c = new Coach(parameters[0], Integer.parseInt(parameters[1]), parameters[2], parameters[3], Integer.parseInt(parameters[4]), Integer.parseInt(parameters[5]), Integer.parseInt(parameters[6]), Integer.parseInt(parameters[7]), parameters[8]);
                  coachList.add(c);   
	    	      } 
                  //
                  else if (cmd.getCommand().equals("add_team")) {
                  
                     String[] parameters = cmd.getParameters();              
                     Team t = new Team(parameters[0], parameters[1].replace("+"," "), parameters[2], parameters[3]);
                     teamList.add(t);
				      } 
                     //
                     else if (cmd.getCommand().equals("remove_coach")) {
                         String[] parameters = cmd.getParameters();
                         //removes the equal size and takes the input data after it.
                         String[] tokens = parameters[0].split("=");
                         //this variable will hold the field specified by user to search the condition coachid.
                         String field = tokens[0];
                         //this variable will hold the data given after the condition
                         String data = tokens[1];
                         //
                         for(int i = 0; i < coachList.size(); i++){
                         Coach c = coachList.get(i);                  
                                                         
                           if(field.equalsIgnoreCase("coachid") && data.equalsIgnoreCase(c.getCoachID())){
                              System.out.println(c.getFirstName() + "  " + c.getLastName() + " is removed... ");
                              coachList.remove(i);
                     
                           }
                         }
				         }	
                     
                        //
                        else if (cmd.getCommand().equals("remove_team")) {
                            String[] parameters = cmd.getParameters();
                            //removes the equal size and takes the input data after it.
                            String[] tokens = parameters[0].split("=");
                            //this variable will hold the field specified by user to search the condition coachid.
                            String field = tokens[0];
                            //this variable will hold the data given after the condition
                            String data = tokens[1];
                            //
                            for(int i = 0; i < teamList.size(); i++){
                            Team t = teamList.get(i);                  
                                                            
                              if(field.equalsIgnoreCase("teamid") && data.equalsIgnoreCase(t.retTeamID())){
                                 System.out.println(t.retTeamName() + " is removed...");
                                 teamList.remove(i);
                              }
   				             }	
                          }
                              //print_coaches function
                              else if (cmd.getCommand().equals("print_coaches")) {
                                 for(int i = 0; i < coachList.size(); i++){
                                     System.out.println(coachList.get(i));
                                 }
	  		                  } 
                              //
                              else if (cmd.getCommand().equals("print_teams")) {
                                 
                                 for(int i = 0; i < teamList.size(); i++){
                                     System.out.println(teamList.get(i));
                                 }
				                  } 
                                 // FIX THIS
                                 else if (cmd.getCommand().equals("coaches_by_name")) {
                                    
                                    String parameters[] = cmd.getParameters();
                                    for(int i = 0; i < coachList.size(); i++){
                                        if (coachList.get(i).getFirstName().trim().equalsIgnoreCase(parameters[0].replace("+", " "))){
                                            System.out.println(coachList.get(i));                      
                                        }
                                    }
				                     } 
                                    //
                                    else if (cmd.getCommand().equals("teams_by_city_league")) {
                                       
                                       String parameters[] = cmd.getParameters();
                                       for(int i = 0; i < teamList.size(); i++){
                                           if (teamList.get(i).retLocation().trim().equalsIgnoreCase(parameters[0].replace("+", " ")) && teamList.get(i).retLeague().trim().equalsIgnoreCase(parameters[1])){
                                               System.out.println(teamList.get(i));
                                           }
                                       }
				                        } 
                                       //
                                       else if (cmd.getCommand().equals("load_coaches")) {
                        
                                           String parameters[] = cmd.getParameters();              
                                           Scanner infile;
                                           
                                           try{
                                             infile = new Scanner(new File(parameters[0]));   
                                             String line;
                                             String[] data;
                                         
                                                 // removes the heading row of the data textfile
                                                 if(infile.hasNextLine()){
                                                     line = infile.nextLine();               
                                                 }                                                          
                                                   while (infile.hasNextLine()){
                                                     line = infile.nextLine();
                                                     data = line.split(",");
                                                         //ensures there is 9 parameters of data being inputted
                                                         if (data.length == 9){
                                                            Coach c = new Coach(data[0], Integer.parseInt(data[1]), data[2], data[3], Integer.parseInt(data[4]), Integer.parseInt(data[5]), Integer.parseInt(data[6]), Integer.parseInt(data[7]), data[8]);
                                                            coachList.add(c);                          
                                                         }
                                                   }
                                             infile.close();      
                                            }
                                            
                                            catch(FileNotFoundException e){
                                                System.out.println(parameters[0] + " The data text file is corrupted or does not exist.");
                                            }  
    		                              } 
                                          //
                                          else if (cmd.getCommand().equals("load_teams")) {
                                          
                                             String parameters[] = cmd.getParameters();
                                             Scanner infile;
                                             
                                             try{
                                                 infile = new Scanner(new File(parameters[0]));
                                                 String line;
                                                 String[] data;
                                                
                                                 // removes the heading row of the data textfile
                                                 if(infile.hasNextLine()){
                                                     line = infile.nextLine();               
                                                 }
                                                   while (infile.hasNextLine()){
                                                     line = infile.nextLine();
                                                     data = line.split(",");
                                                     //ensuring there are only 4 parameters for each record input
                                                     if (data.length == 4){
                                                         Team t = new Team(data[0], data[1], data[2], data[3]);
                                                         teamList.add(t);                          
                                                     }
                                                   }
                                                
                                             infile.close();  
                                             }
                                             
                                             catch(FileNotFoundException e){
                                                 System.out.println(parameters[0] + " This data text file is corrupted or does not exist.");
                                             }                                 
				                              } 
                                             //best_coach function
                                             else if (cmd.getCommand().equals("best_coach")) {
                                             
                                                String parameters[] = cmd.getParameters();
                                                //tracks netwin for specified season
                                                int netWin;
                                                //holds the best netwin out of all calculated netwins
                                                int bestNetWin = 0;
                                           
                                                Coach c;
                                                for(int i = 0; i < coachList.size(); i++){
                                                    c = coachList.get(i);
                                                    
                                                    if(c.getYear() == Integer.parseInt(parameters[0])){   
                                                        //provided formula to calculate the net win
                                                        netWin = (c.getSeasonWin() - c.getSeasonLoss()) + (c.getPlayWin() - c.getPlayLoss());   
                                                        //if netwin is greater, it will keep storing into the best until the max possible net win is stored
                                                        if(netWin > bestNetWin){
                                                            bestNetWin = netWin;
                                                        }
                                                    }
                                                }
                                               
                                                 //same loop again as above, but instead of editing the best net win, it calculates all netwin for the specified season
                                                 //then matches it with the currently stored highest record of the netwin. Then output the best coach corresponding to this netwin
                                                 for(int i = 0; i < coachList.size(); i++){
                                                     c = coachList.get(i);
                                                    
                                                     if(c.getYear() == Integer.parseInt(parameters[0])){
                                                         netWin = (c.getSeasonWin() - c.getSeasonLoss()) + (c.getPlayWin() - c.getPlayLoss());
                                                         if(netWin == bestNetWin){
                                                             System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                         }
                                                     }
                                                 }
				                                 } 
                                                //FIX THIS
                                                else if (cmd.getCommand().equals("search_coaches")) {

                                                   String[] parameters = cmd.getParameters();
                                                   //removes the equal size and takes the input data after it.
                                                   String[] token0 = parameters[0].split("=");
                                                   //String[] token1 = parameters[1].split("=");
                                                   //this variable will hold the field specified by user to search the condition by.
                                                   String field = token0[0];
                                                   //String field1 = token1[0];
                                                   //this variable will hold the data given after the condition
                                                   String data = token0[1];
                                                   //String data1 = token1[1];
                                                      //switch cannot be used here right? also nested if?
                                                      for(int i = 0; i < coachList.size(); i++){
                                                          Coach c = coachList.get(i);                  
                                                        
                                                         
                                                          if(field.equalsIgnoreCase("coachid") && data.equalsIgnoreCase(c.getCoachID())){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("year") && Integer.parseInt(data) == c.getYear()){
                                                              System.out.println(c.getFirstName() + " " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("firstname") && data.equalsIgnoreCase(c.getFirstName())){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("lastname") && data.equalsIgnoreCase(c.getLastName())){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("season_win") && Integer.parseInt(data) == c.getSeasonWin()){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("season_loss") && Integer.parseInt(data) == c.getSeasonLoss()){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("playoff_win") && Integer.parseInt(data) == c.getPlayWin()){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("playoff_loss") && Integer.parseInt(data) == c.getPlayLoss()){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                         
                                                          if(field.equalsIgnoreCase("team") && data.equalsIgnoreCase(c.getTeamCode())){
                                                              System.out.println(c.getFirstName() + "  " + c.getLastName());
                                                          }
                                                        

                                                      }
				                                    } 
                                                   //exit command function - below code is provided by Professor. I did not alter or add any code to it. 
                                                   else if (cmd.getCommand().equals("exit")) {
                                       					System.out.println("Leaving the database, goodbye!");
                                       					break;
				                                       } 
                                                      //
                                                      else if (cmd.getCommand().equals("")) {
				                                          } 
                                                         //
                                                         else {
					                                             System.out.println("Invalid Command, try again!");
		           	                                       }

			                                                if (result) {
		                                                   // ...
		                                                   }
		                                                   System.out.print("> ");
         }//end of while loop
    }//end of class run
    
    //doHelp function printing out input command instructions
    private boolean doHelp() {
        System.out.println("add_coach ID SEASON FIRST_NAME LAST_NAME SEASON_WIN ");
	     System.out.println("SEASON_LOSS PLAYOFF_WIN PLAYOFF_LOSS TEAM - add new coach data");
        System.out.println("add_team ID LOCATION NAME LEAGUE - add a new team");
        System.out.println("print_coaches - print a listing of all coaches");
        System.out.println("print_teams - print a listing of all teams");
		  System.out.println("remove_coach coach_ID - remove an existing record in coaches by ID");
		  System.out.println("remove_team team_ID - remove an existing record in teams by ID");
        System.out.println("coaches_by_name NAME - list info of coaches with the specified FIRST NAME");
        System.out.println("teams_by_city_league CITY - list the teams in the specified CITY and specific LEAGUE");
	     System.out.println("load_coach FILENAME - bulk load of coach info from a file");
        System.out.println("load_team FILENAME - bulk load of team info from a file");
        System.out.println("best_coach SEASON - print the name of the coach with the most netwins in a specified SEASON");
        System.out.println("search_coaches field=VALUE - print the name of the coach satisfying the specified conditions");
		  System.out.println("exit - quit the program");
        return true;
    }


    /**
     * @param args
     **/
     
     
    //main function
    public static void main(String[] args) {
        new P1().run();
    }

}//end of P1

//END OF CODE__________________________________________________________________________________________________________________________