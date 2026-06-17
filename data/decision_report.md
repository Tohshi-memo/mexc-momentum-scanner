# Decision Report

- generated_at: 2026-06-17T14:05:10.599489+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6947**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6947, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=+0.17%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.56% | **+1.56%** |
| ASK_LONG | 20/20 | 100.0% | +1.14% | **+1.14%** |
| LIMIT_BB3S_LONG | 3/6 | 50.0% | +2.14% | **+1.07%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.74% | **+0.55%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$197.02** / 初期 $100.00 (+97.02%)
- 確定: 1813件 (Win 494 / Loss 572 / Flat 747) / skip 1695件
- 成長率目線: 平均log +0.000374 / 幾何平均 +0.037% per trade / maxDD +7.25%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `MARKET_LONG` EXPIRED account +0.50% 残高後 $197.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$102.49** / 初期 $100.00 (+2.49%)
- 確定: 220件 (Win 55 / Loss 50 / Flat 115) / skip 138件
- 成長率目線: 平均log +0.000112 / 幾何平均 +0.011% per trade / maxDD +3.03%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0728 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTW/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $102.49

## 5. Latest Market Context

- 更新: 2026-06-17T14:05:05.448659+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=65158.2
- Funnel: target 790 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +83.97% | $3,628,026.73 |
| ESPORTS/USDT:USDT | +45.62% | $11,874,419.12 |
| BP/USDT:USDT | +25.91% | $1,091,342.22 |
| XPL/USDT:USDT | +25.02% | $10,853,199.98 |
| PLAY/USDT:USDT | +24.89% | $3,285,422.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +2.25% | +2.38% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.71% | +1.83% |
| PLAY/USDT:USDT | below_1h_threshold | +1.36% | +1.48% |
| BLESS/USDT:USDT | below_1h_threshold | +0.85% | +0.97% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.84% | +0.96% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
