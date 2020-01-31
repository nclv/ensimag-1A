library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;

entity tb_compteur4 is
end tb_compteur4;

architecture behavioral of tb_compteur4 is
    component compteur4 is
    port (
    clk :    in  std_logic;
    reset :  in  std_logic;
    cpt:     out unsigned (3 downto 0)
    );
    end component;

    signal clk:     std_logic := '0';
    constant clk_period : time := 8 ns; -- 8 ns par clk
    signal reset:   std_logic;

    signal cpt :  unsigned (3 downto 0);


begin
    -- compteur en hexadecimal
    C_compteur4: compteur4
    port map (  clk     => clk,
                reset   => reset,
                cpt     => cpt);

    process
    begin
        wait for clk_period/2 ; -- on change clk toutes les moitiés de clk_period, clk_period porte bien son nom
        clk <= not clk;
        wait for clk_period/2 ;
        clk <= not clk;
    end process;

    process
    begin
        reset <= '1';
        wait for clk_period ;
        reset <= '0'; -- premier reset
        wait for 10*clk_period ; -- au bout de 10 on reset le compteur (on ajoute 1 à chaque clk_period, mise à 1 de reset)
        reset <= '1';
        wait for clk_period ; -- on mets tout de suite reset à 0 pour ne pas bloquer le compteur à 1
        reset <= '0';
        wait; -- on continue d'incrémenter le compteur jusqu'à la fin des 8ns
    end process;
end behavioral;
