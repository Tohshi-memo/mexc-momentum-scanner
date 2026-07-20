# Decision Report

- generated_at: 2026-07-20T20:11:14.377865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9128**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9128, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.42%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.42% | **-1.42%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_6PCT | 3/20 | 15.0% | -0.08% | **-0.01%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |
| LIMIT_BB3S | 2/13 | 15.4% | -1.89% | **-0.29%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -1.29% | **-0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.29% | **+1.15%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.42% | **+1.14%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +1.52% | **+0.84%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.07% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$109.14** / 初期 $100.00 (+9.14%)
- 確定トレード: 123件 (TP 44 / SL 74 / EXP 5)
- 最新: US/USDT:USDT TP_HIT PnL +8.00% 残高後 $109.14
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$404.91** / 初期 $100.00 (+304.91%)
- 確定: 3190件 (Win 997 / Loss 1012 / Flat 1181) / skip 2499件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $404.91

## 4. Robust Adaptive DryRun ($100)

- 残高: **$127.45** / 初期 $100.00 (+27.45%)
- 確定: 1089件 (Win 283 / Loss 221 / Flat 585) / skip 1450件
- 成長率目線: 平均log +0.000223 / 幾何平均 +0.022% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1181 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $127.45

## 5. Causal Adaptive DryRun ($100)

- 残高: **$101.83** / 初期 $100.00 (+1.83%)
- 確定: 326件 (Win 115 / Loss 142 / Flat 69) / pending 5件 / skip 270件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000331 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HEMI/USDT:USDT `MARKET_LONG` EXPIRED account +0.17% 残高後 $101.83

## 6. Latest Market Context

- 更新: 2026-07-20T20:11:06.499668+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.00% price=65116.4
- Funnel: target 885 → liquid 165 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 93.3 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +53.66% | $1,452,719.47 |
| HEMI/USDT:USDT | +29.75% | $1,295,530.15 |
| SOXS/USDT:USDT | +6.65% | $1,020,717.81 |
| ON/USDT:USDT | +5.90% | $1,452,265.69 |
| ACE/USDT:USDT | +5.47% | $35,058,377.58 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXS/USDT:USDT | below_1h_threshold | +2.23% | +2.23% |
| ON/USDT:USDT | below_1h_threshold | +1.52% | +1.52% |
| AXONSTOCK/USDT:USDT | below_1h_threshold | +0.92% | +0.92% |
| RIVER/USDT:USDT | below_1h_threshold | +0.82% | +0.81% |
| SYN/USDT:USDT | below_1h_threshold | +0.56% | +0.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
