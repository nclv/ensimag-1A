library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity PGCDFPGA is
        port ( clk   :    in  std_logic;
               reset :  in  std_logic;
               start : in  std_logic;
               B:   in  unsigned (5 downto 0);
               aff:  out  unsigned (3 downto 0)
				);
end PGCDFPGA;

architecture mixte of PGCDFPGA is
        component PGCD 
        port ( clk   :    in  std_logic;
               reset :  in  std_logic;
               start : in  std_logic;
               A0:   in  unsigned (7 downto 0);
               B0:   in  unsigned (7 downto 0);
               done  : out  std_logic;
               aff:  out  unsigned (7 downto 0)
				);
        end component;

   component FD8CE
      port ( C   : in    std_logic; 
             CE  : in    std_logic; 
             CLR : in    std_logic; 
             D   : in    unsigned (7 downto 0); 
             Q   : out   unsigned (7 downto 0));
   end component;

    signal s_done:   std_logic;
    signal s_A0, s_B0, s_pgcd, s_aff:  unsigned (7 downto 0);

begin
        
    i_PGCD: pgcd
    port map (  clk     => clk,
                reset   => reset,
                start   => start,
                A0      => s_A0,
                B0      => s_B0,
                done    => s_done ,
                aff     => s_pgcd
        );

        regA: FD8CE
        port map (  C     =>  clk,
                    CE  =>  s_done,
                    CLR   => reset,
                    d     => s_pgcd,
                    q     => s_aff);

        s_A0 <= X"3C";
        s_B0 <= "00"&B;
        aff <= s_aff(3 downto 0) when B(5)='0' else s_aff(7 downto 4);
end mixte;
