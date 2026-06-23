# Decision Report

- generated_at: 2026-06-23T12:24:48.555611+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **7423**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=7423, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.25% | **-1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/18 | 27.8% | +2.10% | **+0.58%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | +0.56% | **+0.08%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.11% | **+0.95%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.33% | **+0.93%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.53% | **+0.84%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.77% | **+0.69%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.34% | **+0.67%** |

## 2. $100 Live Portfolio

- 残高: **$101.94** / 初期 $100.00 (+1.94%)
- 確定トレード: 29件 (TP 11 / SL 18 / EXP 0)
- 最新: RE/USDT:USDT SL_HIT PnL -4.00% 残高後 $101.94
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$231.01** / 初期 $100.00 (+131.01%)
- 確定: 2079件 (Win 617 / Loss 688 / Flat 774) / skip 1905件
- 成長率目線: 平均log +0.000403 / 幾何平均 +0.040% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LAYER/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $231.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$106.59** / 初期 $100.00 (+6.59%)
- 確定: 314件 (Win 90 / Loss 87 / Flat 137) / skip 520件
- 成長率目線: 平均log +0.000203 / 幾何平均 +0.020% per trade / maxDD +3.03%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0199 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RESOLV/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $106.59

## 5. Latest Market Context

- 更新: 2026-06-23T12:24:44.872312+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.20% price=62353.7
- Funnel: target 802 → liquid 169 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARX/USDT:USDT | +29.72% | $17,796,532.20 |
| RESOLV/USDT:USDT | +22.53% | $9,434,956.31 |
| BR/USDT:USDT | +19.48% | $1,528,437.53 |
| BTW/USDT:USDT | +14.38% | $20,383,000.36 |
| BLESS/USDT:USDT | +14.15% | $21,630,704.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ALGO/USDT:USDT | below_1h_threshold | +4.46% | +4.66% |
| BLESS/USDT:USDT | below_1h_threshold | +4.36% | +4.56% |
| MYX/USDT:USDT | below_1h_threshold | +1.30% | +1.50% |
| BTW/USDT:USDT | below_1h_threshold | +1.17% | +1.37% |
| RE/USDT:USDT | below_1h_threshold | +0.98% | +1.18% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
