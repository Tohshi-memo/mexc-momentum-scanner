# Decision Report

- generated_at: 2026-06-27T06:13:33.468705+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7672**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7672, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 8/20 | 40.0% | +2.65% | **+1.06%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.66% | **+0.83%** |
| LIMIT_7PCT | 3/20 | 15.0% | +4.54% | **+0.68%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.08% | **-0.02%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.48% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.20% | **+1.20%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.39% | **+0.98%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +1.76% | **+0.88%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.38% | **+0.83%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.13** / 初期 $100.00 (+138.13%)
- 確定: 2197件 (Win 659 / Loss 731 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $238.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.52** / 初期 $100.00 (+8.52%)
- 確定: 403件 (Win 110 / Loss 100 / Flat 193) / skip 680件
- 成長率目線: 平均log +0.000203 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0845 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $108.52

## 5. Latest Market Context

- 更新: 2026-06-27T06:13:28.969826+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.19% price=60091.4
- Funnel: target 806 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +42.11% | $46,069,137.84 |
| MYX/USDT:USDT | +35.90% | $5,938,742.12 |
| PUNDIX/USDT:USDT | +26.09% | $5,888,702.38 |
| SLX/USDT:USDT | +16.67% | $10,432,686.64 |
| SYRUP/USDT:USDT | +16.08% | $1,309,794.92 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MYX/USDT:USDT | below_1h_threshold | +3.12% | +3.32% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.80% | +1.99% |
| SLX/USDT:USDT | below_1h_threshold | +1.01% | +1.21% |
| ICNT/USDT:USDT | below_1h_threshold | +0.55% | +0.74% |
| UB/USDT:USDT | below_1h_threshold | +0.21% | +0.41% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
