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
   component BDC -- bascule D entrée de mise Q à 0
      port ( C   : in    std_logic;
             CLR : in    std_logic;
             D   : in    std_logic;
             Q   : out   std_logic
				 );
   end component;
   component BDS -- bascule D entrée de mise Q à 1
      port ( C   : in    std_logic;
             D   : in    std_logic;
             S   : in    std_logic;
             Q   : out   std_logic
				 );
   end component;

   signal q_wait, q_test, q_subab, q_init, q_end, q_subba : std_logic;
   signal d_wait, d_test, d_subab, d_init, d_end, d_subba : std_logic;

begin
-- A completer

  s_wait: BDS
      port map ( C => clk,
        d => d_wait,
        S => reset,
        q => q_wait);

  s_test: BDC
      port map ( C => clk,
        d => d_test,
        CLR => reset,
        q => q_test);

  s_subab: BDC
      port map ( C => clk,
        d => d_subab,
        CLR => reset,
        q => q_subab);

  s_subba: BDC
      port map ( C => clk,
        d => d_subba,
        CLR => reset,
        q => q_subba);

  s_end: BDC
      port map ( C => clk,
        d => d_end,
        CLR => reset,
        q => q_end);

  s_init: BDC
      port map ( C => clk,
        d => d_init,
        CLR => reset,
        q => q_init);

  d_wait <= q_end or (q_wait and not start);
  d_test <= q_init or q_subab or q_subba ;

  d_subab <= q_test and not inf and not egal;
  d_subba <= q_test and inf and not egal;

  d_end <= q_test and egal;
  d_init <= q_wait and start;

  getA <= q_init;
  getB <= q_init;

  subBA <= q_subba;

  ldA <= q_subab or q_init;
  ldB <= q_subba or q_init;

  done<= q_end;

end mixte;
