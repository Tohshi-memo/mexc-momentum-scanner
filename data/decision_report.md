# Decision Report

- generated_at: 2026-05-04T01:22:23.927812+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **3123**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=3123, expectancy=-0.16%
- 直近20件 MARKET基準: n=20, expectancy=-0.14%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.14% | **-0.14%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 2/20 | 10.0% | +5.85% | **+0.59%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_5PCT | 5/20 | 25.0% | +0.95% | **+0.24%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.23% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +3.47% | **+1.74%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.72% | **+1.20%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.42% | **+1.00%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.16% | **+0.93%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.00% | **+0.60%** |

## 2. $100 Live Portfolio

- 残高: **$103.21** / 初期 $100.00 (+3.21%)
- 確定トレード: 11件 (TP 5 / SL 5 / EXP 1)
- 最新: AIGENSYN/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-04T01:22:21.847682+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78406.9
- Funnel: target 756 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LAB/USDT:USDT | +66.60% | $244,550,305.92 |
| SKYAI/USDT:USDT | +53.34% | $32,136,358.41 |
| TAG/USDT:USDT | +28.30% | $3,826,546.79 |
| GIGA/USDT:USDT | +22.62% | $1,083,840.81 |
| TRADOOR/USDT:USDT | +17.98% | $3,444,532.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UB/USDT:USDT | below_1h_threshold | +4.29% | +4.41% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.47% | +2.60% |
| BIO/USDT:USDT | below_1h_threshold | +2.23% | +2.35% |
| TST/USDT:USDT | below_1h_threshold | +2.03% | +2.15% |
| B/USDT:USDT | below_1h_threshold | +1.44% | +1.57% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
