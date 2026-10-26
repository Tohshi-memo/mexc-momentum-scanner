# Decision Report

- generated_at: 2026-10-26T10:51:46.306333+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17475**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.44% / filled 20/20。**
- 全期間 MARKET基準: n=17475, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.44%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.44% | **+2.44%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.44% | **+2.44%** |
| LIMIT_1PCT | 16/20 | 80.0% | +1.51% | **+1.21%** |
| LIMIT_ATR | 9/20 | 45.0% | +2.56% | **+1.15%** |
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_BB3S | 4/14 | 28.6% | +2.95% | **+0.84%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 6/20 | 30.0% | +5.11% | **+1.53%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +1.55% | **+0.62%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +0.83% | **+0.41%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +0.21% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6719件 (Win 1956 / Loss 2151 / Flat 2612) / skip 7317件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$316.96** / 初期 $100.00 (+216.96%)
- 確定: 4018件 (Win 1113 / Loss 951 / Flat 1954) / skip 6868件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0507 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $316.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5635件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_8PCT` (selected_by_causal_log_growth) / causal_score +0.000241 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T10:51:24.456817+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.13% price=80403.1
- Funnel: target 1073 → liquid 152 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOOD/USDT:USDT | +57.79% | $2,451,108.83 |
| KIMCHI/USDT:USDT | +50.76% | $3,519,051.43 |
| BULLA/USDT:USDT | +50.17% | $2,285,414.40 |
| CLAUDIA/USDT:USDT | +11.45% | $1,139,305.26 |
| QNT/USDT:USDT | +10.99% | $75,321,210.90 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AIGENSYN/USDT:USDT | below_1h_threshold | +1.32% | +1.45% |
| PHA/USDT:USDT | below_1h_threshold | +1.28% | +1.41% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.13% | +1.26% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +1.04% | +1.17% |
| BEAT/USDT:USDT | below_1h_threshold | +0.85% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
