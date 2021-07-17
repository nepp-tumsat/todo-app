<template>
	<v-card width="400px" class="mx-auto mt-5">
		<v-cart-title>
			<h1 class="display-1">ログイン</h1>
		</v-cart-title>
		<v-card-text>
			<v-form>
				<v-text-field
					prepend-icon="mdi-account-circle"
					label="ユーザ名"
					v-model="name"
				></v-text-field>
				<v-text-field
					v-bind:type="showPassword ? 'text' : 'password'"
					v-bind:append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
					@click:append="showPassword = !showPassword"
					prepend-icon="mdi-lock"
					label="パスワード"
					v-model="password"
				>
				</v-text-field>
				<v-card-actions>
					<v-btn class="info" @click="submit">ログイン</v-btn>
				</v-card-actions>
			</v-form>
		</v-card-text>
	</v-card>
</template>

<script>
export default {
	name: "Login",
	data: () => ({
		showPassword: false,
		name: "",
		password: "",
	}),
	methods: {
		submit() {
			console.log(this.name, this.password);
		},
	},
};
</script>
