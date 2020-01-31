library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity GeneRGB is
    Port (
          X: in unsigned(8 downto 0);
          Y: in unsigned(7 downto 0);
          DATA: in unsigned(31 downto 0);
          R : OUT unsigned(4 downto 0);
          G : OUT unsigned(5 downto 0);
          B : OUT unsigned(4 downto 0);
          ADDR: out unsigned(14 downto 0)
	);
end GeneRGB;

architecture Behavioral of GeneRGB is
    signal pixel:unsigned(7 downto 0); -- vecteur contenant les 8 bits associés au pixel courant à la sortie du multiplexeur.
begin
-- Conseils : 
-- 1) Pour faire le calcul d'adresse, n'utilisez que l'opérateur arithmétique + et l'opérateur de concaténation & (qui permet de faire des multiplications par des puissances de 2). On notera que le vecteur résultat d'une addition est de la même taille que le plus grand de ses opérandes. Les opérateurs *, / ou mod (bien que très pratique) vous apporteraient des erreurs dures à comprendre. 
-- 2) L'accès à un bit d'un vecteur est possible par exemple DATA(2) 
-- 3) De même, pour l'accès à un sous-vecteur. Exemple, DATA(4 downto 2) 
-- 4) Utilisez le signal pixel pour stocker le signal issu du multiplexeur extrayant le pixel courant du mot mémoire. Pour rappel, la syntaxe de l'affectation concurrente conditionnelle se généralise sous la forme :
-- s <= val0 when condition0 else val1 when condition1 else ... else valn ;
end Behavioral;

