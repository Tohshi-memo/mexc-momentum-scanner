# Decision Report

- generated_at: 2026-10-26T18:21:33.993571+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17505**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.86% / filled 20/20。**
- 全期間 MARKET基準: n=17505, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.86%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.86% | **+0.86%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.73% | **+0.62%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.56% | **+0.36%** |
| LIMIT_5PCT | 4/20 | 20.0% | +1.48% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +0.27% | **+0.05%** |
| LIMIT_BB3S_LONG | 5/8 | 62.5% | +0.07% | **+0.04%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | -0.13% | **-0.07%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,534.60** / 初期 $100.00 (+1434.60%)
- 確定: 6720件 (Win 1956 / Loss 2151 / Flat 2613) / skip 7346件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_10PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DOOD/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $1,534.60

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.14** / 初期 $100.00 (+219.14%)
- 確定: 4040件 (Win 1114 / Loss 951 / Flat 1975) / skip 6876件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0456 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $319.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5672件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000282 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T18:21:19.074781+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=80276.7
- Funnel: target 1078 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +18.41% | $3,636,176.94 |
| CHIP/USDT:USDT | +8.06% | $5,473,422.55 |
| BTW/USDT:USDT | +6.93% | $19,625,620.73 |
| BULLA/USDT:USDT | +4.56% | $8,103,218.01 |
| AAOISTOCK/USDT:USDT | +2.76% | $1,461,310.47 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +3.50% | +3.53% |
| SNXX/USDT:USDT | below_1h_threshold | +3.17% | +3.20% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +2.73% | +2.76% |
| SOXL/USDT:USDT | below_1h_threshold | +1.84% | +1.87% |
| MRVLSTOCK/USDT:USDT | below_1h_threshold | +1.79% | +1.82% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
