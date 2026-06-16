# Decision Report

- generated_at: 2026-06-16T21:17:27.088523+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6887**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6887, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.13%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.13% | **-0.13%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.37% | **+0.55%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.96% | **+0.19%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.23% | **+0.17%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.09% | **+0.09%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.64% | **+0.51%** |
| MARKET_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |
| ASK_LONG | 20/20 | 100.0% | +0.32% | **+0.32%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.37% | **+0.21%** |

## 2. $100 Live Portfolio

- 残高: **$101.99** / 初期 $100.00 (+1.99%)
- 確定トレード: 11件 (TP 5 / SL 6 / EXP 0)
- 最新: STG/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.99
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$185.43** / 初期 $100.00 (+85.43%)
- 確定: 1760件 (Win 465 / Loss 553 / Flat 742) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $185.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.68** / 初期 $100.00 (-2.32%)
- 確定: 161件 (Win 29 / Loss 31 / Flat 101) / skip 137件
- 成長率目線: 平均log -0.000146 / 幾何平均 -0.015% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0210 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ESPORTS/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $97.68

## 5. Latest Market Context

- 更新: 2026-06-16T21:17:22.934087+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.02% price=65813.3
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PLAY/USDT:USDT | +14.89% | $1,697,613.17 |
| VELVET/USDT:USDT | +14.34% | $28,925,687.79 |
| ESPORTS/USDT:USDT | +14.20% | $1,829,625.51 |
| BLESS/USDT:USDT | +14.09% | $1,812,956.83 |
| H/USDT:USDT | +13.20% | $56,028,262.24 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.61% | +4.63% |
| BCH/USDT:USDT | below_1h_threshold | +1.27% | +1.28% |
| LUNC/USDT:USDT | below_1h_threshold | +1.23% | +1.24% |
| STG/USDT:USDT | below_1h_threshold | +1.14% | +1.15% |
| TAO/USDT:USDT | below_1h_threshold | +0.77% | +0.78% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
