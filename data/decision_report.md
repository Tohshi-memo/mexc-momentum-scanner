# Decision Report

- generated_at: 2026-06-13T18:12:56.241541+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6596**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6596, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.02%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.02% | **-1.02%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_3PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.00% | **+0.00%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.91% | **+1.46%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.08% | **+1.25%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.69% | **+1.21%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +1.40% | **+0.98%** |
| ASK_LONG | 20/20 | 100.0% | +0.49% | **+0.49%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.79** / 初期 $100.00 (+67.79%)
- 確定: 1469件 (Win 394 / Loss 465 / Flat 610) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $167.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.58** / 初期 $100.00 (+0.58%)
- 確定: 7件 (Win 3 / Loss 1 / Flat 3) / skip 0件
- 成長率目線: 平均log +0.000822 / 幾何平均 +0.082% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0469 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $100.58

## 5. Latest Market Context

- 更新: 2026-06-13T18:12:52.316256+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.13% price=64020.1
- Funnel: target 770 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +14.52% | $62,453,430.36 |
| NOT/USDT:USDT | +5.58% | $2,679,018.91 |
| SKYAI/USDT:USDT | +4.25% | $18,481,202.80 |
| SQD/USDT:USDT | +2.54% | $2,165,639.50 |
| EDGE/USDT:USDT | +2.40% | $3,510,877.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +2.69% | +2.56% |
| EDGE/USDT:USDT | below_1h_threshold | +1.75% | +1.63% |
| H/USDT:USDT | below_1h_threshold | +1.68% | +1.56% |
| SIREN/USDT:USDT | below_1h_threshold | +1.25% | +1.12% |
| CHZ/USDT:USDT | below_1h_threshold | +1.07% | +0.94% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
