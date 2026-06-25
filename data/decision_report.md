# Decision Report

- generated_at: 2026-06-25T10:45:41.248809+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7542**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7542, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.55%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.55% | **-0.55%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| ASK | 20/20 | 100.0% | +0.15% | **+0.15%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.00% | **-0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +3.11% | **+2.08%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +2.37% | **+1.77%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +2.71% | **+1.76%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +2.70% | **+1.48%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +1.81% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$102.94** / 初期 $100.00 (+2.94%)
- 確定トレード: 39件 (TP 15 / SL 24 / EXP 0)
- 最新: MUSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$219.24** / 初期 $100.00 (+119.24%)
- 確定: 2132件 (Win 629 / Loss 715 / Flat 788) / skip 1971件
- 成長率目線: 平均log +0.000368 / 幾何平均 +0.037% per trade / maxDD +8.13%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: UB/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $219.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.99** / 初期 $100.00 (+6.99%)
- 確定: 354件 (Win 99 / Loss 96 / Flat 159) / skip 599件
- 成長率目線: 平均log +0.000191 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_robust_growth_score) / robust_score +0.0838 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SYN/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $106.99

## 5. Latest Market Context

- 更新: 2026-06-25T10:45:36.698216+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.54% price=61375.3
- Funnel: target 807 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BAS/USDT:USDT | +24.76% | $9,874,969.03 |
| RESOLV/USDT:USDT | +21.75% | $3,201,982.78 |
| SLX/USDT:USDT | +20.55% | $18,174,123.34 |
| SYN/USDT:USDT | +19.11% | $17,373,145.69 |
| MUSTOCK/USDT:USDT | +18.49% | $129,144,654.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.58% | +4.12% |
| EDEN/USDT:USDT | below_1h_threshold | +3.29% | +3.83% |
| VELVET/USDT:USDT | below_1h_threshold | +2.72% | +3.26% |
| RESOLV/USDT:USDT | below_1h_threshold | +1.85% | +2.39% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.50% | +2.04% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
