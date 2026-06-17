# Decision Report

- generated_at: 2026-06-17T14:25:38.486923+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6950**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6950, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/15 | 20.0% | +2.91% | **+0.58%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.47% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.16% | **+1.16%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.01% | **+0.81%** |
| ASK_LONG | 20/20 | 100.0% | +0.76% | **+0.76%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.67% | **+0.44%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1698件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定: 223件 (Win 57 / Loss 51 / Flat 115) / skip 138件
- 成長率目線: 平均log +0.000133 / 幾何平均 +0.013% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0847 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $103.01

## 5. Latest Market Context

- 更新: 2026-06-17T14:25:34.321248+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.09% price=65180.0
- Funnel: target 790 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +89.19% | $4,333,384.99 |
| TAC/USDT:USDT | +37.68% | $1,039,090.21 |
| ESPORTS/USDT:USDT | +36.86% | $12,418,567.11 |
| XPL/USDT:USDT | +27.15% | $11,382,961.80 |
| PLAY/USDT:USDT | +26.31% | $3,420,847.34 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +4.67% | +4.76% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +4.35% | +4.44% |
| ARMSTOCK/USDT:USDT | below_1h_threshold | +4.33% | +4.42% |
| BLESS/USDT:USDT | below_1h_threshold | +3.76% | +3.84% |
| WDCSTOCK/USDT:USDT | below_1h_threshold | +3.43% | +3.51% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
