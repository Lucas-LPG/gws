function deleteUser(userId) {
  if (confirm("Tem certeza que deseja deletar esse usuário?")) {
    console.log(userId);
    fetch("/delete_user", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ userId: userId }),
    })
      .then((response) => {
        location.reload();

        if (response.ok) {
          console.log("Usuário deletado com sucesso!");
        } else {
          console.error("Erro ao deletar usuário");
        }
      })
      .catch((error) => {
        console.error("Erro ao deletar usuário: ", error);
      });
  }
}
