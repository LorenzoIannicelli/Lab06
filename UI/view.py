import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab06"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # Elementi UI
        self.txt_titolo = None
        self.txt_responsabile = None
        self.txt_subtitile = None

        # Non obbligatorio mettere già qui tutti gli elementi UI

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        """ Imposta il controller alla pagina """
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge Elementi di UI alla pagina e la aggiorna. """
        self.txt_titolo = ft.Text(value=self.controller.get_nome(), size=38, weight=ft.FontWeight.BOLD)
        self.txt_responsabile = ft.Text(
            value=f"Responsabile: {self.controller.get_responsabile()}",
            size=16,
            weight=ft.FontWeight.BOLD
        )

        # TextField per responsabile
        self.input_responsabile = ft.TextField(value=self.controller.get_responsabile(), label="Responsabile")

        # ListView per mostrare la lista di auto aggiornata
        self.lista_auto = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # TextField per ricerca auto per modello
        self.input_modello_auto = ft.TextField(label="Modello")

        # ListView per mostrare il risultato della ricerca auto per modello
        self.lista_auto_ricerca = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

        # --- PULSANTI e TOGGLE associati a EVENTI ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)
        pulsante_conferma_responsabile = ft.ElevatedButton("Conferma", on_click=self.controller.conferma_responsabile)

        # Altri Pulsanti da implementare (es. "Mostra" e "Cerca")
        self.txt_subtitile = ft.Text(value='Automobili', size=20)
        self.btn_mostra = ft.ElevatedButton("Mostra",
                                            on_click=self.aggiorna_lista_auto)

        self.btn_cerca_auto = ft.ElevatedButton('Cerca',
                                                on_click=self.aggiorna_lista_auto_ricerca)

        # --- LAYOUT ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            self.txt_responsabile,
            ft.Divider(),

            # Sezione 2
            ft.Text("Modifica Informazioni", size=20),
            ft.Row(spacing=200,
                   controls=[self.input_responsabile, pulsante_conferma_responsabile],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3
            ft.Row(spacing=10,
                   controls=[self.txt_subtitile, self.btn_mostra],
                   alignment=ft.MainAxisAlignment.START),
            self.lista_auto,
            ft.Divider(),

            # Sezione 4
            ft.Text('Cerca Automobile', size=20),
            ft.Row(spacing=10,
                   controls=[self.input_modello_auto, self.btn_cerca_auto],
                   alignment=ft.MainAxisAlignment.START),
            self.lista_auto_ricerca
        )

    def cambia_tema(self, e):
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()

    def aggiorna_lista_auto(self, e):
        self.lista_auto.controls.clear()
        automobili = self.controller.get_automobili()
        for auto in automobili:
            self.lista_auto.controls.append(ft.Text(auto))

        self.update()

    def aggiorna_lista_auto_ricerca(self, e):
        try:
            self.lista_auto_ricerca.controls.clear()
            automobili_per_marca = self.controller.get_automobili_per_marca(self.input_modello_auto.value)
            if not automobili_per_marca:
                raise Exception('Errore: nessuna auto trovata!')
            else :
                for auto in automobili_per_marca:
                    self.lista_auto_ricerca.controls.append(ft.Text(auto))
        except Exception as e:
            alert = AlertManager(self.page)
            alert.show_alert(f"❌ {e}")
        finally:
            self.input_modello_auto.value = ''
            self.update()