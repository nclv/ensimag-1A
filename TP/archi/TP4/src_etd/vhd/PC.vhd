library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity PC is
        port ( clk:    in  std_logic;
               reset:  in  std_logic;
               start: in  std_logic;
               inf  :  in std_logic;
               egal :  in  std_logic;
               getA:   out  std_logic;
               getB:   out  std_logic;
               subBA:  out  std_logic;
               ldA:    out  std_logic;
               ldB:    out  std_logic;
               done  : out  std_logic
       );
end PC;

architecture mixte of PC is
-- Déclaration des composants BDC et BDS
-- Aller voir ce qu'ils font dans le fichier .vhd correspondant.
   component BDC
      port ( C   : in    std_logic; 
             CLR : in    std_logic; 
             D   : in    std_logic; 
             Q   : out   std_logic
				 );
   end component;
   component BDS
      port ( C   : in    std_logic; 
             D   : in    std_logic; 
             S   : in    std_logic; 
             Q   : out   std_logic
				 );
   end component;


begin
-- A completer
end mixte;
