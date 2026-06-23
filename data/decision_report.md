# Decision Report

- generated_at: 2026-06-23T00:53:58.057760+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7402**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7402, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | -0.02% | **-0.01%** |
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.87% | **+1.12%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.92% | **+0.87%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.97% | **+0.73%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.18% | **+0.44%** |
| ASK_LONG | 20/20 | 100.0% | +0.41% | **+0.41%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$233.87** / 初期 $100.00 (+133.87%)
- 確定: 2058件 (Win 611 / Loss 678 / Flat 769) / skip 1905件
- 成長率目線: 平均log +0.000413 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $233.87

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 313件 (Win 89 / Loss 87 / Flat 137) / skip 500件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-06-23T00:53:50.750923+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=64067.1
- Funnel: target 808 → liquid 161 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +28.30% | $12,496,384.06 |
| FOLKS/USDT:USDT | +14.72% | $4,038,378.61 |
| FIDA/USDT:USDT | +13.99% | $1,142,754.83 |
| VELVET/USDT:USDT | +11.13% | $19,894,317.91 |
| SYN/USDT:USDT | +10.56% | $30,670,659.19 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BASED/USDT:USDT | below_1h_threshold | +4.38% | +4.26% |
| FIDA/USDT:USDT | below_1h_threshold | +4.13% | +4.01% |
| ID/USDT:USDT | below_1h_threshold | +3.53% | +3.41% |
| FET/USDT:USDT | below_1h_threshold | +2.21% | +2.08% |
| MMT/USDT:USDT | below_1h_threshold | +1.15% | +1.03% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
