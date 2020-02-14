library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.ALL;

entity COMPM8 is
port(
    GT  : out std_logic;
    LT  : out std_logic;
    A   : in unsigned(7 downto 0);
    B   : in unsigned(7 downto 0)
  );
end COMPM8;

architecture COMPM8_V of COMPM8 is
begin
     
  GT <= '1' when (A > B) else '0';
  LT <= '1' when (A < B) else '0';
 
end COMPM8_V;
