# Decision Report

- generated_at: 2026-08-01T05:56:27.373352+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10065**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.20% / filled 20/20。**
- 全期間 MARKET基準: n=10065, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 9/20 | 45.0% | +1.02% | **+0.46%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.96% | **+0.38%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.39% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.74% | **+0.52%** |
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| MARKET_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.31% | **+0.26%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.30% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$565.58** / 初期 $100.00 (+465.58%)
- 確定: 3617件 (Win 1154 / Loss 1184 / Flat 1279) / skip 3009件
- 成長率目線: 平均log +0.000479 / 幾何平均 +0.048% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TLM/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.02% 残高後 $565.58

## 4. Robust Adaptive DryRun ($100)

- 残高: **$140.81** / 初期 $100.00 (+40.81%)
- 確定: 1279件 (Win 359 / Loss 297 / Flat 623) / skip 2197件
- 成長率目線: 平均log +0.000268 / 幾何平均 +0.027% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KOMA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $140.81

## 5. Causal Adaptive DryRun ($100)

- 残高: **$111.79** / 初期 $100.00 (+11.79%)
- 確定: 879件 (Win 284 / Loss 348 / Flat 247) / pending 3件 / skip 655件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000291 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: TLM/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $111.79

## 6. Latest Market Context

- 更新: 2026-08-01T05:56:18.629591+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=63005.9
- Funnel: target 921 → liquid 163 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| GIGGLE/USDT:USDT | +35.97% | $26,581,233.31 |
| JIMOTHY/USDT:USDT | +28.46% | $1,263,063.78 |
| BTW/USDT:USDT | +26.58% | $3,336,329.27 |
| KOMA/USDT:USDT | +19.98% | $18,039,141.50 |
| TLM/USDT:USDT | +13.52% | $1,941,673.94 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.65% | +4.76% |
| BANK/USDT:USDT | below_1h_threshold | +2.19% | +2.30% |
| XPL/USDT:USDT | below_1h_threshold | +1.80% | +1.90% |
| PI/USDT:USDT | below_1h_threshold | +1.44% | +1.55% |
| SYN/USDT:USDT | below_1h_threshold | +1.27% | +1.37% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
