library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity BDS is
  port(
    C : in std_logic;
    D : in std_logic;
    S : in std_logic;
    Q : out std_logic
    );
end BDS;

architecture beh of BDS is
begin
 
  process(C)
  begin


    if (rising_edge(C)) then
      if (S = '1') then
        Q <= '1' ;
      else
        Q <= D ;
      end if;
    end if;
  end process;
end beh;


