# Decision Report

- generated_at: 2026-06-25T07:23:27.633264+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7533**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7533, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.58% | **-0.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/15 | 26.7% | +1.21% | **+0.32%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.07% | **+0.07%** |
| LIMIT_4PCT | 10/20 | 50.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +4.23% | **+2.12%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +3.46% | **+1.90%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.52% | **+1.89%** |
| LIMIT_ATR_LONG | 16/20 | 80.0% | +1.97% | **+1.58%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +3.10% | **+1.24%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 1962件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.76** / 初期 $100.00 (+6.76%)
- 確定: 350件 (Win 98 / Loss 95 / Flat 157) / skip 594件
- 成長率目線: 平均log +0.000187 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BSB/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $106.76

## 5. Latest Market Context

- 更新: 2026-06-25T07:23:21.892455+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.11% price=61761.0
- Funnel: target 807 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=1, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SLX/USDT:USDT | +32.59% | $15,116,594.72 |
| RESOLV/USDT:USDT | +21.39% | $2,789,894.83 |
| MUSTOCK/USDT:USDT | +19.19% | $116,533,978.63 |
| KORU/USDT:USDT | +17.57% | $5,465,096.63 |
| SOXL/USDT:USDT | +14.12% | $5,671,616.44 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_relative_strength | +5.03% | +4.92% |
| EVAA/USDT:USDT | below_1h_threshold | +3.19% | +3.08% |
| POPCAT/USDT:USDT | below_1h_threshold | +2.57% | +2.46% |
| BAS/USDT:USDT | below_1h_threshold | +2.41% | +2.30% |
| SOXL/USDT:USDT | below_1h_threshold | +1.89% | +1.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
