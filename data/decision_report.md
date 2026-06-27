# Decision Report

- generated_at: 2026-06-27T07:04:52.051303+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7674**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7674, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 7/20 | 35.0% | +1.89% | **+0.66%** |
| LIMIT_5PCT | 10/20 | 50.0% | +0.95% | **+0.48%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | -0.08% | **-0.02%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.60% | **+1.60%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.04% | **+1.43%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| ASK_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +1.86% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$102.65** / 初期 $100.00 (+2.65%)
- 確定トレード: 41件 (TP 15 / SL 25 / EXP 1)
- 最新: M/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.65
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$238.12** / 初期 $100.00 (+138.12%)
- 確定: 2199件 (Win 660 / Loss 732 / Flat 807) / skip 2036件
- 成長率目線: 平均log +0.000395 / 幾何平均 +0.039% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MYX/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $238.12

## 4. Robust Adaptive DryRun ($100)

- 残高: **$108.60** / 初期 $100.00 (+8.60%)
- 確定: 405件 (Win 111 / Loss 101 / Flat 193) / skip 680件
- 成長率目線: 平均log +0.000204 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0953 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $108.60

## 5. Latest Market Context

- 更新: 2026-06-27T07:04:47.401760+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=60316.0
- Funnel: target 806 → liquid 154 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +45.13% | $52,855,051.14 |
| MYX/USDT:USDT | +34.36% | $8,940,570.45 |
| PUNDIX/USDT:USDT | +27.68% | $5,992,521.09 |
| SLX/USDT:USDT | +19.15% | $10,455,113.88 |
| SYRUP/USDT:USDT | +19.07% | $1,491,412.28 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SYN/USDT:USDT | below_1h_threshold | +3.30% | +3.35% |
| MYX/USDT:USDT | below_1h_threshold | +1.36% | +1.41% |
| SLX/USDT:USDT | below_1h_threshold | +1.03% | +1.08% |
| PORTAL/USDT:USDT | below_1h_threshold | +0.98% | +1.03% |
| RE/USDT:USDT | below_1h_threshold | +0.62% | +0.67% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
