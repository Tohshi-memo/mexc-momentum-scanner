# Decision Report

- generated_at: 2026-06-18T08:17:23.866414+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7025**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7025, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +6.30% | **+0.95%** |
| LIMIT_9PCT | 3/20 | 15.0% | +5.72% | **+0.86%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.02% | **+0.66%** |
| LIMIT_8PCT | 4/20 | 20.0% | +2.85% | **+0.57%** |
| MARKET | 20/20 | 100.0% | +0.19% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +0.40% | **+0.40%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.33% | **+0.27%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +0.37% | **+0.20%** |
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +0.24% | **+0.08%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | -0.07% | **-0.03%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$217.20** / 初期 $100.00 (+117.20%)
- 確定: 1871件 (Win 525 / Loss 595 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: US/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $217.20

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.85** / 初期 $100.00 (+5.85%)
- 確定: 298件 (Win 84 / Loss 81 / Flat 133) / skip 138件
- 成長率目線: 平均log +0.000191 / 幾何平均 +0.019% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0760 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: US/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $105.85

## 5. Latest Market Context

- 更新: 2026-06-18T08:17:15.579966+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64492.7
- Funnel: target 793 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +108.49% | $41,059,925.17 |
| O/USDT:USDT | +66.99% | $3,870,363.05 |
| SYN/USDT:USDT | +63.25% | $5,628,053.47 |
| HOME/USDT:USDT | +36.13% | $2,187,690.44 |
| FOLKS/USDT:USDT | +22.27% | $2,657,198.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| US/USDT:USDT | below_1h_threshold | +4.47% | +4.43% |
| LAB/USDT:USDT | below_1h_threshold | +3.00% | +2.97% |
| MITO/USDT:USDT | below_1h_threshold | +1.99% | +1.95% |
| ALLO/USDT:USDT | below_1h_threshold | +1.73% | +1.70% |
| AGT/USDT:USDT | below_1h_threshold | +1.67% | +1.64% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
