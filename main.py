from xml.dom import minidom

import os 
import webbrowser

#----------------------------------------------------------------------------
class Boxes_List():   #lista doblemente enlazada
    def __init__(self) -> None:
        self.boxes_head : Box = None #cabecera
        self.boxes_bottom = None #final
        self.boxes_size = 0

    def add_to_end(self,box,box_posX,box_posY,box_color,font_color):
        new_boxes = Box(box,box_posX,box_posY,box_color,font_color)
        self.boxes_size += 1
        if self.boxes_head is None:
            self.boxes_head = new_boxes
            self.boxes_bottom = new_boxes
        else:
            self.boxes_bottom.setNext_Box(new_boxes)
            new_boxes.setPrevius_Box(self.boxes_bottom)
            self.boxes_bottom = new_boxes
        return new_boxes

    def get_Boxs(self, box):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.get_Box() == box:
                return tmp
            tmp = tmp.getNext_Box()
    
    def get_Boxs_By_Pos(self, pos_x, pos_y):
        tmp = self.boxes_head
        while tmp != None:
            if tmp.getPosX_Box() == pos_x and tmp.getPosY_Box() == pos_y:
                return tmp
            tmp = tmp.getNext_Box()

    def slide_Derecha(self):
        tmp =  self.boxes_head
        while tmp != None:
            tmp = tmp.getColor_Box()

  
    def show_Boxes2(self):
        tmp = self.boxes_head
        while tmp != None:
            print('Color:', tmp.get_Box(), 'Pos X: ', tmp.getPosX_Box(), 'Pos Y: ' , tmp.getPosY_Box())
            tmp = tmp.getNext_Box()
    
    def show_Boxes(self, name , code):
        tmp = self.boxes_head

        #bgcolor="red:purple"
        #bgcolor="purple:pink"
        #bgcolor="red:violet"
        #fillcolor="blue:cyan"
        #fillcolor="red:yellow"
 
        strGrafica = 'digraph G { \n graph [pad="1" bgcolor="purple:pink" style="filled" margin="0"  penwidth="3"] \n'
        strGrafica += 'label = "Nombre Piso: {} Codigo Piso: {}" fontname="Arial Black" fontsize="20pt" \n'.format(name,code)
        strGrafica += 'node [style = filled shape = box height="1" width="1"] \n'
        #strGrafica += 'edge [dir="both" arrowsize = "0.3"] \n'

        while tmp != None:
            strGrafica += '{}[fillcolor= "{}" fontcolor = "{}" pos="{},-{}!"] \n'.format(tmp.get_Box(),tmp.getColor_Box(),tmp.getFont_Box(),tmp.getPosX_Box(),tmp.getPosY_Box())
            tmp = tmp.getNext_Box()

        #tmp = self.boxes_head
        #while tmp != None:
        #    if tmp.getNext_Box() is None:
        #        None
        #    else: 
        #        strGrafica += '{}->{};\n'.format(tmp.get_Box(),tmp.getNext_Box().get_Box())
        #    tmp = tmp.getNext_Box()

        strGrafica += ' } '
        documentotxt = 'textoplano.txt'
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf = 'G{}{}.pdf'.format(name,code)
        os.system( 'neato -Tpdf ' + documentotxt + ' -o ' + pdf )
        webbrowser.open(pdf)

#----------------------------------------------------------------------------

class Box():
    def __init__(self, box,box_posX,box_posY,box_color,font_color) -> None:
        self.box_font: str = font_color
        self.box_color: str = box_color
        self.box_posX: int = box_posX
        self.box_posY: int = box_posY
        self.box =  box
        self.next_box = None
        self.previus = None


    def get_Box(self):
        return self.box

    def set_Box(self, box):
        self.box = box

    def getPosX_Box(self):
        return self.box_posX

    def setPosX_Box(self, box_posX):
        self.box_posX = box_posX

    def getPosY_Box(self):
        return self.box_posY

    def setPosY_Box(self, box_posY):
        self.box_posY = box_posY

    def getColor_Box(self):
        return self.box_color

    def setColor_Box(self, box_color):
        self.box_color = box_color


    def getFont_Box(self):
        return self.box_font

    def setFont_Box(self, box_font):
        self.box_font = box_font

    def getNext_Box(self):
        return self.next_box

    def setNext_Box(self, next_box):
        self.next_box = next_box
    
    def getPrevius_Box(self):
        return self.previus

    def setPrevius_Box(self, previus):
        self.previus = previus

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Patterns_List():
    def __init__(self) -> None:
        self.patterns_head : Pattern = None #cabecera
        self.patterns_bottom = None #final
        self.patterns_size = 0

    def add_to_end(self, pattern_code, patterns):
        new_patterns = Pattern(pattern_code, patterns)
        self.patterns_size += 1
        if self.patterns_head is None:
            self.patterns_head = new_patterns
            self.patterns_bottom = new_patterns
        else:
            self.patterns_bottom.setNext_Pattern(new_patterns)
            self.patterns_bottom = new_patterns
        return new_patterns
        
    def get_Patterns(self, Pattern_Code):
        tmp = self.patterns_head
        while tmp != None:
            if tmp.getCode_Pattern() == Pattern_Code:
                return tmp
            tmp = tmp.getNext_Pattern()

    def show_Patterns(self):
        tmp = self.patterns_head
        for i in range(self.patterns_size):
            print('Codigo Patron: ', tmp.getCode_Pattern(), 'Patron: ' , tmp.get_Pattern())
            tmp = tmp.getNext_Pattern()

#----------------------------------------------------------------------------

class Pattern():
    def __init__(self, pattern_code, pattern) -> None:
        self.pattern_code: str = pattern_code
        self.pattern: str = pattern
        self.color_patterns = Boxes_List()                 
        self.next_pattern = None

    def getNext_Pattern(self):
        return self.next_pattern

    def setNext_Pattern(self, next_pattern):
        self.next_pattern = next_pattern

    def setCode_Pattern(self, pattern_code):
        self.pattern_code = pattern_code

    def getCode_Pattern(self):
        return self.pattern_code

    def set_Pattern(self, pattern):
        self.pattern = pattern

    def get_Pattern(self):
        return self.pattern

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
class Deck_List():
    def __init__(self) -> None:
        self.deck_head : Deck = None #cabecera
        self.deck_bottom = None #final
        self.deck_size = 0

    def add_to_end(self, deck_name, deck_rows, deck_column, deck_flip_price, deck_slide_price):
        new_deck = Deck(deck_name, deck_rows, deck_column, deck_flip_price, deck_slide_price)
        self.deck_size += 1
        if self.deck_head is None:
            self.deck_head = new_deck
            self.deck_bottom = new_deck
        else:
            self.deck_bottom.setNext_Deck(new_deck)
            self.deck_bottom = new_deck
        return new_deck

    def get_Decks(self, deck_name):
        tmp = self.deck_head
        while tmp != None:
            if tmp.getName_Deck() == deck_name:
                return tmp
            tmp = tmp.getNext_Deck()

    def get_size(self):
        count = 0
        node = self.deck_head
        while node != None:
            node = node.getNext_Deck()
            count = count + 1
        return count

    def show_Decks(self):
        tmp = self.deck_head
        for i in range(self.deck_size):
            print('Nombre:', tmp.getName_Deck(), 'Filas:', tmp.getRow_Deck(), 'Columnas: ', tmp.getColumn_Deck(),
                             'flip precio: ', tmp.getFlip_Deck(), 'slide precio: ', tmp.getSlide_Deck())
            tmp = tmp.getNext_Deck()

#----------------------------------------------------------------------------
class Deck():
    def __init__(self, deck_name, deck_rows, deck_column, deck_flip_price, deck_slide_price) -> None:
        self.deck_name: str = deck_name
        self.deck_rows: int = deck_rows
        self.deck_column: int = deck_column
        self.deck_flip_price: int = deck_flip_price
        self.deck_slide_price: int = deck_slide_price
        self.code_patterns = Patterns_List()
        self.next_deck = None

    def getName_Deck(self):
        return self.deck_name
            
    def getRow_Deck(self):
        return self.deck_rows
            
    def getColumn_Deck(self):
        return self.deck_column
            
    def getFlip_Deck(self):
        return self.deck_flip_price
            
    def getSlide_Deck(self):
        return self.deck_slide_price
        
    def getNext_Deck(self):
        return self.next_deck

    def setNext_Deck(self, deck):
        self.next_deck = deck

#----------------------------------------------------------------------------

#Globals
deck_name = ''
rows = 0
columns = 0
slide_price = 0
flip_price = 0
pattern_code = ''
pattern = ''


#----------------------------------------------------------------------------
def MiniDom(ruta, linked_list):
    mydoc = minidom.parse(ruta)
    decks = mydoc.getElementsByTagName('piso')
    for deck in decks:

        deck_name = deck.attributes['nombre'].value
        rows = deck.getElementsByTagName('R')
        columns = deck.getElementsByTagName('C')
        flip = deck.getElementsByTagName('F')
        slide = deck.getElementsByTagName('S')

        for a in rows:
            rows = a.firstChild.data
        for b in columns:
            columns = b.firstChild.data
        for c in flip:
            flip_price = c.firstChild.data
        for d in slide:
            slide_price = d.firstChild.data

        decks = linked_list.add_to_end(deck_name,rows,columns,flip_price,slide_price)

        patternses = deck.getElementsByTagName('patrones')

        for patterns in patternses: 
            patterns = deck.getElementsByTagName('patron')
            for e in patterns:
                pattern_code = e.attributes['codigo'].value
                pattern = (e.firstChild.data)
                codes = decks.code_patterns.add_to_end(pattern_code, pattern)

                pos_x = 0
                pos_y = 0
                contador = 1

                Black = '#000000'
                Withe = '#FFFFFF'
                Font_W = 'white'
                Font_B = 'black'

                for color in pattern:
                    count_rows = 0
                    while int(rows) > count_rows:
                        count_cols = 0
                        if color == 'W':
                            color = 'W{}'.format(str(contador))
                            codes.color_patterns.add_to_end(color,pos_x,pos_y,Withe,Font_W)
                            contador += 1 
                            pos_x += 1    
                        elif color == 'B':
                            color = 'B{}'.format(str(contador))
                            codes.color_patterns.add_to_end(color,pos_x,pos_y,Black,Font_B)
                            contador = contador +1
                            pos_x += 1
                        while int(columns) > count_cols:
                            count_cols += 1
                        if color == 'W':
                            color = 'W{}'.format(str(contador))
                            codes.color_patterns.add_to_end(color,pos_x,pos_y,Withe,Font_W)
                            contador = contador +1
                            pos_x += 1   
                        elif color == 'B':
                            pos_x += 1
                            color = 'B{}'.format(str(contador))
                            codes.color_patterns.add_to_end(color,pos_x,pos_y,Black,Font_B)
                            pos_x += 1
                            contador += 1
                            pos_y += 1
                        count_rows = count_rows + 1
                        if pos_x >= int(columns):
                            pos_y += 1
                            pos_x = 0

#----------------------------------------------------------------------------  

def third_menu(linked: Deck_List,decks1: Deck,codes1: Pattern,colorses1: Box):
    flag = True
    while flag:
        
        print('=======================')
        print('Menu Impresion Pisos')
        print('=======================')
        print('1. Mostrar patrones') #mostrar lista de patrones general
        print('2. Seleccionar un Patron') #Seleccionar un nuevo patron por codigo 
        print('3. Ver patron seleccionado')
        print('4. Imprimir Pasos para el cambio') #instrucciones paso a paso para que el robot construya el nuevo patrón al costo mínimo calculado
        print('5. Verificar costo de Cambio') #costo minimo para realizar cambio hacia el nuevo patron
        print('6. Imprimir el Nuevo Patron')
        print('7. Volver al menu principal')
        print('=======================')

        option = input('> ')

        if option == '1':
            try:
                decks1.code_patterns.show_Patterns()
            except:
                print('Asegurese de haber seleccionado un piso')
        elif option == '2':
            try:
                codigo  = input('Ingrese el codigo del patron que desea seleccionar: ')
                codes2 = decks1.code_patterns.get_Patterns(codigo)
                if codes2 is None:
                    print('Codigo incorrecto')
                else:
                    print('Se ha seleccionado el Codigo: ', codes2.getCode_Pattern())
            except:
                print('Asegurese de haber seleccionado un piso')
        elif option == '3':
            try:
                codes2.color_patterns.show_Boxes(str(decks1.getName_Deck()),str(codes2.getCode_Pattern()) )
                #codes2.color_patterns.show_Boxes2()
                print(('Se ha impreso el Piso {} con codigo {}').format(decks1.getName_Deck(),codes2.getCode_Pattern()))
            except:
                print('Asegurese de haber seleccionado un patron')
        elif option == '4':
            #algoritmo que cambia los colores segun las referencias de las pociciones
            color1: Box = codes1.color_patterns.boxes_head
            color2: Box = codes2.color_patterns.boxes_head

            costo = 0
        
            #piso 1  --> piso 2
            while color1 != None:
                while color2 != None:
                    if color1.getColor_Box() == color2.getColor_Box():
                        pass
                    else:
                        #color 1
                        x1 = color1.getPosY_Box()
                        y1 = color1.getPosX_Box()
                        #color 2
                        x2 = color2.getPosY_Box()
                        y2 = color2.getPosX_Box()
                        #color1 --> color2

                        #if decks1.getFlip_Deck() >= decks1.getSlide_Deck():
                        if codes1.color_patterns.get_Boxs_By_Pos(x1+1,y1) != codes2.color_patterns.get_Boxs_By_Pos(x2,y2) and codes1.color_patterns.get_Boxs_By_Pos(x1,y1-1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2):          
                            color1.setColor_Box(color2.getColor_Box())
                            color1.setFont_Box(color2.getColor_Box())
                            print(('Se ha realizado un Slide en el Patron: {} desde la coordenada: X: {} Y: {} hacia la coordenada X: {} Y: {}').format(codes1.getCode_Pattern(),color2.getPosX_Box(),color2.getPosY_Box(),color1.getPosX_Box(),color1.getPosY_Box()))
                            costo += int(decks1.getSlide_Deck())
                        if codes1.color_patterns.get_Boxs_By_Pos(x1+1,y1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2) and codes1.color_patterns.get_Boxs_By_Pos(x1,y1-1) != codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                            color1.setColor_Box(color2.getColor_Box())
                            color1.setFont_Box(color2.getColor_Box())
                            print(('Se ha realizado un Slide en el Patron: {} desde la coordenada: X: {} Y: {} hacia la coordenada X: {} Y: {}').format(codes1.getCode_Pattern(),color2.getPosX_Box(),color2.getPosY_Box(),color1.getPosX_Box(),color1.getPosY_Box()))
                            costo += int(decks1.getSlide_Deck())
                        if codes1.color_patterns.get_Boxs_By_Pos(x1+1,y1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2) and codes1.color_patterns.get_Boxs_By_Pos(x1,y1-1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                            color1.setColor_Box(color2.getColor_Box())
                            color1.setFont_Box(color2.getColor_Box())
                            print(('Se ha realizado un Flip en el Patron: {} en la coordenada: X: {} Y: {}').format(codes1.getCode_Pattern(),color1.getPosY_Box(),color1.getPosX_Box()))
                            costo += int(decks1.getFlip_Deck())
                        if codes1.color_patterns.get_Boxs_By_Pos(x1+1,y1) != codes2.color_patterns.get_Boxs_By_Pos(x2,y2) and codes1.color_patterns.get_Boxs_By_Pos(x1,y1-1) != codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                            if decks1.getFlip_Deck() > decks1.getSlide_Deck():
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Slide en el Patron: {} desde la coordenada: X: {} Y: {} hacia la coordenada X: {} Y: {}').format(codes1.getCode_Pattern(),color2.getPosX_Box(),color2.getPosY_Box(),color1.getPosX_Box(),color1.getPosY_Box()))
                                costo += int(decks1.getSlide_Deck())
                            else: 
                                decks1.getFlip_Deck() < decks1.getSlide_Deck()
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Slide en el Patron: {} desde la coordenada: X: {} Y: {} hacia la coordenada X: {} Y: {}').format(codes1.getCode_Pattern(),color2.getPosX_Box(),color2.getPosY_Box(),color1.getPosX_Box(),color1.getPosY_Box()))
                                costo += int(decks1.getSlide_Deck())
                        if codes1.color_patterns.get_Boxs_By_Pos((decks1.getColumn_Deck()),y1):
                            if codes1.color_patterns.get_Boxs_By_Pos(x1,y1-1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Flip en el Patron: {} en la coordenada: X: {} Y: {}').format(codes1.getCode_Pattern(),color1.getPosY_Box(),color1.getPosX_Box()))
                                costo += int(decks1.getFlip_Deck())
                            if codes1.color_patterns.get_Boxs_By_Pos(x1,y1-1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Slide en el Patron: {} desde la coordenada: X: {} Y: {} hacia la coordenada X: {} Y: {}').format(codes1.getCode_Pattern(),color2.getPosX_Box(),color2.getPosY_Box(),color1.getPosX_Box(),color1.getPosY_Box()))
                                costo += int(decks1.getSlide_Deck())
                        if codes1.color_patterns.get_Boxs_By_Pos(x1,(decks1.getRow_Deck())):
                            if codes1.color_patterns.get_Boxs_By_Pos(x1+1,y1) == codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Flip en el Patron: {} en la coordenada: X: {} Y: {}').format(codes1.getCode_Pattern(),color1.getPosY_Box(),color1.getPosX_Box()))
                                costo += int(decks1.getFlip_Deck())
                            if codes1.color_patterns.get_Boxs_By_Pos(x1+1,y1) != codes2.color_patterns.get_Boxs_By_Pos(x2,y2):
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Slide en el Patron: {} desde la coordenada: X: {} Y: {} hacia la coordenada X: {} Y: {}').format(codes1.getCode_Pattern(),color2.getPosX_Box(),color2.getPosY_Box(),color1.getPosX_Box(),color1.getPosY_Box()))
                                costo += int(decks1.getSlide_Deck())
                        if codes1.color_patterns.get_Boxs_By_Pos((decks1.getColumn_Deck()),(decks1.getRow_Deck())):
                                color1.setColor_Box(color2.getColor_Box())
                                color1.setFont_Box(color2.getColor_Box())
                                print(('Se ha realizado un Flip en el Patron: {} en la coordenada: X: {} Y: {}').format(codes1.getCode_Pattern(),color1.getPosY_Box(),color1.getPosX_Box()))
                                costo += int(decks1.getFlip_Deck())
                    color1 = color1.getNext_Box()
                    color2 = color2.getNext_Box()
            

        elif option == '5':
            print(('El costo total para el cambio es de: Q. {}').format(costo))
        elif option == '6':
            try:
                codes1.color_patterns.show_Boxes(str(decks1.getName_Deck()),str(codes1.getCode_Pattern()))
                #codes1.color_patterns.show_Boxes2()
                print(('Se ha impreso el Piso {} con codigo {}').format(decks1.getName_Deck(),codes1.getCode_Pattern()))
            except:
                print('Asegurese de haber realizado el cambio de patrones')
        elif option == '7':
            main_menu(linked)
            break
        else:
            print('Opcion Invalida!')


def second_menu(linked):
    flag = True
    while flag:
        print('=======================')
        print('Menu Secundario')
        print('=======================')
        print('1. Buscar piso por nombre')
        print('2. Mostrar patrones')
        print('3. Seleccionar un Patron')
        print('4. Imprimir el Patron')
        print('5. Seleccionar patron de cambio')
        print('6. Volver al menu Principal')
        print('=======================')

        option = input('> ')
        
        name1 = ''
        codigo = ''

        if option == '1':
            try:
                name1 =  input('Ingrese el nombre del piso que desea seleccionar: ')
                decks1: Deck = linked.get_Decks(name1)
                if decks1 is None:
                    print('Nombre incorrecto')
                else:
                    print('Se ha seleccionado el piso: ', decks1.getName_Deck())
            except:
                print('Asegurese de haber cargado la data')
        elif option == '2':
            try:
                decks1.code_patterns.show_Patterns()
            except:
                print('Asegurese de haber seleccionado un piso')

        elif option == '3':
            try:
                codigo  = input('Ingrese el codigo del patron que desea seleccionar: ')
                codes1 = decks1.code_patterns.get_Patterns(codigo)
                if codes1 is None:
                    print('Codigo incorrecto')
                else:
                    print('Se ha seleccionado el Codigo: ', codes1.getCode_Pattern())
            except:
                print('Asegurese de haber cargado un patron')
        elif option == '4':
                colorses1 = codes1.color_patterns.show_Boxes(str(decks1.getName_Deck()),str(codes1.getCode_Pattern()) )
                #colorses1 = codes1.color_patterns.show_Boxes2()
                print(('Se ha impreso el Piso {} con codigo {}').format(decks1.getName_Deck(),codes1.getCode_Pattern()))
        elif option == '5':

            third_menu(linked,decks1,codes1,colorses1)
            break
            
        elif option == '6':
            main_menu(linked)
            break
        else:
            print('Opcion Invalida!')


def main_menu(linked):
    flag = True
    while flag:
        print('=======================')
        print('Menu Principal')
        print('=======================')
        print('1. Cargar Data')
        print('2. Mostrar pisos cargados')
        print('3. Seleccionar un piso')
        print('4. Salir')
        print('=======================')

        option = input('> ')

        if option == '1':
            MiniDom('./Files/Prueba.xml', linked)
            print('La data se ha cargado!')
        elif option == '2':
            print('Pisos Cargados: ')
            linked.show_Decks()
        elif option == '3':
            second_menu(linked)
            break
        elif option == '4':
            flag = False
            print('=======================')
            print('=>Ejecucion Terminada<=')
            print('=======================')
        else:
            print('Opcion Invalida!')

#----------------------------------------------------------------------------

linked_decks = Deck_List()

if __name__ == '__main__':
    main_menu(linked_decks)
