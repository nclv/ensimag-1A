library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity BDC is
  port(
    C : in std_logic;
    D : in std_logic;
    CLR : in std_logic;
    Q : out std_logic
    );
end BDC;

architecture beh of BDC is
begin
 
  process(C)
  begin
    if (rising_edge(C)) then
      if (CLR = '1') then
        Q <= '0' ;
      else
        Q <= D ;
      end if;
    end if;
  end process;
end beh;


