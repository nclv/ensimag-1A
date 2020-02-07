library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity auto is
    port ( clk:     in  std_logic;
           reset:   in  std_logic;
           e:       in  std_logic;
           s:       out std_logic);
end auto;

architecture structural of auto is
	type Etat_type is (A,B,C,D,eE); -- On définit un nouveau type "Etat_type" comme étant une énumération de 5 symboles possibles.
		-- comme le langage est insensible à la case on ne peut pas définir un symbole E (entrée e de l'entité déjà existante) on nomme donc cet état eE
    -- Ces symboles pourront être utilisés pour les signaux de ce type.
    signal Etat_courant, Etat_futur: Etat_type; -- on définit nos 2 signaux
begin
	-- On décrit le registre d'état avec un process (pas le choix car on ne connait pas la taille du registre)
	Registre : process (clk)
  begin
    if rising_edge(clk) then
      if (reset='1') then
        Etat_courant <= A
      else
        Etat_courant <= Etat_futur;
      end if;
    end if;
	end process;

    -- Pour décrire la fonction de transition et la fonction de sortie, on peut aussi utiliser un process
	Combinatoire : process (Etat_courant, e)
		-- Liste de sensibilité à compléter avec tous les signaux entrants des fonctions combinatoires
		)
	begin
		s <= '0'; -- Un processus décrit la comportement séquentiellement. Il est donc possible d'attribuer une valeur par défaut dans la description (ici '0') et de changer cette valeur plus loin (avant le end évidemment).
		case Etat_courant is
			when A => -- comprendre : quand Etat_courant vaut A faire ...
				if e = '0' then -- Dans un process, on peut aussi utiliser un if/then/else
					Etat_futur <= A;
				else
					Etat_futur <= B;
				end if;
      when B =>
        if e = '0' then
          Etat_futur <= C;
        else
          Etat_futur <= B;
        end if;
      when C =>
        if e = '0' then
          Etat_futur <= C;
        else
          Etat_futur <= D;
        end if;
      when D =>
        if e = '0' then
          Etat_futur <= C;
        else
          Etat_futur <= eE;
        end if;
      when eE =>
        if e = '0' then
          Etat_futur <= C;
        else
          Etat_futur <= B;
        end if;
		end case; -- fin de la structure case

  s <= '1' when Etat_courant = eE else '0';
	end process;
end structural;
