library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

package CPU_pkg is
        subtype w8 is unsigned(7 downto 0);
        subtype w16 is unsigned(15 downto 0);

        type ADDR_select is ( from_PC, from_AD );
        type RES_select is ( from_ALU, from_input );
        type PC_select is ( from_INCR, from_AD );

        type CPU_CTRL is record
                rst     : boolean;
                selA    : unsigned(1 downto 0);
                selB    : unsigned(1 downto 0);
                op      : unsigned(2 downto 0);
                selR    : RES_select;
                selAD   : ADDR_select;
                selPC   : PC_select;
                ldPC    : boolean;
                ldADH   : boolean;
                ldADL   : boolean;
                ldIR    : boolean;
                ldR0    : boolean;
                ldR1    : boolean;
                ldR2    : boolean;
                ldR3    : boolean;
                ldz     : boolean;
        end record;
  constant CTRL_defaut : CPU_CTRL := 
    (
                rst    => false, 
                selA   => "00", 
                selB   => "00", 
                op     => "000", 
                selR   => from_ALU, 
                selAD  => from_PC, 
                selPC  => from_INCR, 
                ldPC   => false, 
                ldADH  => false, 
                ldADL  => false, 
                ldIR   => false, 
                ldR0   => false, 
                ldR1   => false, 
                ldR2   => false, 
                ldR3   => false,
                ldz    => false 
      );

        type CPU_COMPTE_RENDU is record
                z       : std_logic;
                IR      : w8;
        end record;

end CPU_pkg;
