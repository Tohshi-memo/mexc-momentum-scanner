# Decision Report

- generated_at: 2026-09-20T10:36:49.955100+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15170**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15170, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.76%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.76% | **-1.76%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 5/20 | 25.0% | +0.80% | **+0.20%** |
| LIMIT_9PCT | 6/20 | 30.0% | -0.57% | **-0.17%** |
| LIMIT_8PCT | 6/20 | 30.0% | -0.72% | **-0.21%** |
| LIMIT_6PCT | 9/20 | 45.0% | -0.70% | **-0.32%** |
| LIMIT_BB3S | 5/11 | 45.5% | -0.98% | **-0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.70% | **+1.89%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +3.11% | **+1.87%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.57% | **+1.79%** |
| LIMIT_BB3S_LONG | 2/9 | 22.2% | +8.00% | **+1.78%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +3.01% | **+1.36%** |

## 2. $100 Live Portfolio

- 残高: **$120.56** / 初期 $100.00 (+20.56%)
- 確定トレード: 215件 (TP 79 / SL 131 / EXP 5)
- 最新: BULLA/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.56
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,216.81** / 初期 $100.00 (+1116.81%)
- 確定: 5696件 (Win 1704 / Loss 1836 / Flat 2156) / skip 6035件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTW/USDT:USDT `LIMIT_3PCT_LONG` TP_HIT account +1.00% 残高後 $1,216.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$247.51** / 初期 $100.00 (+147.51%)
- 確定: 3279件 (Win 910 / Loss 764 / Flat 1605) / skip 5302件
- 成長率目線: 平均log +0.000276 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AKE/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $247.51

## 5. Causal Adaptive DryRun ($100)

- 残高: **$121.37** / 初期 $100.00 (+21.37%)
- 確定: 2978件 (Win 880 / Loss 1179 / Flat 919) / pending 0件 / skip 3671件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000127 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CATE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $121.37

## 6. Latest Market Context

- 更新: 2026-09-20T10:36:30.554150+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=80354.1
- Funnel: target 1050 → liquid 147 → pre 50 → checked 50 → surge 6 → strict 0
- Surge前reject: below_1h_threshold=44, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.9 >= 65=1, 4h RSI 67.0 >= 65=1, 4h RSI 76.8 >= 65=1, 4h RSI 74.3 >= 65=1, 4h RSI 75.7 >= 65=1, 4h RSI 65.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +87.16% | $73,272,041.34 |
| CELR/USDT:USDT | +64.69% | $6,933,973.25 |
| ONE/USDT:USDT | +30.86% | $53,218,193.45 |
| BTW/USDT:USDT | +26.99% | $1,974,339.03 |
| EVAA/USDT:USDT | +25.83% | $2,294,922.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZAMA/USDT:USDT | below_1h_threshold | +3.47% | +3.58% |
| VVV/USDT:USDT | below_1h_threshold | +2.85% | +2.96% |
| TAG/USDT:USDT | below_1h_threshold | +1.52% | +1.62% |
| TOKYOELSTOCK/USDT:USDT | below_1h_threshold | +1.32% | +1.43% |
| CAKE/USDT:USDT | below_1h_threshold | +0.52% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
