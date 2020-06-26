using System;

namespace ConsoleGame
{
 class Game : SuperGame
 {
  public new static void UpdatePosition(string key_pressed, out int xChange, out int yChange)
  {
   switch (key_pressed)
   {
    case "LeftArrow":
     xChange = -1;
     yChange = 0;
     break;
    case "RightArrow":
     xChange = 1;
     yChange = 0;
     break;
    case "UpArrow":
     xChange = 0;
     yChange = -1;
     break;
    case "DownArrow":
     xChange = 0;
     yChange = 1;
     break;
    default:
     xChange = 0;
     yChange = 0;
     break;
   }
  }

  public new static char UpdateCursor(string key_pressed)
  {

   switch (key_pressed)
   {
    case "LeftArrow":
     return '<';
    case "RightArrow":
     return '>';
    case "UpArrow":
     return '^';
    case "DownArrow":
     return 'v';
    default:
     return '<';
   }
  }

  public new static int KeepInBounds(int coordinate, int max_value)
  {

   if (coordinate >= max_value)
   {
    return 1;
   }
   else if (coordinate < 0)
   {
    return max_value - 1;
   }
   else
   {
    return coordinate;
   }

  }

  public new static bool DidScore(int current_x, int current_y, int goal_x, int goal_y)
  {
   bool scored = false;
   if (current_x == goal_x && current_y == goal_y)
   {
    scored = true;
   }
   else
   {
    scored = false;
   }
   return scored;
  }


 }
}