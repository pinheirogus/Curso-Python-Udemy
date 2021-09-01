
if __name__ == '__main__':
    try:
        import sys
        import os

        sys.path.append(
            os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__),
                    '../'
                )
            )
        )
    except ImportError:
        raise
else:
    import Modulos_Padrao.aula84