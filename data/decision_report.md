# Decision Report

- generated_at: 2026-10-26T17:41:46.112945+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17500**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17500, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.06%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_2PCT | 15/20 | 75.0% | +0.56% | **+0.42%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.27% | **+0.11%** |
| MARKET | 20/20 | 100.0% | +0.06% | **+0.06%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.60% | **+1.30%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.79% | **+0.47%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_FIB1272_LONG | 9/20 | 45.0% | +0.49% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6720件 (Win 1956 / Loss 2151 / Flat 2613) / skip 7341件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.14** / 初期 $100.00 (+219.14%)
- 確定: 4038件 (Win 1114 / Loss 951 / Flat 1973) / skip 6873件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0576 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $319.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5668件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000199 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T17:41:24.096432+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=80267.4
- Funnel: target 1078 → liquid 158 → pre 50 → checked 50 → surge 3 → strict 3
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +44.57% | $2,435,509.94 |
| CHIP/USDT:USDT | +6.79% | $5,046,454.57 |
| ORDER/USDT:USDT | +5.60% | $1,115,893.24 |
| BULLA/USDT:USDT | +3.85% | $7,858,481.23 |
| APR/USDT:USDT | +3.41% | $4,455,414.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CHIP/USDT:USDT | below_1h_threshold | +3.94% | +3.85% |
| APR/USDT:USDT | below_1h_threshold | +3.39% | +3.30% |
| ETHFI/USDT:USDT | below_1h_threshold | +3.08% | +2.99% |
| NIL/USDT:USDT | below_1h_threshold | +2.33% | +2.25% |
| HYPE/USDT:USDT | below_1h_threshold | +2.07% | +1.99% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
