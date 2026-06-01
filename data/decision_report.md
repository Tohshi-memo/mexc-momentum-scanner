# Decision Report

- generated_at: 2026-06-01T14:13:17.701271+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **5323**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=5323, expectancy=-0.05%
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
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.68% | **+0.34%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| ASK | 20/20 | 100.0% | +0.23% | **+0.23%** |
| MARKET | 20/20 | 100.0% | +0.17% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.10% | **+0.99%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |
| ASK_LONG | 20/20 | 100.0% | +0.74% | **+0.74%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +0.48% | **+0.34%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.11% | **+0.33%** |

## 2. $100 Live Portfolio

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定トレード: 82件 (TP 24 / SL 55 / EXP 3)
- 最新: GUA/USDT:USDT SL_HIT PnL -4.00% 残高後 $97.60
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$131.03** / 初期 $100.00 (+31.03%)
- 確定: 894件 (Win 207 / Loss 269 / Flat 418) / skip 990件
- 成長率目線: 平均log +0.000302 / 幾何平均 +0.030% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BSB/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $131.03

## 4. Latest Market Context

- 更新: 2026-06-01T14:13:15.267257+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.17% price=71576.1
- Funnel: target 776 → liquid 136 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +109.58% | $42,146,000.59 |
| PORTAL/USDT:USDT | +89.16% | $39,568,016.11 |
| SLX/USDT:USDT | +68.12% | $9,440,352.95 |
| LAB/USDT:USDT | +66.78% | $229,335,567.11 |
| VIC/USDT:USDT | +41.06% | $1,489,170.45 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.17% | +2.35% |
| DELLSTOCK/USDT:USDT | below_1h_threshold | +1.81% | +1.98% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.31% | +1.48% |
| HOME/USDT:USDT | below_1h_threshold | +1.28% | +1.46% |
| H/USDT:USDT | below_1h_threshold | +0.95% | +1.12% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
