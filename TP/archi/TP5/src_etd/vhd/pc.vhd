library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;
library work;
use work.CPU_pkg.all;

entity PC is
        Port ( CLK : in  STD_LOGIC;
               RESET : in  STD_LOGIC;
               ctrl:   out  CPU_CTRL;
               CR : in CPU_COMPTE_RENDU;
               WEb : out  STD_LOGIC;
               CEb : out  STD_LOGIC
       );
end PC;

architecture Behavioral of PC is

        -- Signaux de la PC
        type StateType is (fetch,decode,init,ldHad,ldLad ,li ,stinst ,opinst,ldinst, jmpinst);
        signal ETAT_SUIVANT,ETAT_COURANT : StateType;

begin

        Registres_Partie_Controle: process (CLK,RESET) 
        begin 
                if (RESET='1') then 
                        ETAT_COURANT<=init;
                elsif (clk'event and clk='1') then 
                        ETAT_COURANT<=ETAT_SUIVANT;
                end if;
        end process Registres_Partie_Controle ;	

        process (ETAT_COURANT,CR)
        begin 
                -- valeur par defaut des sorties
                WEb<='1';
                CEb<='1';
                ctrl <= CTRL_defaut;
                ctrl.selB<=CR.IR(3 downto 2);
                ctrl.selA<=CR.IR(1 downto 0);
                ctrl.op<=CR.IR(6 downto 4);
                ETAT_SUIVANT<=fetch;

                case ETAT_COURANT is
                        when init =>
                               ctrl.RST<=true;

                        when fetch => 
                                CEb<='0';
                                ctrl.ldIR<=true;
                                ctrl.ldPC<=true;
                                ETAT_SUIVANT<=decode;

                        when decode => 
                                if CR.IR(7)='0' then
                                        ETAT_SUIVANT<=opinst;
                                elsif CR.IR(5)='0' THEN
                                        ETAT_SUIVANT<=ldHad;
                                elsif CR.IR(5)='1' THEN
                                        ETAT_SUIVANT<=li;
                                end if;

                        when opinst =>
                                case CR.IR(1 downto 0) is
                                        when "00" => ctrl.ldR0 <= true;
                                        when "01" => ctrl.ldR1 <= true;
                                        when "10" => ctrl.ldR2 <= true;
                                        when "11" => ctrl.ldR3 <= true;
                                        when others => report "IR impossible" severity failure;
                                end case;
                                ctrl.ldz<=true;

                        when li => 
                                CEb<='0';
                                ctrl.ldPC<=true;
                                case CR.IR(1 downto 0) is
                                        when "00" => ctrl.ldR0 <= true;
                                        when "01" => ctrl.ldR1 <= true;
                                        when "10" => ctrl.ldR2 <= true;
                                        when "11" => ctrl.ldR3 <= true;
                                        when others => report "IR impossible" severity failure;
                                end case;
                                ctrl.selR<=from_input;
                
                        when ldHad =>
                                ctrl.ldADH<=true;
                                ctrl.ldPC<=true;
                                CEb<='0';
                                ETAT_SUIVANT<=ldLad;

                        when ldLad =>
                                ctrl.ldADL<=true;
                                ctrl.ldPC<=true;
                                CEb<='0';
                                if CR.IR(2)='1' THEN
                                        if (CR.z or not CR.IR(0)) = '1' then ETAT_SUIVANT<=jmpinst; end if;
                                elsif CR.IR(6)='1' then
                                        ETAT_SUIVANT<=stinst;
                                else 
                                        ETAT_SUIVANT<=ldinst;
                                end if;

                        when stinst=> 
                                ctrl.selAD<=from_AD;
                                CEb<='0';
                                WEb<='0';
                
                        when ldinst=> 
                                ctrl.selAD<=from_AD;
                                CEb<='0';
                                ctrl.selR<=from_input;
                                case CR.IR(1 downto 0) is
                                        when "00" => ctrl.ldR0 <= true;
                                        when "01" => ctrl.ldR1 <= true;
                                        when "10" => ctrl.ldR2 <= true;
                                        when "11" => ctrl.ldR3 <= true;
                                        when others => report "IR impossible" severity failure;
                                end case;
                
                        when jmpinst=> 
                                ctrl.ldPC <= true;
                                ctrl.selPC <= from_AD;
                end case;
        end process;
end Behavioral;
