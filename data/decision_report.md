# Decision Report

- generated_at: 2026-10-13T02:41:36.966129+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16623**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16623, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.35% | **-0.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 7/20 | 35.0% | +1.63% | **+0.57%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +0.86% | **+0.47%** |
| LIMIT_10PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |
| LIMIT_9PCT | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | -1.43% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.95% | **+0.81%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.93% | **+0.56%** |
| LIMIT_BB3S_LONG | 5/11 | 45.5% | +0.80% | **+0.36%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | -0.57% | **-0.20%** |

## 2. $100 Live Portfolio

- 残高: **$121.72** / 初期 $100.00 (+21.72%)
- 確定トレード: 238件 (TP 89 / SL 142 / EXP 7)
- 最新: BATON/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.72
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.75** / 初期 $100.00 (+1191.75%)
- 確定: 6293件 (Win 1845 / Loss 2016 / Flat 2432) / skip 6891件
- 成長率目線: 平均log +0.000407 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: STX/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,291.75

## 4. Robust Adaptive DryRun ($100)

- 残高: **$273.99** / 初期 $100.00 (+173.99%)
- 確定: 3641件 (Win 1011 / Loss 855 / Flat 1775) / skip 6393件
- 成長率目線: 平均log +0.000277 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $273.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4786件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000189 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-13T02:41:19.616153+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=82770.8
- Funnel: target 1089 → liquid 189 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| CT/USDT:USDT | +19.27% | $3,210,709.22 |
| MAGIC/USDT:USDT | +14.79% | $10,630,500.02 |
| BAT/USDT:USDT | +7.15% | $3,970,838.85 |
| SOXS/USDT:USDT | +6.96% | $44,087,199.15 |
| SYN/USDT:USDT | +5.61% | $1,098,117.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BAT/USDT:USDT | below_1h_threshold | +3.96% | +3.52% |
| CHIP/USDT:USDT | below_1h_threshold | +3.03% | +2.59% |
| SYN/USDT:USDT | below_1h_threshold | +1.58% | +1.14% |
| RENDER/USDT:USDT | below_1h_threshold | +1.20% | +0.76% |
| S/USDT:USDT | below_1h_threshold | +1.16% | +0.72% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
