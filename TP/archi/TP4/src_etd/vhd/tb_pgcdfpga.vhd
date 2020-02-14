library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity tb_pgcdfpga is
end tb_pgcdfpga;

architecture behavioral of tb_pgcdfpga is
        component pgcdfpga is
        port ( clk   :    in  std_logic;
               reset :  in  std_logic;
               start : in  std_logic;
               B:   in  unsigned (5 downto 0);
               aff:  out  unsigned (3 downto 0)
				);
        end component;

        signal clk:     std_logic := '0';
        signal s_reset,s_start:   std_logic;
        signal s_initB:  unsigned (5 downto 0);
        signal s_aff:  unsigned (3 downto 0);
        constant clk_period : time := 8 ns;

begin

        UUT: pgcdfpga
        port map (  clk     => clk,
                    reset   => s_reset,
                    start   => s_start,
                    B      => s_initB,
                    aff     => s_aff
            );

        process
        begin
                clk <= not clk;
                wait for clk_period/2 ;
        end process;

        process
        begin
                s_initB <= "100100";
                s_start <= '0';
                wait for 9*clk_period/4;
                s_start <= '1';
                wait for 2*clk_period;
                s_start <= '0';
                attente : loop
                        s_initB(5)<= not s_initB(5); -- on permute le bouton 5 pour changer la vue sur les LED (haute ou basse)
                        wait for clk_period/2;
                        if s_aff = x"0" then
                            s_initB(5)<= not s_initB(5);
                            wait for clk_period/2;
                            if s_aff /= x"0" then
                                exit attente;
                            end if;
                        else
                            exit attente;
                        end if;
                end loop attente;
                s_initB(5)<= not s_initB(5);
                wait for clk_period/2;
                s_initB(5)<= not s_initB(5);
                wait for clk_period/2;
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

