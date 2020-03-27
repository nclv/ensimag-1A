library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_pgcd is
end tb_pgcd;

architecture behavioral of tb_pgcd is
        component pgcd is
                port ( clk   :    in  std_logic;
                       reset :  in  std_logic;
                       start : in  std_logic;
                       A0:   in  unsigned (7 downto 0);
                       B0:   in  unsigned (7 downto 0);
                       done  : out  std_logic;
                       aff:  out  unsigned (7 downto 0));
        end component;

        signal clk:     std_logic := '0';
        signal s_reset,s_start,s_done:   std_logic;
        signal s_aff, s_initA, s_initB:  unsigned (7 downto 0);
   -- Clock period definitions
        constant clk_period : time := 8 ns;

begin

        UUT: pgcd
        port map (  clk     => clk,
                    reset   => s_reset,
                    start   => s_start,
                    A0      => s_initA,
                    B0      => s_initB,
                    done    => s_done ,
                    aff     => s_aff
            );

        process
        begin
                clk <= not clk;
                wait for clk_period/2 ;
        end process;

        process
        begin
                s_initA <= X"30";
                s_initB <= X"24";
                s_start <= '0';
                wait for 9*clk_period/4;
                s_start <= '1';
                wait for clk_period;
                s_start <= '0';
                attente : loop
                        wait for clk_period;
                        exit attente when s_done = '1';
                end loop attente;
                wait for 2*clk_period;
                report "Simulation terminé" severity failure;
                wait;
        end process;

        process
        begin
                s_reset <= '1';
                wait for clk_period/4;
                s_reset <= '0';
                wait;
        end process;
end behavioral;

