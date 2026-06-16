# Decision Report

- generated_at: 2026-06-16T18:49:33.368761+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6879**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6879, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.28%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 4/20 | 20.0% | +0.96% | **+0.19%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.46% | **+0.14%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |
| ASK | 20/20 | 100.0% | -0.23% | **-0.23%** |
| MARKET | 20/20 | 100.0% | -0.28% | **-0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/5 | 100.0% | +3.01% | **+3.01%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.07% | **+0.91%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.28% | **+0.77%** |
| ASK_LONG | 20/20 | 100.0% | +0.44% | **+0.44%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$187.06** / 初期 $100.00 (+87.06%)
- 確定: 1752件 (Win 463 / Loss 549 / Flat 740) / skip 1688件
- 成長率目線: 平均log +0.000357 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $187.06

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.02** / 初期 $100.00 (-1.98%)
- 確定: 157件 (Win 29 / Loss 30 / Flat 98) / skip 133件
- 成長率目線: 平均log -0.000127 / 幾何平均 -0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0619 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $98.02

## 5. Latest Market Context

- 更新: 2026-06-16T18:49:25.186667+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.11% price=65870.7
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +15.19% | $62,435,095.86 |
| VELVET/USDT:USDT | +12.55% | $25,699,847.75 |
| STG/USDT:USDT | +8.34% | $3,548,797.52 |
| ESPORTS/USDT:USDT | +8.03% | $1,660,163.41 |
| UNI/USDT:USDT | +7.31% | $36,319,841.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +2.27% | +2.38% |
| UNI/USDT:USDT | below_1h_threshold | +2.08% | +2.19% |
| XMR/USDT:USDT | below_1h_threshold | +1.71% | +1.83% |
| UAI/USDT:USDT | below_1h_threshold | +1.70% | +1.82% |
| LIT/USDT:USDT | below_1h_threshold | +1.65% | +1.76% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
