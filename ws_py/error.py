class OpcodeError(Exception):
	'''
	opcodeが指定されたものではありません
	'''
	pass

class TooLongMessageError(Exception):
	'''
	メッセージは125バイト以下です
	'''
	pass

class FirstFrameBitError(Exception):
	'''
	fin,rsv1,2,3の数値が0,1ではありません
	'''
	pass

class UnavailableToSendError(Exception):
	'''
	データが送信できなかった。
	'''
	pass

class UnavailableToSendHandShakeError(Exception):
	'''
	ハンドシェイクが送信できなかった。
	'''
	pass

class UnavailableToReceiveDataEror(Exception):
	'''
	サーバーからの返信が読み込めなかった。
	'''
	pass

class HashNotMatchError(Exception):
	'''
	サーバーから返ってきたハッシュが自分のものと一致しなかった。
	'''
	pass

