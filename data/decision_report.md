# Decision Report

- generated_at: 2026-05-02T16:12:22.581921+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2947**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2947, expectancy=-0.17%
- 直近20件 MARKET基準: n=20, expectancy=-0.98%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.98% | **-0.98%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +6.70% | **+1.34%** |
| LIMIT_5PCT | 11/20 | 55.0% | +2.24% | **+1.23%** |
| LIMIT_6PCT | 6/20 | 30.0% | +3.92% | **+1.18%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +5.42% | **+3.39%** |
| LIMIT_ATR_LONG | 18/20 | 90.0% | +2.79% | **+2.51%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +2.69% | **+2.15%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +2.12% | **+1.91%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.17% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 8件 (TP 4 / SL 4 / EXP 0)
- 最新: NAORIS/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-02T16:12:17.743695+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=78487.2
- Funnel: target 755 → liquid 162 → pre 50 → checked 50 → surge 4 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.5 >= 65=1, 4h RSI 86.4 >= 65=1, 4h RSI 96.3 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PHAROS/USDT:USDT | +12.10% | $1,156,485.61 |
| TAG/USDT:USDT | +10.01% | $11,045,081.58 |
| ORDI/USDT:USDT | +8.96% | $20,422,033.27 |
| LAB/USDT:USDT | +6.06% | $176,945,944.69 |
| BASED/USDT:USDT | +4.68% | $1,179,008.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +4.69% | +4.64% |
| TAC/USDT:USDT | below_1h_threshold | +3.94% | +3.90% |
| XNY/USDT:USDT | below_1h_threshold | +2.63% | +2.58% |
| ASTEROID/USDT:USDT | below_1h_threshold | +2.38% | +2.34% |
| ORCA/USDT:USDT | below_1h_threshold | +2.04% | +1.99% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
