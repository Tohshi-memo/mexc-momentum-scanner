# Decision Report

- generated_at: 2026-06-18T02:20:29.508528+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6991**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6991, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-2.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.20% | **-2.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.24% | **+0.11%** |
| LIMIT_10PCT | 6/20 | 30.0% | -0.85% | **-0.25%** |
| LIMIT_8PCT | 7/20 | 35.0% | -1.19% | **-0.41%** |
| LIMIT_5PCT | 10/20 | 50.0% | -1.31% | **-0.66%** |
| LIMIT_7PCT | 7/20 | 35.0% | -2.06% | **-0.72%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK_LONG | 20/20 | 100.0% | +3.80% | **+3.80%** |
| MARKET_LONG | 20/20 | 100.0% | +3.00% | **+3.00%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +3.06% | **+1.84%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.45% | **+1.72%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +1.90% | **+0.76%** |

## 2. $100 Live Portfolio

- 残高: **$100.97** / 初期 $100.00 (+0.97%)
- 確定トレード: 13件 (TP 5 / SL 8 / EXP 0)
- 最新: H/USDT:USDT SL_HIT PnL -4.00% 残高後 $100.97
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$208.82** / 初期 $100.00 (+108.82%)
- 確定: 1837件 (Win 507 / Loss 579 / Flat 751) / skip 1715件
- 成長率目線: 平均log +0.000401 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BP/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $208.82

## 4. Robust Adaptive DryRun ($100)

- 残高: **$105.52** / 初期 $100.00 (+5.52%)
- 確定: 264件 (Win 73 / Loss 67 / Flat 124) / skip 138件
- 成長率目線: 平均log +0.000204 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0951 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BP/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $105.52

## 5. Latest Market Context

- 更新: 2026-06-18T02:20:25.246986+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64549.5
- Funnel: target 790 → liquid 172 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +140.25% | $28,775,204.94 |
| O/USDT:USDT | +76.97% | $1,559,779.32 |
| SYN/USDT:USDT | +40.82% | $4,420,352.77 |
| H/USDT:USDT | +27.18% | $38,600,029.99 |
| MITO/USDT:USDT | +18.84% | $1,749,568.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.50% | +4.46% |
| GUA/USDT:USDT | below_1h_threshold | +4.10% | +4.05% |
| CLO/USDT:USDT | below_1h_threshold | +3.55% | +3.51% |
| BSB/USDT:USDT | below_1h_threshold | +2.99% | +2.94% |
| SIREN/USDT:USDT | below_1h_threshold | +2.98% | +2.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
