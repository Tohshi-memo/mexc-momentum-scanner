# Decision Report

- generated_at: 2026-09-06T12:11:24.481337+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13810**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=13810, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_1PCT | 16/20 | 80.0% | +0.78% | **+0.63%** |
| LIMIT_3PCT | 12/20 | 60.0% | +0.72% | **+0.43%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.36% | **+0.14%** |
| LIMIT_2PCT | 14/20 | 70.0% | +0.20% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +5.23% | **+3.14%** |
| LIMIT_ATR_LONG | 17/20 | 85.0% | +1.24% | **+1.05%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +0.57% | **+0.37%** |
| LIMIT_FIB1272_LONG | 13/20 | 65.0% | +0.46% | **+0.30%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.30% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.04** / 初期 $100.00 (+21.04%)
- 確定トレード: 205件 (TP 77 / SL 123 / EXP 5)
- 最新: BONER/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.04
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$847.68** / 初期 $100.00 (+747.68%)
- 確定: 5116件 (Win 1536 / Loss 1674 / Flat 1906) / skip 5255件
- 成長率目線: 平均log +0.000418 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $847.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$191.89** / 初期 $100.00 (+91.89%)
- 確定: 2555件 (Win 715 / Loss 609 / Flat 1231) / skip 4666件
- 成長率目線: 平均log +0.000255 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $191.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.28** / 初期 $100.00 (+19.28%)
- 確定: 2422件 (Win 721 / Loss 923 / Flat 778) / pending 5件 / skip 2856件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000151 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $119.28

## 6. Latest Market Context

- 更新: 2026-09-06T12:11:14.555223+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=79852.0
- Funnel: target 1054 → liquid 125 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +46.71% | $169,528,151.66 |
| FONE/USDT:USDT | +40.32% | $1,004,382.43 |
| FLOCK/USDT:USDT | +40.26% | $1,942,618.09 |
| RAY/USDT:USDT | +37.91% | $4,329,040.04 |
| JUP/USDT:USDT | +21.78% | $7,854,802.07 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASECAT/USDT:USDT | below_1h_threshold | +2.48% | +2.52% |
| WLD/USDT:USDT | below_1h_threshold | +1.49% | +1.52% |
| TAO/USDT:USDT | below_1h_threshold | +1.25% | +1.28% |
| LDO/USDT:USDT | below_1h_threshold | +0.96% | +1.00% |
| JUP/USDT:USDT | below_1h_threshold | +0.78% | +0.81% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
