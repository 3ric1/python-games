# Steps for creating the player


1. Implement a class named Player which
   inherits StatefulEntity and adds 2D
   speed and direction
   * Handle key presses. We need a set which stores the
     keys that are currently pressed at a time
     -> for this you need to treat events of type KEYDOWN and KEYUP
   * based on the key presses, also creat a method named
     update_position which uses an external dt, and the speed and direction field to
     recompute `self.pos`
   * after the player can move left and right,
     add code for switching between the sit and walk animation
   