library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity PGCD is
        port ( clk   :    in  std_logic;
               reset :  in  std_logic;
               start : in  std_logic;
               A0:   in  unsigned (7 downto 0);
               B0:   in  unsigned (7 downto 0);
               done  : out  std_logic;
               aff:  out  unsigned (7 downto 0)
				);
end PGCD;

architecture mixte of PGCD is
        component PC 
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
               done  : out  std_logic );
        end component;


        component PO 
        port ( clk:     in  std_logic;
               reset:   in  std_logic;
               getA:   in  std_logic;
               getB:   in  std_logic;
               subBA:   in  std_logic;
               ldA:   in  std_logic;
               ldB:   in  std_logic;
               A0:   in  unsigned (7 downto 0);
               B0:   in  unsigned (7 downto 0);
               LT :  out std_logic;
               EQ:   out  std_logic;
               Res:  out  unsigned (7 downto 0));
        end component;

        signal s_inf, s_egal, s_geta, s_getb,s_subba,s_lda, s_ldb: std_logic;

begin
        
        i_PC: PC 
        port map ( clk=> clk, 
               reset=> reset,
               start=>start,
               inf  => s_inf,
               egal => s_egal,
               getA=>  s_geta,
               getB=>  s_getb,
               subBA=> s_subba,
               ldA=>   s_lda,
               ldB=>   s_ldb,
               done  => done);


        i_PO: PO 
        port map ( clk=>clk,
               reset=>reset,
               getA=>s_getA,
               getB=> s_getB,
               subBA=>s_subBA,
               ldA=>  s_ldA,
               ldB=>  s_ldB,
               A0=>   A0,
               B0=>   B0,
               LT =>  s_inf,
               EQ=>   s_egal,
               Res=>  aff);
        
        
end mixte;
