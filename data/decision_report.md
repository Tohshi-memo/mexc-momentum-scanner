# Decision Report

- generated_at: 2026-09-24T21:31:28.708766+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15492**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15492, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.34%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.34% | **-0.34%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_6PCT | 4/20 | 20.0% | -1.01% | **-0.20%** |
| LIMIT_3PCT | 16/20 | 80.0% | -0.26% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 8/13 | 61.5% | +2.92% | **+1.80%** |
| MARKET_LONG | 20/20 | 100.0% | +1.42% | **+1.42%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.63% | **+1.31%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.90% | **+1.24%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.48% | **+1.03%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6153件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.55** / 初期 $100.00 (+153.55%)
- 確定: 3437件 (Win 949 / Loss 792 / Flat 1696) / skip 5466件
- 成長率目線: 平均log +0.000271 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0009 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ETC/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.84** / 初期 $100.00 (+20.84%)
- 確定: 3161件 (Win 932 / Loss 1248 / Flat 981) / pending 2件 / skip 3804件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `見送り` (no_strategy_passed_causal_filters) / causal_score n/a / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.17% 残高後 $120.84

## 6. Latest Market Context

- 更新: 2026-09-24T21:31:15.696701+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=84384.7
- Funnel: target 1069 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.9 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +33.22% | $2,482,262.61 |
| XAI/USDT:USDT | +19.46% | $9,910,762.67 |
| LSK/USDT:USDT | +16.46% | $18,721,780.41 |
| CHIP/USDT:USDT | +9.74% | $1,206,823.10 |
| XPL/USDT:USDT | +9.57% | $11,262,025.97 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XPL/USDT:USDT | below_1h_threshold | +2.85% | +2.77% |
| NEAR/USDT:USDT | below_1h_threshold | +1.39% | +1.32% |
| CHIP/USDT:USDT | below_1h_threshold | +1.23% | +1.16% |
| AR/USDT:USDT | below_1h_threshold | +1.14% | +1.06% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.08% | +1.00% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
