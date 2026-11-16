# Decision Report

- generated_at: 2026-11-16T06:46:26.140503+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18999**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.82% / filled 20/20。**
- 全期間 MARKET基準: n=18999, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.82%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.82% | **+0.82%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +4.09% | **+0.41%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.20% | **+0.10%** |
| LIMIT_8PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |
| LIMIT_10PCT | 3/20 | 15.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/7 | 42.9% | +2.76% | **+1.18%** |
| LIMIT_4PCT_LONG | 14/20 | 70.0% | +1.16% | **+0.81%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +0.58% | **+0.44%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.83% | **+0.41%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.01% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 276件 (TP 100 / SL 168 / EXP 8)
- 最新: IDOL/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,720.06** / 初期 $100.00 (+1620.06%)
- 確定: 7340件 (Win 2108 / Loss 2351 / Flat 2881) / skip 8220件
- 成長率目線: 平均log +0.000388 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JCT/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,720.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$429.80** / 初期 $100.00 (+329.80%)
- 確定: 4983件 (Win 1331 / Loss 1081 / Flat 2571) / skip 7427件
- 成長率目線: 平均log +0.000293 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $429.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7159件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000144 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-16T06:46:09.144247+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=64607.6
- Funnel: target 1066 → liquid 116 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RARE/USDT:USDT | +52.69% | $7,757,575.46 |
| SKR/USDT:USDT | +28.92% | $2,119,610.23 |
| SHELL/USDT:USDT | +10.99% | $1,543,761.79 |
| JCT/USDT:USDT | +10.28% | $9,670,200.29 |
| EVAA/USDT:USDT | +5.71% | $18,347,565.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| EVAA/USDT:USDT | below_1h_threshold | +3.12% | +2.87% |
| BARD/USDT:USDT | below_1h_threshold | +2.49% | +2.24% |
| SOXS/USDT:USDT | below_1h_threshold | +1.91% | +1.66% |
| ASTER/USDT:USDT | below_1h_threshold | +1.21% | +0.96% |
| VVV/USDT:USDT | below_1h_threshold | +1.08% | +0.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
