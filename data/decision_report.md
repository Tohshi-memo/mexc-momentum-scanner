# Decision Report

- generated_at: 2026-07-03T10:04:03.529969+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **8150**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=8150, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.09%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.09% | **+0.09%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_6PCT | 4/20 | 20.0% | +0.42% | **+0.08%** |
| ASK | 20/20 | 100.0% | +0.08% | **+0.08%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -0.92% | **-0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.68% | **+0.75%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.09% | **+0.49%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.43% | **+0.19%** |
| ASK_LONG | 20/20 | 100.0% | +0.15% | **+0.15%** |
| MARKET_LONG | 20/20 | 100.0% | +0.10% | **+0.10%** |

## 2. $100 Live Portfolio

- 残高: **$102.11** / 初期 $100.00 (+2.11%)
- 確定トレード: 54件 (TP 19 / SL 34 / EXP 1)
- 最新: SKHYNIXSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $102.11
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$283.02** / 初期 $100.00 (+183.02%)
- 確定: 2471件 (Win 759 / Loss 824 / Flat 888) / skip 2240件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.13%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: THE/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $283.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.03** / 初期 $100.00 (+6.03%)
- 確定: 599件 (Win 144 / Loss 142 / Flat 313) / skip 962件
- 成長率目線: 平均log +0.000098 / 幾何平均 +0.010% per trade / maxDD +3.57%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: NEX/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $106.03

## 5. Latest Market Context

- 更新: 2026-07-03T10:03:58.731043+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=61670.0
- Funnel: target 834 → liquid 165 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +50.18% | $1,859,592.05 |
| ARPA/USDT:USDT | +40.97% | $2,227,483.19 |
| RIF/USDT:USDT | +29.30% | $8,299,054.28 |
| ZKP/USDT:USDT | +27.52% | $4,319,949.12 |
| BLESS/USDT:USDT | +25.03% | $5,587,116.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| FLOKI/USDT:USDT | below_1h_threshold | +1.68% | +1.71% |
| PIPPIN/USDT:USDT | below_1h_threshold | +0.67% | +0.69% |
| SYN/USDT:USDT | below_1h_threshold | +0.44% | +0.47% |
| ADA/USDT:USDT | below_1h_threshold | +0.42% | +0.45% |
| US/USDT:USDT | below_1h_threshold | +0.34% | +0.37% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
