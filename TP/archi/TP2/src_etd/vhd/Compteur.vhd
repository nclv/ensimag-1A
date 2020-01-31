library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Compteur is
	generic (n: positive := 17);
	port (cpt : out unsigned(n-1 downto 0);
	      max : in unsigned(n-1 downto 0);
	      clk : in std_logic;
	      rst : in std_logic);
end Compteur;

architecture mixte of Compteur is
	signal cptq, cptd : unsigned(n-1 downto 0);
	signal rst_interne : std_logic;
begin

   -- processus de description du registre 	
	process (clk)
	begin
		if rising_edge(clk) then
			if rst_interne='1' then
				cptq <= (others => '0');
			else
				cptq <= cptd;
			end if;
		end if;
	end process;

	cptd <= cptq + 1; -- incrémenteur
	cpt <= cptq; -- On utilise un signal interne pour ne pas lire sur la sortie

-- On introduit ici l'affectation concurrente conditionnelle qui permet de représenter un multiplexeur 2v1.
-- Ainsi, un multiplexeur commandé par une entrée c ayant 2 entrées de données e0 et e1 et une sortie s pourra être représenté par :
-- s <= e1 when c = '1' else e0 ;
-- Le champ de test nécessite un booléen, ce qui explique qu'on ne peut pas faire le test avec un std_logic. 
-- Ci-dessous un exemple d'application
	rst_interne <= '1' when cptq = max else rst; -- Notez que = réalise un test d'égalité entre 2 unsigned et renvoie un booléen utilisable dans la condition du when. 
end mixte;
