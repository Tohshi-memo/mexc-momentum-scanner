# Decision Report

- generated_at: 2026-10-26T18:41:39.181149+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17510**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.37% / filled 20/20。**
- 全期間 MARKET基準: n=17510, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.37%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.37% | **+1.37%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.94% | **+0.61%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_6PCT | 6/20 | 30.0% | +0.98% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.89% | **+0.40%** |
| LIMIT_BB3S_LONG | 5/9 | 55.6% | +0.65% | **+0.36%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +0.44% | **+0.11%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -0.12% | **-0.06%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6720件 (Win 1956 / Loss 2151 / Flat 2613) / skip 7351件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.14** / 初期 $100.00 (+219.14%)
- 確定: 4042件 (Win 1114 / Loss 951 / Flat 1977) / skip 6879件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0428 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $319.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5675件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T18:41:23.231617+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=80214.0
- Funnel: target 1078 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +63.80% | $5,079,116.45 |
| CHIP/USDT:USDT | +6.75% | $5,625,626.15 |
| BULLA/USDT:USDT | +4.13% | $8,287,574.52 |
| AAOISTOCK/USDT:USDT | +3.39% | $1,467,966.94 |
| APR/USDT:USDT | +3.13% | $3,842,612.74 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.17% | +3.28% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.73% | +2.84% |
| AGT/USDT:USDT | below_1h_threshold | +2.11% | +2.22% |
| SOXL/USDT:USDT | below_1h_threshold | +1.84% | +1.95% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.90% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
