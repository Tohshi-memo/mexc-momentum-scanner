# Decision Report

- generated_at: 2026-10-25T05:51:31.003143+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17407**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17407, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 16/20 | 80.0% | +1.26% | **+1.01%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.49% | **+0.32%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.02% | **+0.25%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +3.00% | **+1.80%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.63% | **+1.45%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.92% | **+1.32%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.65% | **+1.24%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.80% | **+1.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,492.16** / 初期 $100.00 (+1392.16%)
- 確定: 6660件 (Win 1934 / Loss 2122 / Flat 2604) / skip 7308件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $1,492.16

## 4. Robust Adaptive DryRun ($100)

- 残高: **$307.88** / 初期 $100.00 (+207.88%)
- 確定: 3950件 (Win 1092 / Loss 926 / Flat 1932) / skip 6868件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1751 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $307.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5566件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000555 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-25T05:51:14.039007+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.51% price=80482.1
- Funnel: target 1079 → liquid 130 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| APR/USDT:USDT | +100.77% | $3,898,895.00 |
| T/USDT:USDT | +31.77% | $3,073,153.53 |
| USELESS/USDT:USDT | +20.28% | $4,147,111.00 |
| LIGHT/USDT:USDT | +19.21% | $1,346,157.22 |
| AGT/USDT:USDT | +17.24% | $5,713,047.41 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIGHT/USDT:USDT | below_1h_threshold | +2.55% | +3.05% |
| MSTRSTOCK/USDT:USDT | below_1h_threshold | +0.22% | +0.73% |
| CT/USDT:USDT | below_1h_threshold | +0.21% | +0.72% |
| RIVER/USDT:USDT | below_1h_threshold | +0.19% | +0.70% |
| AGT/USDT:USDT | below_1h_threshold | +0.19% | +0.70% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
