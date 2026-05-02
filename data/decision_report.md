# Decision Report

- generated_at: 2026-05-02T12:31:53.525884+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2901**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2901, expectancy=-0.14%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.59% | **+0.88%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.17% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +4.13% | **+2.68%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +3.23% | **+2.42%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.91% | **+2.04%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.67% | **+1.20%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.17% | **+1.19%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T12:31:51.526797+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78177.8
- Funnel: target 755 → liquid 168 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1, 4h RSI 69.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +219.31% | $126,530,989.89 |
| TAG/USDT:USDT | +35.48% | $5,235,571.02 |
| BIO/USDT:USDT | +29.32% | $2,161,439.82 |
| TAC/USDT:USDT | +28.13% | $1,998,652.85 |
| SPACE/USDT:USDT | +21.03% | $1,246,191.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BIO/USDT:USDT | below_1h_threshold | +3.50% | +3.41% |
| LAB/USDT:USDT | below_1h_threshold | +3.47% | +3.38% |
| MOVR/USDT:USDT | below_1h_threshold | +3.24% | +3.14% |
| BLESS/USDT:USDT | below_1h_threshold | +3.03% | +2.94% |
| USTC/USDT:USDT | below_1h_threshold | +2.44% | +2.35% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
