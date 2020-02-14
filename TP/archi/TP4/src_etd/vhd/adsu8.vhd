library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.ALL;

entity ADSU8 is
port(
    CO   : out std_logic;
    OFL  : out std_logic;
    S    : out unsigned(7 downto 0);

    A    : in unsigned(7 downto 0);
    ADD  : in std_logic;
    B    : in unsigned(7 downto 0);
    CI   : in std_logic
  );
end ADSU8;

architecture ADSU8_V of ADSU8 is

begin
  adsu_p : process (A, ADD, B, CI)
    variable adsu_tmp : unsigned(9 downto 0);
  begin
    if (ADD = '1') then
      adsu_tmp := ('0'&A &'1') + ('0'& B & CI);
    else
      adsu_tmp := ('0'&A & '0') - ('0'&B& not CI);
    end if;
      
  S <= adsu_tmp(8 downto 1);

  if (ADD='1') then
    CO <= adsu_tmp(9);
    OFL <=  ( A(7) and B(7) and (not adsu_tmp(8)) ) or ( (not A(7)) and (not B(7)) and adsu_tmp(8) );  
  else
    CO <= not adsu_tmp(9);
    OFL <=  ( A(7) and (not B(7)) and (not adsu_tmp(8)) ) or ( (not A(7)) and B(7) and adsu_tmp(8) );  
  end if;

  end process;
  
end ADSU8_V;
