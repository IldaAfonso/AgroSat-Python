from conexao import conectar

from modules.usuarios import (
cadastrar_usuario,
listar_usuarios,
atualizar_usuario,
excluir_usuario
)

from modules.propriedades import (
cadastrar_propriedade,
listar_propriedades,
atualizar_propriedade,
excluir_propriedade
)

from modules.clima import (
cadastrar_clima,
listar_clima,
atualizar_clima,
excluir_clima
)

from modules.energia import (
cadastrar_energia,
listar_energia,
atualizar_energia,
excluir_energia
)

from modules.caminhoes import (
cadastrar_caminhao,
listar_caminhoes,
atualizar_caminhao,
excluir_caminhao
)

import modules.alertas

from modules.dashboard import exibir_dashboard
