# Decision Report

- generated_at: 2026-05-03T19:02:21.153136+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3103**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3103, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-2.79%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.79% | **-2.79%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +2.79% | **+0.98%** |
| LIMIT_5PCT | 11/20 | 55.0% | +1.33% | **+0.73%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 5/20 | 25.0% | +0.74% | **+0.18%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +5.79% | **+3.47%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.91% | **+2.93%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.90% | **+2.46%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +5.29% | **+2.38%** |
| LIMIT_5PCT_LONG | 5/20 | 25.0% | +5.60% | **+1.40%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-03T19:02:19.296587+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=78687.6
- Funnel: target 755 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +62.20% | $295,834,250.66 |
| SKYAI/USDT:USDT | +20.25% | $24,851,048.87 |
| MERL/USDT:USDT | +10.49% | $1,030,051.61 |
| BB/USDT:USDT | +7.61% | $1,518,516.18 |
| ZBT/USDT:USDT | +7.41% | $1,537,904.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SKYAI/USDT:USDT | below_1h_threshold | +2.30% | +2.32% |
| LAB/USDT:USDT | below_1h_threshold | +1.42% | +1.44% |
| BIO/USDT:USDT | below_1h_threshold | +1.03% | +1.05% |
| BB/USDT:USDT | below_1h_threshold | +0.91% | +0.94% |
| AIGENSYN/USDT:USDT | below_1h_threshold | +0.88% | +0.90% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
