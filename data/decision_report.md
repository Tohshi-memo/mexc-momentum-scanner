# Decision Report

- generated_at: 2026-05-12T09:53:15.958589+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4107**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4107, expectancy=-0.13%
- 直近20件 MARKET基準: n=20, expectancy=-0.92%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.92% | **-0.92%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.50% | **+0.15%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_BB3S | 7/17 | 41.2% | -1.33% | **-0.55%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +3.67% | **+3.67%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.75% | **+2.06%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.08% | **+0.97%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +1.48% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$99.19** / 初期 $100.00 (-0.81%)
- 確定トレード: 34件 (TP 9 / SL 22 / EXP 3)
- 最新: DOGS/USDT:USDT TP_HIT PnL +8.00% 残高後 $99.19
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$114.17** / 初期 $100.00 (+14.17%)
- 確定: 243件 (Win 66 / Loss 83 / Flat 94) / skip 425件
- 成長率目線: 平均log +0.000545 / 幾何平均 +0.055% per trade / maxDD +4.21%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PENGUIN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $114.17

## 4. Latest Market Context

- 更新: 2026-05-12T09:53:12.156145+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=80836.4
- Funnel: target 762 → liquid 194 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 68.8 >= 65=1, 4h RSI 84.2 >= 65=1, 4h RSI 87.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGA/USDT:USDT | +56.57% | $4,373,886.33 |
| SAGA/USDT:USDT | +45.79% | $12,443,329.02 |
| USELESS/USDT:USDT | +40.67% | $7,547,307.81 |
| SKYAI/USDT:USDT | +37.40% | $44,136,781.63 |
| GUA/USDT:USDT | +30.24% | $3,264,268.35 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PENGUIN/USDT:USDT | below_1h_threshold | +4.43% | +4.38% |
| ESPORTS/USDT:USDT | below_1h_threshold | +4.14% | +4.10% |
| DEGEN/USDT:USDT | below_1h_threshold | +3.64% | +3.59% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.92% | +2.88% |
| SAPIEN/USDT:USDT | below_1h_threshold | +2.77% | +2.73% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
